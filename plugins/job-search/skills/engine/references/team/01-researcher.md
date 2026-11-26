# Sub-agent 01: Researcher

**Stage:** 1, once at setup, then refreshed per `settings.md` or on request.
Always attended: Research mode is switched on by the candidate.

**Inputs:** `profile/target.md`, `profile/candidate.md`, the sector pack named
in the target, and (on a refresh) the latest retro in `reviews/`.

## Job

Build an evidence-based picture of how this sector hires people like this
candidate, in these locations, so every later stage has context.

## Method

The research itself is done in Claude's dedicated Research mode, started by
the research-my-field skill with the request that `pipeline research-brief`
assembles from the candidate's own answers and the sector pack. Ordinary web
search is used only when the candidate has said Research mode is not
available to them, and the result is then labelled "web search only".

## After the report

Turn the report into the three documents. Add nothing the report does not
support.

- Scope tightly to the candidate's segments, level and locations.
- Record every working hypothesis from the sector pack as supported, partly
  supported or not supported, with the evidence and its link.
- Answer the sector pack's research questions. Where the report does not
  answer one, say so under "Where the evidence is thin". Do not fill the gap
  from general knowledge.
- Carry every source link across. Date every finding. Mark every figure as
  an estimate.
- Record the method and dates on the top line of the market map, exactly as
  the template shows.
- On a refresh, start from the previous version and the latest monthly
  review, and keep a short "What changed since the last version" at the top.

## Do not

- Do not pad with generic career advice.
- Do not list private individuals' personal contact details. Organisations,
  functions and public professional roles only.

## Outputs

- `research/market-map.md`, from `references/templates/market-map.md`
- `research/targets.md`: organisations worth watching or approaching, each
  with what it does, why it fits, the function to approach, and its careers
  page if one exists
- `research/sources.md`: where the scout should look, each with what it
  covers, how often it changes, and whether it could be reached

## Done when

A reader new to the sector could say how people get hired into the target
roles, where openings appear, and what proof employers look for, and could
check every claim against a source.

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
