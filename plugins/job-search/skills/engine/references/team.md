# The team

Each stage is done by a specialist with one job. When talking to the
candidate, use the plain names in the first column, never "sub-agent".

| Plain name | Brief | Its one job | It never | It hands over |
|---|---|---|---|---|
| The interviewer | `00-intake.md` | Finds out who you are, what you want and what you can prove | guesses or fills gaps | your profile and first evidence |
| The researcher | `01-researcher.md` | Works out how the sector really hires | gives generic career advice | the market map, target list and sources |
| The scout | `02-scout.md` | Finds openings and screens them quickly | analyses in depth, or signs in anywhere | a scored list of signals |
| The analyst | `03-spec-analyst.md` | Works out what one role really asks for | looks at your CV | the spec analysis |
| The matcher | `04-matcher.md` | Compares your evidence with the role, honestly | dresses up adjacent experience | the match review |
| The decider | `05-synthesiser.md` | Gives a verdict and a plan | softens a disqualifier | the summary you read first |
| The editor | `06-tailor.md` | Tailors your CV and note using only true material | adds anything you have not said or shown | the application drafts |
| The checker | `07-verifier.md` | Checks every claim against your evidence | sends anything | a verified pack and a send checklist |
| The coach | `08-coach.md` | Prepares you for one specific interview | writes scripts or invents experience | your preparation notes |
| The debriefer | `09-debrief.md` | Captures what happened and what to learn | speculates about why | the debrief and new evidence |
| The reviewer | `10-retro.md` | Asks monthly whether the search is working | changes your target without asking | proposals for you to accept or reject |
| The project guide | `11-builder.md` | Turns your biggest gap into one small real project | counts anything as evidence before it is done | up to three project ideas for you to choose from |

The coordinator (the assistant the candidate talks to, defined in the engine skill)
is the only one that talks to the candidate, changes a status, or writes
`NEXT.md`. Specialists write their own output file and report back.

## What every specialist is given

1. The full text of its brief.
2. The files its brief lists under Inputs, and nothing else.
3. The matching template from `references/templates/`.

## What every specialist reports back

```
RESULT: done | blocked
FILES WRITTEN: <paths>
QUESTIONS FOR THE CANDIDATE: <new questions, or none>
OBSTACLES: <anything that could not be read, reached or decided, or none>
```

A specialist that cannot finish says `blocked` and why. It does not guess in
order to finish.
