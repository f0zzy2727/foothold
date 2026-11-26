# Deterministic checks

The script tests form, consistency and traceability. It gives the same answer
every time. It cannot tell whether a claim is true, whether a verdict is wise,
or whether research is correct: those rest on the specialists, the evidence
bank and the candidate.

| After stage | Run | The script fails the stage if |
|---|---|---|
| 0 | `pipeline check` | the target lacks segments, roles, level or locations; the sector pack named does not exist |
| 1 | `pipeline check --research` | the market map lacks a section, a research date, a refresh date or a method; fewer than five source links; a hypothesis has no finding; no target organisations or no sources. Warns if the method was web search only |
| 2 | `pipeline check` | the signals log has a duplicate |
| 3 | `pipeline check <slug> --stage 3` | no saved source; Type is not advert or approach; a required section is missing; a template placeholder is left in. Warns if the market context cites no link, and if the saved advert contains text addressed to an AI |
| 4 | `--stage 4` | a requirement has no verdict of met, partly met or not met; a met or partly met has no evidence id or CV reference; an evidence id does not exist; a requirement has no skill name, or a skill name that is not in `profile/skills.md` (reviews written before skill names existed are accepted and simply not counted) |
| 11 | `pipeline project <slug> done` | the project has no proof recorded; no line in the evidence bank has the source `project <slug>`; the project file does not cite that line's id. Also refuses a second project while one is in progress, and a project whose skill is not in `profile/skills.md` |
| 5 | `--stage 5` | the verdict is not one of the four bands; no readiness figure; closing date is not a date or "none stated"; stage 3 found red flags and the summary does not mention them; the advert contains text addressed to an AI and the summary does not say "hidden instructions" |
| 6 | `--stage 6` | tailored CV or covering note missing; any change in `changes.md` cites no evidence or cites an id that does not exist |
| 7 | `--stage 7` | any claim is not marked supported; a number in the application is not in the master CV, the evidence bank or the advert; a term from the advert is new to the application and not addressed in the verification; a name, a qualification or seniority word ("degree", "fluent", "managed", "senior" and similar) or a number written as a word appears in the application, is in neither the master CV nor the evidence bank, and has no supported row citing evidence; no send checklist |
| 8 | `--stage 8` | fewer than three themes; no interview date; an evidence id does not exist |
| 10 | `--stage 10` | the outcome is not one of the allowed values; no date |
| every run | `pipeline check` | a status does not match the files present; the active limit is exceeded; ids or question numbers are duplicated. Warns when the research refresh date has passed, and on closing dates that have passed or fall within three days |

`pipeline doctor` runs all of the above across the whole setup, adds checks
on folders, settings, caches, logs, save files, the history, the storage
test, the last automatic check and the size of the everyday save, and with
`--fix` repairs what is safe. See the doctor skill.

The plugin's own tests are in the repository beside the plugin
(`tests/test_pipeline.py`). They run every check above against a deliberately
dishonest application, an advert with planted instructions, a damaged save
and a search in the old format.

Also deterministic, by script and never by hand: status changes
(`pipeline set`), the pipeline table (`pipeline pipeline`), funnel counts
(`pipeline funnel`), the gap map (`pipeline leverage`: which missing skills
recur, and for how many adverts each is the only essential missing), change
detection (`pipeline changed`), closing and
archiving stale roles (`pipeline tidy`, run by `close`), the save files and
the guard against two sessions saving over each other (`pipeline guard`), and
upgrades of a search made with an older version (`pipeline migrate`).

One limit to state honestly: the checks are deterministic, but running them
depends on the coordinator following the engine skill. The hard stops are in
the script itself: `pipeline set` refuses to move an opportunity forward
until its checks pass.
