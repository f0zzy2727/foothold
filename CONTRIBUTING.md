# Contributing

Thank you for looking. This is a small project in an early pilot, so the most
useful contribution right now is a clear report of what happened when a real
person used it.

## Reporting how it went

Open an issue and say: what you asked Claude, what it did, and what you
expected. Say whether you used a Project or a folder, and which Claude app.
Remove anything personal first. Never post a real CV or a saved search.

## Changing the code or the wording

1. Run the tests before and after: `python3 -m unittest discover -s tests -v`.
2. Keep the script to the Python standard library.
3. If your change alters a file in the person's saved search, read
   `MIGRATIONS.md` first. Old searches must keep working.
4. Write for someone who has never used an AI assistant. Short sentences,
   plain words, no jargon. The skills under `plugins/foothold/skills/` are
   instructions to Claude, written as directives.
5. Do not weaken the three promises: it never contacts anyone for the
   person, it never writes anything about them that they did not say, and it
   tells them when a role is not worth their time.
6. Add a line to `CHANGELOG.md`.

Use only invented people and organisations in tests and examples.

By contributing you agree that your contribution is licensed under the MIT
licence that covers this project.
