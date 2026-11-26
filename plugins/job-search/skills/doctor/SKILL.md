---
name: doctor
description: >
  This skill should be used to check that a job search run with this plugin
  is set up and working, and to repair it when it is not. Triggers include
  "run the doctor", "check my setup", "is everything set up right",
  "something is not working", "my search is broken", "it has stopped
  working", "fix my setup", "why is my dashboard out of date", or an error
  from any other job-search skill that it cannot explain.
metadata:
  version: "0.7.0"
---

# Doctor

Find out what is wrong with the setup, repair what is safe to repair, and
tell the candidate in plain words what, if anything, they need to do. The
candidate may be new to AI and may be worried that something is lost. Say
early that nothing they wrote is ever deleted or changed by a repair.

1. Load the `engine` skill from this plugin and read it in full. If it cannot
   be loaded, the plugin itself is the problem: go to "The plugin" below.

## Part 1: what this conversation can do

Check these yourself. They are about the conversation, not the files, so the
script cannot see them.

| Check | How | If it fails, say |
|---|---|---|
| The plugin | The engine skill loads and its `scripts/pipeline.py` exists | "The job search plugin is not fully added. In Claude, go to Customize, then Plugins, remove it and upload the file again." |
| Running the script | Run `pipeline selftest` | "This conversation cannot run the checks. Open your job search project in the Claude app and ask again there." Then do Part 2 by hand from `references/checks.md` and say the result is unverified |
| A home for the search | A Project with readable documents, or a connected folder holding the search | "Your search has nowhere to be kept. Create a project called 'My job search' and talk to me there." |
| Looking things up | A web search tool is present | "Web search is off, so I cannot look for openings. Switch it on from the plus button." |
| Research mode | A research tool is present | Not a fault. Say it is only needed for researching the field, and how to switch it on when asked |
| The schedule | If a tool can list scheduled tasks, look for the daily check and the weekly review | "No daily check is scheduled. I can set one up, or you can say 'Check for new jobs' whenever you like." |
| Publishing pages | A tool that publishes a web page is present | Not a fault. Say the dashboard will be given as a file instead of a link |
| The model | You know which model you are | Not a fault. If it is smaller than Opus, say once that setup and applications work best on Opus and the daily check is fine on Sonnet |

## Part 2: the saved search

1. Open the workspace as `references/storage.md` describes.
   - If a save file is refused, run `pipeline verify` on every save file you
     can fetch, to see which are sound. Restore the sound ones. Tell the
     candidate exactly which part could not be loaded. Never continue from a
     partial restore of the core save.
   - If there is no saved search at all, say so, and offer "Start my search".
     Stop here.
2. Restore every opportunity that is not closed, so their documents can be
   checked.
3. Run the storage test in `references/storage.md`: `pipeline storage-test
   make`, write the test file to the Project, read it back, `pipeline
   storage-test check <file>`. This proves, with a file the size of a real
   search, that this place can keep the search and give it back intact. In a
   folder on the computer the first command does the whole test.
4. Run `pipeline doctor`. It changes nothing. It also reports when the
   automatic daily check last reached the search, and whether the search was
   brought up to date from an older version of the plugin. Each line is one
   of:

| Line starts | Meaning | What to do |
|---|---|---|
| `OK` | Fine | Nothing |
| `FIXABLE` | The script can repair it safely | Step 5 |
| `REDO` | Something you, the coordinator, must do or redo | Step 6 |
| `NEEDS YOU` | Only the candidate can settle it | Step 7 |
| `INFO` | Worth knowing, not a fault | Mention only if relevant |

5. **Repair.** If there are `FIXABLE` lines, tell the candidate in one
   sentence what will be repaired and that every changed file is backed up
   first. If they are present, ask once: "Shall I fix these?" On a yes, run
   `pipeline doctor --fix`. In an unattended run, do not repair: report only.
6. **Redo.** For each `REDO` line, do what it says by rerunning the step
   concerned (`references/checks.md` says which check belongs to which step).
   Never invent content to make a check pass. If a line in the evidence bank
   is malformed, rewrite it in the right form without changing its meaning,
   and read it back to the candidate.
7. **Needs you.** Give the candidate each `NEEDS YOU` item as one plain
   instruction, most important first, at most three at a time.
8. Run `pipeline doctor` once more to confirm. Then close the workspace with
   `pipeline close "the doctor checked your setup"`.

## What a repair will and will not do

A repair may: recreate a missing folder or blank starter file, restore a
missing setting to its default, reset a damaged cache, set aside unreadable
log lines, restore a lost status from the history, remove an opening logged
twice, and rebuild the tracker, the to-do list and the dashboard.

A repair will never: delete anything, change the profile, the evidence bank,
the CV or any application document, or change what the candidate is looking
for.

## How to report

Lead with the answer, using the same signals as the dashboard.

- Everything fine: "Your setup is working. Nothing needs you."
- Repaired: say how many things were repaired and name the one or two that
  matter in plain words. Leave out caches and logs unless asked.
- Needs you: the instructions from step 7.
- Could not be fixed here: say exactly what is not working and what was
  tried, and that nothing was lost.

Do not show the raw output unless the candidate asks for it.
