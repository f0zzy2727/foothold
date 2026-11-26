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

## Testing in the Claude app without the interview or the research

A real setup takes most of an hour: about 20 minutes of questions, then a
research run. To test everything else, load a ready-made search for an
invented person, Sam Example. This is for developers. It is not part of the
plugin and no candidate sees it.

1. Run `scripts/test-search.py`. It writes `dist/test-search/`. Every date
   is moved so the search reads as if it were today, so build it on the day
   you test. Add `--place Dublin`, or any real place, if you want a daily
   check to find real adverts. Without it Sam lives in an invented town and
   a daily check finds nothing.
2. In Claude, follow steps 1 to 3 of `SETUP.md` in a new project. Use a
   project you will delete afterwards.
3. Start a chat in the project. Attach `test-search.zip` and paste the text
   of `PROMPT.txt` as the message. If the zip is refused, attach the `.txt`
   save files in the folder, leaving out `PROMPT.txt` and
   `sam-example-cv.txt`.
4. Start a new chat and carry on as a candidate would: "What should I do
   today?", "Show me my dashboard", "I applied to the Northside Festival
   role", "Check for new jobs".

The search holds seven roles at seven different stages, so most of what a
candidate can say has something to act on. Its profile and research are a few lines
each, which is enough to test that the flow works and not enough to judge
the quality of a verdict. It does not test the interview, a Research mode
run or the first half of "Start my search". Those need a real run.

By contributing you agree that your contribution is licensed under the MIT
licence that covers this project.
