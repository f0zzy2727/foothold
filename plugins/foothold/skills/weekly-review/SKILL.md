---
name: weekly-review
description: >
  This skill should be used to review progress on an existing job search.
  Triggers include "run the foothold weekly-review", "weekly review", "how
  is my search going", "review my week", "monthly review", "review my
  search", "nothing is coming up", "widen my search", "is my search working",
  "what should change", or a scheduled task that names this skill.
metadata:
  version: "0.10.0"
---

# Weekly review

1. Load the `engine` skill from this plugin and read it in full.
2. Run `pipeline review`. It counts the early signs in `settings.md`. Do not
   count them yourself.
3. If the request says "monthly", "review my search", "nothing is coming up"
   or "widen my search", or the script prints a `REVIEW DUE` line, follow
   "Monthly" in the engine's modes. Give the candidate the script's reason in
   plain words first. Otherwise follow "Weekly".

Points specific to this skill:

- Take every count from `pipeline funnel`. Do not count by hand.
- With small numbers, say so. Do not read a pattern into three results.
- Ask the candidate to choose one or two goals for next week. Offer options
  if they are stuck, but the choice is theirs.
- Name real progress, however small. Do not manufacture any.
- Run `pipeline leverage` and give the top gap in one sentence with its
  numbers, and one skill the candidate already has that adverts keep asking
  for. If a project is in progress, ask how it is going, once, without
  pressure. If there is a suggested focus and no project, offer the
  `close-the-gap` skill.
- Look at `profile/contacts.md` with the candidate: who could help, and is
  there one person worth a message this week. Most roles in many fields are
  filled through people. The candidate makes the contact, never Claude.
- List the sources marked as not readable in `research/sources.md` and ask
  whether the candidate has looked at them this week.
- Roles the script closed as expired, no decision or no response this week
  are listed under what happened. Say so plainly; do not hide them.
- If goals are repeatedly missed, suggest a lighter rhythm, not more effort.
- If the monthly review finds the market map no longer matches what is
  happening, propose a research refresh. The candidate runs it by switching
  Research on and saying "Refresh the research".
- A monthly review ends with proposals the candidate can answer yes or no to.
  Change nothing until they answer. A wider search is one of those proposals:
  never widen the target, the area or the sources without a yes.
- When the candidate has answered every proposal, run `pipeline review done`.
  The early signs are then counted afresh from today. In a scheduled run with
  nobody to answer, do not run it: the review stays on the candidate's list.
