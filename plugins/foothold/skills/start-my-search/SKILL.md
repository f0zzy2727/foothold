---
name: start-my-search
description: >
  This skill should be used when the user wants to set up a full, ongoing job
  search. Triggers include "start my search", "get to know me", "set up my job
  search", "help me find a job in" a sector, "run my whole job search", "help
  my son or daughter get a job", or accepting the offer made at the end of
  try-one-job.
metadata:
  version: "0.9.1"
---

# Start my search

Set up an ongoing job search for one candidate. Takes about 45 minutes, of
which the candidate is needed for about 20.

1. Load the `engine` skill from this plugin and read it in full. If it cannot
   be loaded, say the plugin is not fully installed and stop.
2. Follow "Setup" in the engine's modes.

Points specific to this skill:

- Opus is the recommended model for setup. If this conversation is on a
  smaller model, say so once before starting: "Setup works best on Claude
  Opus. You can switch with the model picker, or carry on as we are." Then do
  what the candidate prefers.
- Run the storage test before the interview, not after. If it fails, stop.
- If this project has no instructions that mention the Foothold plugin,
  offer the text in the engine's `references/project-instructions.md` for
  the person to paste into the project's instructions. It makes every later
  conversation start the right way. Carry on whether or not they add it.
- If the person setting this up is not the candidate (a parent, a friend),
  say so kindly before intake: the search works only if the candidate owns
  it. Ask for the candidate to do the interview, and offer the other person
  the supporter role.
- Before intake, tell the candidate the three promises in the engine's
  `references/how-it-works.md`.
- If there is nowhere to keep the search between conversations, explain the
  two options in the engine's `references/storage.md`, section C, before
  starting. Do not run a 45 minute setup that will be lost.
- The sector pack shipped with the plugin is `music-industry`. For any other
  career, have the researcher draft a pack first from
  `references/sectors/_blank.md`, and show the candidate its hypotheses before
  researching.
- The research step uses Claude's dedicated Research mode. After the
  interview, tell the candidate in plain words to press the plus button under
  the message box, choose Research, and say "Research my field". Do not run
  an ordinary web search in its place.
- Finish by showing the candidate their `NEXT.md` in plain words and asking
  the first question from the queue.
