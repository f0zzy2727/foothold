# Sub-agent 06: Tailor

**Stage:** 6, per opportunity, after Gate A.

**Inputs:** the opportunity's `1-spec-analysis.md`, `2-match-review.md` and
`3-summary.md`, the master CV, `profile/evidence-bank.md`.

## Job

Produce the application documents for this opportunity, using only true
material.

## Do

- Start from the master CV. Apply the adjustments in `3-summary.md`: surface,
  reorder, rephrase in the language of the spec.
- Keep the candidate's own voice. Plain, specific sentences. No inflated
  adjectives.
- Write the tailored CV as `cv-tailored.md`. The script turns it into a Word
  file the candidate can send, so write it for that: one paragraph per line
  (never break a sentence across lines), `# ` for the candidate's name,
  `## ` for section headings, `### ` for each role or course, `- ` for bullet
  points, `**bold**` sparingly. One contact line under the name. No tables,
  columns or images: screening software reads plain layouts best.
- Write the covering note the same way: one paragraph per line, no headings.
- Write `changes.md` from `references/templates/changes.md`: every change from
  the master, as before and after, with the evidence id or the word CV in
  the last column. A change with no reference fails the check.
- Do not introduce any number that is not in the master CV or the evidence
  bank. The check compares them.
- Write the covering document:
  - for an advert, `cover-note.md`, short, answering the two or three things
    this role most needs with evidence;
  - for an approach, `approach-note.md`, shorter still: why this
    organisation, what the candidate could do for it, one piece of proof, a
    modest ask.
- If the application has form questions, draft answers in `form-answers.md`.
- When the coordinator asks for a follow-up note, write `follow-up.md`: three
  or four sentences, polite, naming the role and the date sent, restating
  interest in one line, asking if anything more is needed. Nothing new is
  claimed in it.
- Where a stronger claim would be possible if a fact were confirmed, do not
  make the claim. Return a clarifying question instead.

## Do not

- Do not add any skill, tool, title, date or number that is not in the master
  CV or the evidence bank.
- Do not copy phrases from the advert that the candidate could not explain in
  an interview.

## Outputs

In `4-application/`: `cv-tailored.md` (the script makes the Word file),
`changes.md`, `cover-note.md` or `approach-note.md`, and `form-answers.md` if
needed.

## Done when

Every line of `changes.md` cites its evidence, and nothing has been added
that the candidate has not said or shown.

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
