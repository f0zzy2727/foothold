# Foothold

**An honest, systematic job search, run with Claude.**

[![tests](https://github.com/f0zzy2727/foothold/actions/workflows/tests.yml/badge.svg)](https://github.com/f0zzy2727/foothold/actions/workflows/tests.yml)
[![licence: MIT](https://img.shields.io/badge/licence-MIT-blue.svg)](LICENSE)

Foothold is a plugin for Claude that helps one person run their own job
search properly. Paste a job advert and your CV and you get a straight
verdict in about ten minutes. If that is useful, it runs the whole search
with you: it finds openings, judges each one against what you have really
done, prepares each application for you to send, coaches you for interviews
and learns from every result.

You do not need to know anything about AI. You talk to it in ordinary
sentences.

It was first built for people looking for a way into the music industry. It
works for any career: Claude drafts the sector knowledge it needs when you
set it up.

## Three promises

1. It will not apply, email or contact anyone for you.
2. It will not put anything in your CV that you have not told it or shown it.
3. It will tell you when a role is not worth your time, and why.

## Get started

**Follow [SETUP.md](SETUP.md).** It is one page, written for someone who has
never used an AI tool. It takes you from nothing to a working search in six
steps, and it includes five short tests so you can see for yourself that each
part works before you depend on it.

The short version:

1. Add the plugin to Claude: Customize, then Plugins, then Add marketplace,
   and paste `f0zzy2727/foothold`.
2. Create a project called "My job search".
3. Paste the instructions from SETUP.md into the project.
4. Add your CV.
5. Type `Run the setup tests`, then paste an advert and type
   `Is this job right for me?`
6. Type `Start my search`.

In Claude Code, version 2.1.275 or later:

```
/plugin install job-search --marketplace f0zzy2727/foothold
```

### The bootstrap tests

These are the checks in SETUP.md. Run them in this order on a new setup.

| Test | Type this | Proves |
|---|---|---|
| 1 | `Run the setup tests` | The plugin is on, its checks run, and your search can be stored in the project and read back |
| 2 | A new chat, then `Run the setup tests` | The project keeps your search between conversations |
| 3 | An advert, then `Is this job right for me?` | You get an honest verdict from your own CV |
| 4 | After `Start my search`: a new chat, then `What should I do today?` | Claude picks up your saved search without being told who you are |
| 5 | `Show me my dashboard` | The whole search appears on one page |

Tests 1 to 3 take about 15 minutes and need no commitment. If test 1 says
storing failed, stop there and open an issue.

## What it does

| Step | Claude does | You do |
|---|---|---|
| 1 | Gets to know you, in a 20 minute chat | Share your CV and what you want, once |
| 2 | Researches how your field really hires | Switch Research on when asked |
| 3 | Looks for openings every weekday | Pass on any you find yourself |
| 4 | Gives an honest verdict: go for it, or skip | Choose what to pursue |
| 5 | Tailors and checks your CV, using only true things | Read it and press send |
| 6 | Coaches you for the interview, then learns from the result | Go, then say how it went |

One page, your dashboard, shows the whole search. Three signals tell you
where to look: red means urgent, amber means it is your turn, green means on
track with nothing to do.

It also reminds you to follow up when an application has had no reply, keeps
a short list of people who could help, and tidies away roles that have
closed.

## It helps you build evidence, not only present it

Rewording a CV cannot fix a missing skill. Once Foothold has read about ten
adverts for you, it counts which missing skills come up again and again and
shows the one that would open the most doors: "QLab comes up in 10 of your 12
adverts. In 3 of them it is the only essential you are missing."

It then suggests up to three small, real projects to close that gap, each a
weekend to two weeks long and each ending with something you can show. You
pick one, or none. Nothing goes on your record until you have done it. Then
every job it affects gets a fresh verdict.

## Status

Version 0.7.1. An early pilot.

**Tested**, by the automated suite in this repository: the honesty checks
against a deliberately dishonest application, an advert with instructions
planted for AI tools, the rules for moving an application forward, saving and
restoring a search, damaged saves, two sessions saving at once, closing and
archiving stale roles, the Word documents, the gap map and its projects,
upgrading a search from earlier versions, and repairing a deliberately broken
search.

**Not yet tested**: a full search with a real candidate, a real Research mode
run started by the plugin, whether the projects it suggests are good ones,
and whether a scheduled daily check can reach the Project that holds the
search. The setup check tests your own Project's
storage for real, and the dashboard shows when an automatic check last ran,
so you can see for yourself.

## Please read: disclaimer

Foothold helps you run your own job search. It is not careers, legal or
financial advice, and nobody can promise an interview or an offer. Claude can
be wrong, so read everything before you send it: what goes out under your
name is yours. The tool cannot confirm that an advert is genuine. It is
provided as is, with no warranty.

Foothold is an independent project. It is not affiliated with or endorsed by
Anthropic. "Claude" is a trademark of Anthropic, PBC.

The full text is in [DISCLAIMER.md](DISCLAIMER.md).

## Privacy

- Foothold has no server, no accounts and no analytics. It collects nothing.
- Your CV, your evidence and your applications stay where you keep them: in a
  Project in your own Claude account, or in a folder on your computer. How
  Claude handles that content is set by Anthropic's privacy policy and your
  own Claude settings.
- Your dashboard is published as a private page. If you choose to share it,
  whoever you share it with can see your search.
- The dashboard page loads one typeface from Google Fonts, so opening it
  makes a request to Google.
- The list of people who could help holds other people's details. Keep it to
  what you would put in an address book.
- If you report a problem here, remove anything personal first. Never post a
  real CV or a saved search in an issue.

## For developers

| Path | What it is |
|---|---|
| `SETUP.md` | The one page a new person follows, with the project instructions and the bootstrap tests |
| `plugins/job-search/` | The plugin: ten skills, the specialist briefs, the templates and one script |
| `.claude-plugin/marketplace.json` | Lets Claude install the plugin from this repository |
| `tests/` | The test suite and an invented sample search it runs against |
| `scripts/package.sh` | Runs the tests, then builds `dist/job-search.plugin` |
| `CHANGELOG.md` | What changed in each version |
| `MIGRATIONS.md` | The rule for changing a file format, so old searches keep working |

The project is called Foothold. The plugin it ships is called `job-search`,
which is the name Claude and its skills use.

```
python3 -m unittest discover -s tests -v     # run the tests
scripts/package.sh                           # test, then build the upload file
```

The tests need Python 3 and nothing else (checked on 3.11 and 3.13). They run
on every push.

To release a version:

1. Change the version in `plugins/job-search/.claude-plugin/plugin.json` and
   in every `SKILL.md`. A test fails if they disagree.
2. If a file in a person's saved search changed shape, follow `MIGRATIONS.md`.
3. Add an entry to `CHANGELOG.md`.
4. Run the tests, commit, then tag and push: `git tag v0.7.1` and
   `git push --tags`. The release workflow builds the upload file and
   attaches it to a GitHub release.

What a script cannot test: whether Claude follows the skills as written, the
quality of a verdict, a real Research mode run, and whether a scheduled task
can reach a Project. Those need real use, which is what the pilot is for.

Nothing in this repository is about a real person. The sample search in
`tests/fixtures/` is invented.

## Contributing, security, licence

- How to help: [CONTRIBUTING.md](CONTRIBUTING.md)
- Reporting a security problem: [SECURITY.md](SECURITY.md)
- Licence: [MIT](LICENSE). Copyright 2026 LUGHa.
