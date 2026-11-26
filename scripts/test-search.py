#!/usr/bin/env python3
"""Build a ready-made saved search for testing Foothold in the Claude app.

For developers only. It is not part of the plugin and no candidate ever sees
it. It takes the invented sample search in tests/fixtures (Sam Example, with
the interview and the research already done and seven roles at different
stages), moves every date so the search reads as if it were today, and writes
the save files a test project can load in one step. That skips the interview
and the research run, which together take most of an hour.

    scripts/test-search.py                     write dist/test-search/
    scripts/test-search.py --place Dublin      put Sam in a real place, so a daily check can find real adverts
    scripts/test-search.py --today 2027-01-15  build it for another day
    scripts/test-search.py --out <folder>      write somewhere else

Standard library only. CONTRIBUTING.md says how to use what it writes.
"""
import argparse
import datetime
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SAMPLE = REPO / "tests" / "fixtures" / "sample-search"
PIPELINE = REPO / "plugins" / "foothold" / "skills" / "engine" / "scripts" / "pipeline.py"
SAMPLE_DAY = "2026-11-26"       # the day the sample search was written for. The tests use the same day
SAMPLE_PLACE = "Testville"
OURS = ".test-search"           # marks a folder this script wrote, so it never clears anyone else's
TEXT = {".md", ".txt", ".json", ".log", ""}
DATE = re.compile(r"(?<!\d)(20\d{2})-(\d{2})-(\d{2})(?!\d)")

PROMPT = """This is a developer test of the Foothold plugin. Nobody real is looking for a job here.

The attached files are a saved search for an invented person, Sam Example. The interview and the research are already in it. Load it in place of both. If the attachment is a zip file, unzip it first.

1. Load the engine skill and read its storage reference.
2. Create the workspace: pipeline init ./job-search --cloud
3. Run the storage test as the storage reference describes. Stop if it fails.
4. Run pipeline restore on core.txt first, then on every other attached save file except latest.txt. If one is REFUSED, stop and say which.
5. Write every attached save file except core.txt and latest.txt to this project as job-search/<its name>, passing the file itself, unchanged.
6. Run pipeline check. Stop if it fails.
7. Close with: pipeline close "a test search was loaded". Store what it prints in this project as the storage reference describes.
8. Run pipeline doctor and tell me every line that is not OK.

Do not run the interview. Do not run research. Do not look for new jobs yet.

Finish by telling me, in the words Sam would see, what needs doing today.
"""


def shift_dates(text, days):
    def move(m):
        try:
            day = datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        except ValueError:
            return m.group(0)
        return (day + datetime.timedelta(days=days)).isoformat()
    return DATE.sub(move, text)


def resplit_signals(ws):
    """The signals log is one file a month. Once the dates have moved, a row
    may belong to another month, so the rows are dealt out again."""
    folder = ws / "signals"
    head, months, month = None, {}, None
    for f in sorted(folder.glob("*.md")):
        lines = f.read_text(encoding="utf-8").splitlines()
        cut = next(i for i, line in enumerate(lines) if line.startswith("|---")) + 1
        head = head or lines[1:cut]
        for row in lines[cut:]:
            m = DATE.search(row.split("|")[1]) if row.startswith("|") else None
            month = m.group(0)[:7] if m else month
            if month and row.strip():
                months.setdefault(month, []).append(row)
        f.unlink()
    for month, rows in months.items():
        (folder / f"{month}.md").write_text("\n".join([f"# Signals log: {month}"] + head + rows) + "\n",
                                            encoding="utf-8")
    counts = ws / ".state" / "signal-counts.json"      # a cache keyed by month. The script counts again
    if counts.exists():
        counts.unlink()


def pipeline(ws, today, *args):
    env = dict(os.environ, JOB_SEARCH_TODAY=today)
    env.pop("JOB_SEARCH_HOME", None)
    done = subprocess.run([sys.executable, str(PIPELINE), "--home", str(ws), *args],
                          capture_output=True, text=True, env=env)
    if done.returncode != 0:
        sys.exit(f"pipeline {' '.join(args)} failed:\n{done.stdout}{done.stderr}")
    return done.stdout


def build(out, today, place):
    days = (datetime.date.fromisoformat(today) - datetime.date.fromisoformat(SAMPLE_DAY)).days
    if out.exists():
        if not (out / OURS).exists():
            sys.exit(f"{out} exists and this script did not write it. Choose another --out, or remove it yourself")
        shutil.rmtree(out)
    with tempfile.TemporaryDirectory(prefix="foothold-test-search-") as tmp:
        ws = Path(tmp) / "job-search"
        shutil.copytree(SAMPLE, ws)
        for empty in ("inbox", "reviews", "signals", "profile/cv", "profile/projects"):
            (ws / empty).mkdir(parents=True, exist_ok=True)      # git does not keep empty folders
        for f in sorted(p for p in ws.rglob("*") if p.is_file() and p.suffix.lower() in TEXT):
            text = shift_dates(f.read_text(encoding="utf-8"), days)
            f.write_text(text.replace(SAMPLE_PLACE, place), encoding="utf-8")
        resplit_signals(ws)
        pipeline(ws, today, "pipeline")
        pipeline(ws, today, "dashboard")
        check = pipeline(ws, today, "check")
        pipeline(ws, today, "save")
        out.mkdir(parents=True)
        (out / OURS).write_text("Written by scripts/test-search.py. Safe to delete.\n", encoding="utf-8")
        saves = sorted((ws / ".save").glob("*.txt"))
        for f in saves:
            shutil.copy2(f, out / f.name)
        with zipfile.ZipFile(out / "test-search.zip", "w", zipfile.ZIP_DEFLATED) as z:
            for f in saves:
                z.write(f, f.name)
        shutil.copy2(ws / "profile" / "cv" / "cv-master.md", out / "sam-example-cv.txt")
        (out / "PROMPT.txt").write_text(PROMPT, encoding="utf-8")
    return [f.name for f in saves], check.strip().splitlines()[-1]


def main():
    ap = argparse.ArgumentParser(description="Build a ready-made saved search for testing in the Claude app.")
    ap.add_argument("--out", default=str(REPO / "dist" / "test-search"))
    ap.add_argument("--today", default=datetime.date.today().isoformat(), help="YYYY-MM-DD. Default: today")
    ap.add_argument("--place", default=SAMPLE_PLACE, help="where Sam lives. Default: an invented town")
    args = ap.parse_args()
    out = Path(args.out).resolve()
    saves, result = build(out, args.today, args.place)
    print(f"Built a test search for {args.today}, set in {args.place}: {len(saves)} save files. Checks: {result}")
    print(f"  {out}")
    print("  test-search.zip      attach this to a chat in the test project (or attach the .txt save files)")
    print("  PROMPT.txt           paste this as the message")
    print("  sam-example-cv.txt   the invented CV, if you want one in the project")
    return 0


if __name__ == "__main__":
    sys.exit(main())
