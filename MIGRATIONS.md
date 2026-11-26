# Changing a file format

A candidate's search outlives any one version of the plugin. People will open
a search made months ago with a newer plugin, and sometimes a newer search
with an older plugin. Both must be safe.

## The rule

If a change means a search written by the previous version would be read
wrongly, checked wrongly or be missing something the new version needs:

1. Raise `WORKSPACE_VERSION` in `pipeline.py`.
2. Add one step to `UPGRADES` that brings the previous format up to the new
   one. A step may add files, settings and derived data. It must never remove
   or rewrite anything the candidate wrote. It backs up every file it changes
   through the `backup` function it is given.
3. Add a test in `tests/test_pipeline.py` that downgrades the sample search,
   runs any command, and proves the candidate's files are byte for byte the
   same afterwards.
4. Add a line to the table below and to `CHANGELOG.md`.

Changes that need none of this: new commands, new checks that only warn, new
wording in briefs and skills, new optional files that the script creates when
missing.

A new check that fails on documents the previous version produced counts as a
format change. Either make it warn, or migrate.

## How an upgrade happens

The search carries its format number in `.state/version.txt`, which travels
in the core save. Every command checks it first. Older: the upgrade steps
run, the script prints `UPGRADED`, and backups go to
`.state/backup-upgrade-<time>/`. Newer: the script refuses and asks for the
plugin to be updated. Nothing is changed.

Save files have their own version in their first line. The reader accepts
every save version ever written. Never remove an old reader.

## History

| Format | Plugin | What changed |
|---|---|---|
| 1 | up to 0.5.0 | The first format. No version file: its absence means 1 |
| 2 | 0.6.0 | Settings for follow-up and tidying; `profile/contacts.md`; `archive/`; counters that survive archiving; save files version 2 with a content-derived separator and a save number |
| 3 | 0.7.0 | Settings for building evidence; `profile/skills.md`; `profile/projects/`; a Skill column in new match reviews (old reviews stay valid and are not counted); `.state/gaps.json` and `leverage.md` |
