---
name: my-search
description: >
  This skill should be used for questions about, and updates to, an existing
  job search run with this plugin. Triggers include "what should I do today",
  "where is my search", "what's the state of my search", "I applied to" a
  role, "skip that one", "I want to go for that one", "why did you say skip",
  "add this job to my search", "I found a job", "I followed up", "I know
  someone at", "I've changed what I'm looking for", "pause my search", and "help" or "what can you do" in the context of a job search.
metadata:
  version: "0.9.1"
---

# My search

The everyday conversation with the candidate about their search.

1. Load the `engine` skill from this plugin and read it in full.
2. Open the workspace. If there is no saved search, say so, and offer
   try-one-job or start-my-search.
3. Answer what was asked. Do not start a run unless asked to.

| The candidate says | Do |
|---|---|
| "help", "what can you do" | Answer from `references/how-it-works.md`, five lines or fewer |
| "what should I do today" | Read out `NEXT.md` in plain words |
| "where is my search" | Summarise `pipeline.md`: what is waiting on them, what is waiting on the system |
| "show me my dashboard" | Give the link to their dashboard page if one exists; otherwise close the workspace so it is built, then publish it or hand over `dashboard.html` |
| "why skip", "why that verdict" | Restore that opportunity and explain from its summary and evidence |
| "I applied to X" | `pipeline set <slug> applied`. If it was not ready, use `--force` and say so |
| "skip X" | `pipeline set <slug> closed skip` |
| "go for X anyway" | `pipeline set <slug> go`. If the limit is full, say which are active and ask which to hold |
| "refresh the research", "research my field" | Hand over to the `research-my-field` skill from this plugin |
| "something is not working", "check my setup" | Hand over to the `doctor` skill from this plugin |
| "add this job", "I found a job", "I have added some jobs", an advert pasted or uploaded | Treat it as a signal the candidate chose: save it as `0-source.md`, queue it and analyse it now. Then `pipeline checked-sources` |
| "I followed up with X" | `pipeline followed-up <slug>` |
| "I checked the job boards" | `pipeline checked-sources` |
| "I know someone at", "I spoke to" | Add or update the row in `profile/contacts.md`. Agree a next step and a date if they want one. Never contact anyone |
| "give me my CV as a Word file" | `pipeline export <slug>` and send the files it names |
| "what is my biggest gap", "what should I work on", "I finished my project" | Hand over to the `close-the-gap` skill from this plugin |
| "what happened to that old role" | Look in `archive/index.md`; `pipeline unarchive <slug>` brings it back |
| a new fact about themselves | Add it to the evidence bank with the next id, and say which roles it might change |
| "I've changed what I'm looking for" | Talk it through, then update `profile/target.md` once they confirm the new target in their own words |
| "pause" | Set active opportunities `on-hold` only if asked. Suggest pausing the scheduled runs. No pressure to resume |

Points specific to this skill:

- A new fact changes verdicts. A wish does not. Say so kindly when needed.
- If the candidate sounds worn down by the search, say so plainly and
  kindly, suggest talking to someone they trust, and do not push tasks.
- If anything changed, however small, close the workspace before the final
  reply, naming what happened. That is what keeps the dashboard current.
