---
name: research-my-field
description: >
  This skill should be used to run or refresh the in-depth research into how a
  candidate's field hires, tailored to their career type, level, experience,
  location and goals. Triggers include "research my field", "research my
  sector", "refresh the research", "update the research", "redo the research",
  "the research is out of date", or the research step at the end of
  start-my-search.
metadata:
  version: "0.10.0"
---

# Research my field

Run the in-depth research in Claude's dedicated Research mode, then turn the
report into the three documents the rest of the search depends on. This is
always done with the candidate present. It never runs from a scheduled task.

1. Load the `engine` skill from this plugin and read it in full.
2. Open the workspace. Restore `research.txt` if there is one.

## Step 1: is the interview done?

Run `pipeline research-brief`. If it is refused, the interview is unfinished:
say which answers are missing and collect them, one question at a time. The
research is only as specific as the answers behind it.

If the candidate's field has no sector pack yet, draft one from
`references/sectors/_blank.md`, save it in the workspace as
`sectors/<name>.md`, show the candidate its working hypotheses in plain words,
and ask whether any look wrong before going further.

## Step 2: is Research mode on?

Dedicated Research mode is required. Check whether this conversation has a
research tool: one that runs a long, multi-source investigation and returns a
cited report.

If it does not, stop and say this, then wait:

> This needs Claude's Research mode, which looks much further than an ordinary
> search. Press the plus button under the message box and choose Research. A
> blue marker appears. Then say "Research my field" again.

Web search must also be on for Research to work. Do not start an ordinary web
search in its place.

Only if the candidate says Research is not available to them, offer the
lighter route once: an ordinary web search pass, clearly labelled. If they
accept, follow `references/team/01-researcher.md` by ordinary search and
record the method as "web search only".

## Step 3: run it

Give the research tool the request printed by `pipeline research-brief`, word
for word. It is saved at `research/brief.txt`. Do not shorten or reword it:
it was assembled from the candidate's own answers and the sector pack.

Tell the candidate it will take a while and needs nothing from them.

## Step 4: turn the report into the three documents

Follow `references/team/01-researcher.md` from "After the report". Write only
what the report supports, with its sources:

- `research/market-map.md`, from `references/templates/market-map.md`. The
  top line records today's date, the method, and a refresh date taken from
  the research refresh interval in `settings.md`.
- `research/targets.md`: organisations worth watching or approaching.
- `research/sources.md`: where the scout should look.

On a refresh, keep a short "What changed since the last version" at the top.

## Step 5: check, explain, close

1. Run `pipeline check --research` and fix what it reports.
2. Give the candidate the short version in plain words: how people really get
   hired into what they want, which of the working assumptions held up, and
   what that changes about their search. Ask whether anything looks wrong to
   them. They know things the research does not.
3. Tell them to switch Research off again by pressing the blue marker, so
   everyday questions get quick answers.
4. Close the workspace, naming what happened: "the research was done" or
   "the research was refreshed".

## When a refresh is due

The script warns when the refresh date has passed, and the daily check puts
it in the candidate's list. A monthly review may also ask for one early. A
refresh always needs the candidate, because Research mode is switched on by
them.
