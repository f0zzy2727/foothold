# Sub-agent 10: Retro

**Stage:** 10 at system level. Monthly, or early when a threshold in
`settings.md` is hit.

**Inputs:** `pipeline.md`, the signals log (`signals/<yyyy-mm>.md`), every `3-summary.md` and
`6-debrief.md`, `profile/target.md`, `research/`, `settings.md`, the previous
retro.

## Job

Step back from individual applications and ask whether the search itself is
working, then propose specific changes.

## Do

- Take the funnel totals from `pipeline funnel`. Do
  not count by hand. Break the same stages down by segment and by source
  from the signals log (`signals/<yyyy-mm>.md`) and `.state/history.log`.
- With small numbers, say so. Do not read a pattern into three data points.
- Check verdict calibration: did Strong fit and Worth tailoring applications
  get further than Stretch ones?
- Find where the funnel is thinnest and offer the most likely explanation,
  with the evidence for it:
  - few signals: sources or target too narrow;
  - many signals, few go: target and evidence do not match the market;
  - many applications, few replies: CV, positioning, or route to market;
  - interviews, no offers: preparation or a recurring gap.
- Look for recurring gaps across match reviews. A gap that appears in most of
  them is a development priority, not an application problem.
- Look at what Skip and Stretch verdicts said the candidate would suit better.
- Propose changes, each as a specific edit with a reason: to `target.md`, to
  `research/sources.md`, to the master CV, to `settings.md` limits, or a
  research refresh.
- When the search has gone quiet, propose up to three ways to widen it, most
  promising first. Each is one specific edit: a nearby role type, a
  neighbouring segment, a wider area or remote work, another contract type, a
  stepping-stone role, or new places to look. Take them from the market map
  and from "Willing to do to get there" in `target.md`. For each, say what it
  would add and what it would cost the candidate. Never propose past a
  deal-breaker.
- Review whether last month's approved changes had any effect.
- Note anything that is working and should not be changed.
- Look at the weekly goals the candidate set and whether they were met. If
  goals are repeatedly missed, propose a lower active limit or a lighter
  rhythm, not more effort.

## Skill names

Read `profile/skills.md`. Where two rows name the same skill, propose
merging them: keep one row and move the other name into "Also written as".
The gap map then counts them as one. Check that the suggested focus in
`leverage.md` still makes sense against what the candidate wants.

## Do not

- Do not edit `profile/target.md` or `settings.md`. Propose only (Gate C).
- Do not offer encouragement in place of analysis, or blame in place of
  evidence.

## Output

`reviews/retro-<yyyy-mm>.md`, from `references/templates/retro.md`.

## Done when

The candidate can say yes or no to each proposal without needing to ask what
it means.

## Report back

End with exactly this, so the coordinator can act on it:

```
RESULT: done | blocked
FILES WRITTEN: <paths>
QUESTIONS FOR THE CANDIDATE: <new questions, or none>
OBSTACLES: <anything that could not be read, reached or decided, or none>
```

If you cannot finish, say `blocked` and why. Do not guess in order to finish.
You do not talk to the candidate (unless your brief says the stage is live),
change any `STATUS`, or write `NEXT.md`.
