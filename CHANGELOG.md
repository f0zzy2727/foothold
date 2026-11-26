# Changelog

## 0.10.0, 2026-11-26

No change to the search format.

Added
- For developers: typing "Load the test search" in a new project loads a
  ready-made search for an invented person, with the interview and the
  research already done, so the rest of the flow can be tested in minutes.
  Every date is moved to today. It loads only into a project with no search
  in it, and no skill offers it. `CONTRIBUTING.md` says how to use it.
- The script has a matching command, `test-search`.
- The page that explains the search has a switch for light and dark. It
  follows the device until the reader chooses, and the choice is kept in that
  browser only.

Changed
- The instructions a person pastes into their project have their own page,
  `PROJECT-INSTRUCTIONS.md`. Step 3 of `SETUP.md` and the page that explains
  the search link to it. The text itself is unchanged. The page links to the
  full setup guide beside its six steps.
- The invented search the tests run against moved from `tests/fixtures/`
  into the plugin, so the tests and the test search are one set of files.
  It gained two invented target organisations.

## 0.9.1, 2026-11-26

No change to the search format.

Fixed
- The script's help listed 13 of its 24 commands. The storage test, the gap
  map, projects, Word export and seven others were missing, so a Claude that
  asked the script what it could do was not told. The help now lists every
  command, grouped by what it is for, and a test keeps it complete.

## 0.9.0, 2026-11-26

No change to the search format.

Changed
- The plugin is now called `foothold`, not `job-search`. The folder is
  `plugins/foothold/`, the released file is `foothold.plugin`, and the
  phrases for scheduled runs are "run the foothold daily-check" and "run the
  foothold weekly-review". Claude treats a renamed plugin as a new one:
  remove `job-search`, add `foothold`, and paste the instructions from
  `SETUP.md` again, because the old ones name the old plugin.
- Nothing inside a saved search is renamed. Its documents stay under
  `job-search/`, and the marker file is still `.job-search`. A search saved
  with the old name opens unchanged.

Fixed
- After the setup tests, Claude said only "type Start my search", which reads
  as if the looking begins at once. The doctor now says what happens first:
  the questions about the person, then the field research, and only then any
  jobs. "Get to know me" also starts setup, and the first two stops on the
  explainer page show the words that begin them.

Added
- The page that explains the search now has a public address:
  https://f0zzy2727.github.io/foothold/how-it-works.html. GitHub Pages serves
  it from `docs/`.
- A link to that page in `SETUP.md` and the README, in the words Claude uses
  for help, and at the end of the setup tests when they pass.
- A test that every link to the page points at a file that exists.

## 0.8.0, 2026-11-26

No change to the search format.

Changed
- The dashboard is redesigned. A rail on the left holds the name, the date
  and the four signals, which now filter the page. Each role is a row that
  opens, with its place on a path of seven steps from found to offer. The
  first thing that needs the person is set larger than the rest. Counts are
  drawn as bars on one scale. Anything to say to Claude has a copy button.
  A page more than a day old says so.
- The dashboard no longer loads a typeface from Google Fonts. It loads
  nothing from any other site, and the privacy note says so.

Fixed
- The dashboard's title now carries the person's name. A published page takes
  its name from its own title, so every dashboard was listed as "My job
  search" whatever name Claude was told to give it.

Added
- `docs/how-it-works.html`: the page that explains the search, redesigned to
  match the dashboard. Its only copy was a published page. Ten stops on a
  path, a switch to show only the person's part, six set-up steps that follow
  `SETUP.md` and can be ticked off, and the things worth saying, each with a
  copy button.
- `FACTS.md`: what has been learned about how the plugin behaves in the
  Claude app.
- Two tests: neither page may load anything from another site, and each
  page's script must parse and keep its names inside one function.

## 0.7.1, 2026-11-26

No change to the search format.

Added
- `SETUP.md`: one page that takes a new person from nothing to a working
  search, with the project instructions to paste (in Role, Action, Context,
  Expectations form) and five bootstrap tests.
- "Run the setup tests": the doctor now reports a short pass or fail table,
  and works before any search has been saved.
- A test that the project keeps files between conversations, using the test
  file an earlier conversation left behind.
- Each save line gives the file's sha256, so a write to the project can be
  confirmed without reading the file back.
- `AGENTS.md` and `CLAUDE.md` for anyone working on this repository with a
  coding agent.

Changed
- The storage test file is smaller. Measured: a project document of about
  120,000 characters or less comes back as text that Claude must copy to disk
  by hand, so a large test file tested Claude's copying more than the
  storage. The checksum still catches any slip.

Fixed
- Two tests failed on a fresh clone because git does not keep empty folders.

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
