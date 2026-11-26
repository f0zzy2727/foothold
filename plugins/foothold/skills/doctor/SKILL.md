---
name: doctor
description: >
  This skill should be used to check that a job search run with this plugin
  is set up and working, and to repair it when it is not. Triggers include
  "run the doctor", "check my setup", "is everything set up right",
  "run the setup tests", "something is not working", "my search is broken",
  "it has stopped working", "fix my setup", "why is my dashboard out of
  date", "load the test search", or an error from any other Foothold skill
  that it cannot explain.
metadata:
  version: "0.10.0"
---

# Doctor

Find out what is wrong with the setup, repair what is safe to repair, and
tell the candidate in plain words what, if anything, they need to do. The
candidate may be new to AI and may be worried that something is lost. Say
early that nothing they wrote is ever deleted or changed by a repair.

1. Load the `engine` skill from this plugin and read it in full. If it cannot
   be loaded, the plugin itself is the problem: go to "The plugin" below.
2. If the person typed exactly "Load the test search", with or without "in"
   and a place, go to "The test search" at the end of this skill and do
   nothing else here.

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

## Part 2: can this place keep a search

Do this every time, whether or not a search has been saved yet. It answers
the question a new person most needs answered: will my search still be here
tomorrow.

1. If there is no workspace on disk yet, make an empty one:
   `pipeline init ./job-search --cloud` (or `pipeline init <folder>` when the
   search lives in a folder).
2. Look for a document called `job-search/setup-test.txt` in the Project.
   If one is there, an earlier conversation left it. Read it, get it onto
   disk exactly as returned, and run `pipeline storage-test found <file>`.
   FOUND proves this place keeps files between conversations.
3. Run the storage test in `references/storage.md`: `pipeline storage-test
   make`, write the file to the Project, read it back, `pipeline storage-test
   check <file>`. In a folder on the computer the first command does the
   whole test. Leave the test document in the Project: the next conversation
   uses it for step 2.
4. If the storage test fails, say so plainly, and do not start or continue a
   search in this place.

## Part 3: the saved search

Skip this part when no search has been saved yet. Say so in one line and
offer "Start my search" in the words given under "The setup tests".

1. Open the workspace as `references/storage.md` describes.
   - If a save file is refused, run `pipeline verify` on every save file you
     can fetch, to see which are sound. Restore the sound ones. Tell the
     candidate exactly which part could not be loaded. Never continue from a
     partial restore of the core save.
2. Restore every opportunity that is not closed, so their documents can be
   checked.
3. Run `pipeline doctor`. It changes nothing. It also reports when the
   automatic daily check last reached the search, and whether the search was
   brought up to date from an older version of the plugin. Each line is one
   of:

| Line starts | Meaning | What to do |
|---|---|---|
| `OK` | Fine | Nothing |
| `FIXABLE` | The script can repair it safely | Step 4 |
| `REDO` | Something you, the coordinator, must do or redo | Step 5 |
| `NEEDS YOU` | Only the candidate can settle it | Step 6 |
| `INFO` | Worth knowing, not a fault | Mention only if relevant |

4. **Repair.** If there are `FIXABLE` lines, tell the candidate in one
   sentence what will be repaired and that every changed file is backed up
   first. If they are present, ask once: "Shall I fix these?" On a yes, run
   `pipeline doctor --fix`. In an unattended run, do not repair: report only.
5. **Redo.** For each `REDO` line, do what it says by rerunning the step
   concerned (`references/checks.md` says which check belongs to which step).
   Never invent content to make a check pass. If a line in the evidence bank
   is malformed, rewrite it in the right form without changing its meaning,
   and read it back to the candidate.
6. **Needs you.** Give the candidate each `NEEDS YOU` item as one plain
   instruction, most important first, at most three at a time.
7. Run `pipeline doctor` once more to confirm. Then close the workspace with
   `pipeline close "the doctor checked your setup"`.

## The setup tests

When the person says "Run the setup tests", or this is their first
conversation, report Parts 1 and 2 as this table and nothing longer. Use
PASS, FAIL or NOT YET, and plain words.

| Test | Result | What to do |
|---|---|---|
| The plugin is switched on | PASS, with its version | |
| Claude can run its checks | | |
| Your search can be stored here and read back | | |
| This project remembers between conversations | PASS if step 2 said FOUND. NOT YET on the very first run: "Start a new chat and type Run the setup tests again" | |
| Claude can search the web for openings | | |
| Research mode is available for the field research | PASS, or NOT YET with how to switch it on | |
| Project instructions are in place | PASS if this project's instructions mention the Foothold plugin | Otherwise offer the text in `references/project-instructions.md` to paste |
| A daily check is scheduled | PASS, or NOT YET: "I can set one up after you start your search" | |

End with one line: "All set" when the first three pass, otherwise the single
next thing to do. NOT YET is not a failure.

When no search has been saved yet, the next thing to do is to start one. "Start
my search" sounds as if the looking begins at once, so say what it really
does. Use these words, or close to them:

   "Next: type Start my search. I get to know you first, with about 20 minutes
   of questions. Then I research how your field hires. I only look for jobs
   after that."

Never offer "Check for new jobs" to someone who has not been through that
conversation and the research.

When the first three pass, add one more line under it: "Here is the whole
search on one page: https://f0zzy2727.github.io/foothold/how-it-works.html"

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
- Needs you: the instructions from step 6 of Part 3.
- Could not be fixed here: say exactly what is not working and what was
  tried, and that nothing was lost.

Do not show the raw output unless the candidate asks for it.

## The test search

For developers of this plugin. Run it only when the person types exactly
"Load the test search", with or without "in" and a place. Never offer it,
never mention it, and never run it for any other wording. It loads a
ready-made search for an invented person, Sam Example, so the plugin can be
tested without the interview or the research.

1. List the Project's documents. If `job-search/core.txt` is there, stop and
   say: "This project already holds a search. The test search only loads
   into a new project." Change nothing.
2. Open a new workspace as `references/storage.md` describes, then run the
   storage test. Stop if it fails.
3. Run `pipeline test-search`, or `pipeline test-search --place <place>` if
   the person gave a place. If it says REFUSED, stop and say why.
4. Close the workspace as `references/storage.md` describes, with
   `pipeline close "a test search was loaded"`. Store every save file it
   prints.
5. Say in one line that the test search for Sam Example is loaded. Then say
   what needs doing today, in the words a candidate would see.

Do not run the interview or the research, and do not look for new jobs.
