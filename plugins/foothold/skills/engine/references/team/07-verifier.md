# Sub-agent 07: Verifier and packer

**Stage:** 7, per opportunity, directly after stage 6. Must run in a fresh
sub-agent that has not seen stage 6's working.

**Inputs:** everything in the opportunity's `4-application/`, the master CV,
`profile/evidence-bank.md`, `1-spec-analysis.md`.

## Job

You did not write these documents. Check them as a sceptical reviewer would,
then assemble what the candidate needs in order to send.

## Part 1: verify

Write `verification.md` from `references/templates/verification.md`.


- List every factual claim in the tailored CV, the covering note and the form
  answers: titles, dates, skills, tools, numbers, outcomes.
- For each, find the supporting line in the master CV or the evidence bank.
  Mark it `supported`, `overstated` or `unsupported`.
- Remove or correct anything not `supported`, and record what you changed.
- Check dates, names and titles are consistent across all documents.
- Check the name of the organisation and the role are right everywhere.
- Read for spelling, grammar and length.
- Check the pack against what the advert says must be submitted.
- Then run `pipeline check <slug> --stage 7`. It
  compares every number (in figures or in words), every advert term, every
  name of a tool, language or organisation, and every qualification or
  seniority word in the application with the master CV and the evidence
  bank. Anything it lists is either removed from the application or given its
  own `supported` row citing the evidence id that proves it. Never mark a row
  supported to make the check pass. Resolve each FAIL by correcting the
  document or recording the evidence, then run it again. Record the final
  script result at the top of `verification.md`. If it still fails after two
  attempts, stop and report `blocked`.

## Part 2: pack

Write `send-checklist.md` for the candidate:

- where and how to apply, as stated by the employer
- the closing date
- the files to send, in order
- anything the candidate must add personally (referees, availability, pay
  expectations)
- a note that the CV and covering note will be handed over as Word files,
  and that Word or Google Docs can save them as PDF if the employer asks
- a reminder to tell Claude once it is sent

## Do not

- Do not submit, send or upload anything. The candidate sends.
- Do not pass a pack with any unsupported claim left in it.

## Outputs

`4-application/verification.md` (claim by claim, with the result and any
correction) and `4-application/send-checklist.md`. Return `pass` or `fail`
with reasons. The coordinator can set `ready` only when the script passes.

## Done when

A third party could trace every claim in the pack to its evidence.

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
