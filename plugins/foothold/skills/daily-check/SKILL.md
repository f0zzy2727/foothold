---
name: daily-check
description: >
  This skill should be used to run the regular check of an existing job
  search: look for new openings, analyse them, prepare applications that are
  due, and update what needs the candidate. Triggers include "run the
  foothold daily-check", "check for new jobs", "run my daily check", "any
  new openings", "I have added some jobs", "I found a job", a job advert
  pasted or uploaded with nothing else said when a search already exists, or
  a scheduled task that names this skill.
metadata:
  version: "0.10.0"
---

# Daily check

1. Load the `engine` skill from this plugin and read it in full.
2. Follow "Daily" in the engine's modes.

Points specific to this skill:

- This usually runs unattended. Do not ask questions and wait. Take the most
  reasonable reading, record what was assumed in the run log, and queue any
  question for the candidate.
- If the saved search cannot be reached, change nothing. Report that in one
  sentence and stop. Never start a new search from here.
- When a schedule started this run (the request says "scheduled", or nobody
  is in the conversation), close with `pipeline close --scheduled "the daily
  check"`. That is how the candidate can see the automatic check is working.
- If `pipeline guard` refuses at close, another session saved first. Write
  nothing, report it in one sentence and stop. The next run picks it up.
- Adverts the candidate added themselves are analysed first and never
  filtered out.
- Sonnet is enough for this check. It does not need a larger model.
- Never mark anything ready unless the script allowed it.
- If the saved search will not load, or `pipeline check` fails in a way the
  run cannot put right, run `pipeline doctor` (report only, never `--fix`
  unattended) and add a note asking the candidate to say "Run the doctor".
- Never widen the search from here. When checks keep finding nothing, the
  script puts "Review your search with Claude" in the candidate's list. Say
  so in the closing lines and change nothing in the target or the sources.
- Never run or refresh the research from here. If the script warns that a
  refresh is due, put it in the candidate's list.
- End with at most five plain lines: what was found, what moved, and what
  needs the candidate. If nothing changed, say so in one line.
