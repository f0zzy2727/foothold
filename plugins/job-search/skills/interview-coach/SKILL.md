---
name: interview-coach
description: >
  This skill should be used when the user has an interview or meeting for a
  job in their search, or has just had one. Triggers include "I've got an
  interview", "prepare me for the interview", "help me prepare", "give me a
  practice interview", "mock interview", "debrief", "I had the interview
  today", "they turned me down", or "I got an offer".
metadata:
  version: "0.7.1"
---

# Interview coach

1. Load the `engine` skill from this plugin and read it in full.
2. Open the workspace and restore the opportunity concerned.
3. Work out which of three things is wanted:

**Prepare.** Record the interview with `pipeline set <slug> interview <date
and time>`. Run the coach (`references/team/08-coach.md`). Give the candidate
the day sheet and the three themes in plain words, and offer a practice run.

**Practise.** Ask one question at a time, as the interviewer would. Wait for
the answer. Then give short, specific, honest feedback: what worked, what was
vague, and which real example from the evidence bank would be stronger. Do
not hand over scripts. Stop when the candidate says so.

**Debrief.** Run the debriefer (`references/team/09-debrief.md`) live, one
question at a time, the same day if possible. Record the outcome with
`pipeline set`. Add new facts to the evidence bank. If a thank-you or a
request for feedback is appropriate, draft it for the candidate to send.

Points specific to this skill:

- If this job is not in the candidate's search yet, add it first, or prepare
  from the advert and CV directly and say that nothing will be kept.
- After a rejection, be factual and kind. "No reason given" is a valid entry.
  Do not speculate about why.
- After an offer, congratulate once, then help the candidate think about what
  to check before accepting. For contract terms, say a qualified person
  should look.
- Close the workspace before the final reply.
