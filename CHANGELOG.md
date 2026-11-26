# Changelog

## 0.7.0, 2026-11-26

Search format 3. Searches made with 0.5.0 or 0.6.0 are upgraded
automatically.

Added
- The gap map. Across every advert analysed in the last 120 days the script
  counts which skills are asked for, which the candidate cannot show yet, and
  for how many adverts each is the only essential missing. Shown on the
  dashboard, in `leverage.md` and in the weekly review.
- Projects. For the biggest gap that a short project can close, the new
  project guide proposes up to three small real projects. The candidate
  picks one and a finish date. The script refuses to mark it done without
  recorded proof and an evidence line that names the project.
- Once a project is finished, adverts reviewed before it stop counting that
  skill as a gap. Roles reviewed afterwards carry the matcher's own view.
- A `close-the-gap` skill: "What is my biggest gap?", "I finished my
  project".
- `profile/skills.md`: one agreed name per skill, with other wordings, so
  the same skill is counted once. Match reviews carry a Skill column, and
  the check refuses a name that is not on the list.
- When a verdict moves up or down after new evidence, the script records it
  and the dashboard shows it.

Not changed
- Match reviews written before 0.7.0 are still valid. They are left out of
  the gap map until their next review.

## 0.6.0, 2026-11-26

Search format 2. Searches made with 0.5.0 are upgraded automatically.

Added
- Setup check that stores a test file of realistic size where the search
  will live and reads it back, at setup and whenever the doctor runs.
- The dashboard and the doctor show when an automatic check last reached the
  search.
- Stale roles close themselves (expired, no decision, no response) and move
  to an archive a month later. Nothing is deleted. All limits are settings.
- A follow-up reminder ten days after applying, with a drafted note.
- A short list of people who could help, with next steps that surface on the
  dashboard when due.
- Jobs the candidate finds are first class: paste or add an advert and say
  "I found a job". Sources Claude cannot read are listed for the candidate
  to check weekly.
- The tailored CV and covering note are written as Word files when an
  application becomes ready.
- A guard that stops two sessions saving over each other, and stops an empty
  new search overwriting a stored one.
- Automatic upgrade of a search made with an older version, with backups. A
  search from a newer version is refused, not damaged.
- A test suite, a marketplace file and a packaging script.
- A model recommendation: Opus for setup and applications, Sonnet for the
  daily check.

Changed
- Honesty check: also catches numbers written as words, names that are not
  in the candidate's record, and qualification or seniority words.
- Adverts and files are treated as untrusted text. Words in them addressed
  to an AI are never acted on, are flagged by the script, and must be
  reported to the candidate.
- Verdicts are "fair but direct": judged at the level the advert states,
  unpaid and project evidence counts in full, and each verdict says what
  would change it.
- The verdict line accepts a hyphen, a colon, a bracket or nothing after the
  band.
- Save files use a separator worked out from their content, so a document
  can contain any text.

Fixed
- A session that had loaded only the core save could overwrite stored
  research with blank starter files.
- Progress totals were wrong in a session that had not loaded every month's
  log of openings.
- The engine told the coordinator to write items into the to-do list by
  hand in three places; the script owns that list.

## 0.5.0

The doctor skill, the palette and the signal system. Not released outside
testing.
