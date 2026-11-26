# Working on Foothold

Instructions for a coding agent (Claude Code, Codex or similar) working in
this repository. People should read README.md and SETUP.md instead.

## What this is

A Claude plugin, `foothold`, that runs an honest job search for one person.
The repository is also the marketplace that serves it. The people who use it
are new to AI. Everything they see must be plain.

## Layout

- `plugins/foothold/`: the plugin. Skills are in `skills/<name>/SKILL.md`.
  The `engine` skill holds the method, the specialist briefs
  (`references/team/`), the templates, the starter workspace
  (`references/seed/`) and one script, `scripts/pipeline.py`.
- `SETUP.md`: the one page a new person follows. Its instructions block must
  stay identical to `plugins/foothold/skills/engine/references/project-instructions.md`.
  A test enforces this.
- `docs/how-it-works.html`: the page that explains the search to a new
  person. It shares its look with the dashboard template
  (`references/dashboard-template.html`). Neither page may load anything from
  another site. A test enforces this. GitHub Pages serves the `docs` folder,
  so a push to `main` updates the page at
  https://f0zzy2727.github.io/foothold/how-it-works.html
- `FACTS.md`: what has been learned about how the plugin behaves in the
  Claude app. Read it before changing storage, folders or setup.
- `tests/`: the test suite and an invented sample search.
- `MIGRATIONS.md`: the rule for changing any file in a person's saved search.

## Commands

```
python3 -m unittest discover -s tests -v     # run before and after every change
scripts/package.sh                           # tests, then dist/foothold.plugin
claude plugin validate .                     # if the claude CLI is present
```

## Rules

1. The tests must pass before a commit. If a check fails three times for the
   same reason, stop and report. Do not loop.
2. `pipeline.py` uses the Python standard library only.
3. Never weaken the three promises: the plugin never contacts anyone for the
   person, never writes anything about them that they did not say, and tells
   them when a role is not worth their time.
4. A change to any file format in a saved search follows `MIGRATIONS.md`:
   raise the format number, add a migration step, add a test. Old searches
   must keep working.
5. To release: change the version in `plugins/foothold/.claude-plugin/plugin.json`
   and in every `SKILL.md` (a test checks they agree), add a `CHANGELOG.md`
   entry, run the tests, commit, then tag `vX.Y.Z` and push the tag.
6. Git does not keep empty folders. Never rely on one existing. The script
   and the tests create the folders they need.
7. Use only invented people and organisations in tests and examples. Never
   commit a real CV or a real saved search.

## Writing style

- European English spelling.
- No dashes of any kind in prose: no em dash, no en dash, no spaced hyphen.
  Use a full stop, a comma or a colon.
- Short sentences. Plain words. No hype.
- Skill files are instructions to Claude, written as directives.
- Text a candidate will read assumes they have never used an AI tool.

## What cannot be tested here

Whether Claude follows the skills as written, the quality of a verdict, a
real Research mode run, and whether a scheduled task reaches a Project. Those
need a real run in the Claude app. Say so when a change depends on them.
