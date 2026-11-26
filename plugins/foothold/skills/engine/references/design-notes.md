# Design notes

Why the system is built this way, and what each choice rests on. For whoever
maintains or adapts it. Researched 26 November 2026.

## 1. A fixed workflow, not a free-roaming agent

Anthropic's guidance on agentic systems recommends the simplest design that
works, and separates workflows (model calls arranged along predefined paths)
from agents (the model directs its own process). It says workflows give
predictability and consistency for well-defined tasks. A job application is a
well-defined sequence, so this system is a workflow with gates.

Source: https://www.anthropic.com/research/building-effective-agents

## 2. Programmatic gates between stages

The same guidance describes adding programmatic checks ("gates") to
intermediate steps of a chained workflow to keep the process on track. That is
the `pipeline` script: a stage is not finished until its check passes,
and a status cannot change unless the script allows it.

## 3. A separate checker for the application

The guidance describes an evaluator pattern in which one model call produces
and another evaluates. Claude Code's own guidance on sub-agents recommends a
fresh sub-agent when an unbiased review is needed, because it does not inherit
the assumptions of the work it reviews. Stage 7 therefore runs in a fresh
sub-agent, and the script checks its output.

Source: https://claude.com/resources/articles/subagents-in-claude-code

## 4. One specialist per stage

The same article names pipeline workflows, sequential stages with clear
handoffs, as a good fit for sub-agents: each stage gets focused context. The
cost is usage, since each sub-agent makes its own requests. This is why the
system screens cheaply first (stage 2) and reruns only what changed.

Each brief follows the points Anthropic's training material stresses for
sub-agents: a clear description of the job, a defined output format, an
instruction to report obstacles, and limited scope.

Sources: https://code.claude.com/docs/en/best-practices and
https://academy.claude.com/courses/introduction-to-subagents/designing-effective-subagents

## 5. Instructions are advisory; hooks are deterministic

Claude Code's documentation is explicit: an instruction in a skill or a
CLAUDE.md file is something the model reads and usually follows, with no
guarantee, while a hook is run by the harness every time.

This plugin does not ship a hook yet. A hook that misfires would interrupt
every session, and it could not be tested on a real desktop install before
release. The hard stops are therefore inside the script: `pipeline set`
refuses to move an opportunity forward until its checks pass, and
`pipeline restore` refuses a save file that fails its checksum. Adding a hook
that runs `pipeline check` is the next step once it has been tested.

Plugin components load differently by surface: skills load in chat, Cowork
and Claude Code; agents and hooks load in Cowork and Claude Code and are
ignored in chat. The plugin is skills only so that it behaves the same
everywhere.

Sources: https://code.claude.com/docs/en/best-practices ,
https://code.claude.com/docs/en/hooks-guide and
https://claude.com/docs/plugins/platform-support

## 6. Skill and motivation together

A meta-analysis of 47 job search interventions (Liu, Huang and Wang,
Psychological Bulletin, 2014) found that participants were considerably more
likely to find work than non-participants, and that programmes helped only
when they combined skill development with motivation enhancement. The
components associated with success were: teaching job search skills, improving
self-presentation, boosting self-efficacy, encouraging proactivity, promoting
goal setting, and enlisting social support.

How the system maps to these:

| Component | Where it is |
|---|---|
| Job search skills | research, scout, spec analysis |
| Self-presentation | tailoring, verification, interview preparation |
| Self-efficacy | "Progress you can point to" in the weekly review; honest verdicts |
| Proactivity | the approach path; the candidate's own inbox |
| Goal setting | the candidate chooses a goal each week |
| Social support | an optional named supporter, asked about at intake |

Caveat: the study covers structured programmes run by people, mostly for
unemployed job seekers. It is evidence for the ingredients, not for this
system.

Source: https://doi.org/10.1037/a0035923

## 6a. Research is done in Research mode, attended

The market research uses Claude's dedicated Research mode, which the person
switches on from the plus button under the message box. It cannot be switched
on by a skill or a scheduled task, so research and every refresh are attended
steps. The request is assembled by the script from the candidate's answers
and the sector pack, so nothing is lost in paraphrase.

Source: https://support.claude.com/en/articles/11088861-use-research-on-claude

## 7. What has and has not been validated

Tested, with a deliberately dishonest test application:
- the stage checks, the status rules, the active limit and the tracker
- cloud save and restore, including an exact round trip and refusal of a
  save file that was cut short or altered
- writing a script-generated save file into a Claude Project
- the dashboard, built by the script from a sample search and rendered once
- the doctor, run against a deliberately broken copy of a sample search: ten
  faults repaired, every changed file backed up, the candidate's CV and
  evidence left untouched

Not yet tested:
- an end-to-end run with a real candidate
- installation of the plugin on a real account
- whether a scheduled run can reach the Project that holds the saved search
- the sector packs, which contain hypotheses for the researcher to test

The checks verify form and traceability. A false statement the candidate
made at intake will pass every check.

## 8. Next capabilities, in order of value

1. **A hook** that runs the check automatically (see note 5).
2. **Mail and calendar connectors**, in the candidate's own account: job
   alert emails become signals, interview dates become calendar entries,
   outreach is saved as drafts for the candidate to send.
3. **A browser extension**, for job boards that need the candidate's own
   sign-in. The scout brief forbids signing in on its own.
4. **Document skills** (Word, PDF), so the tailored CV is produced in the
   same format as the original.
5. **Publishing the dashboard automatically** from a scheduled run, once
   scheduled runs are confirmed to reach the saved search.

## Decisions in version 0.6.0

- **Fair but direct.** Verdicts are judged at the level the advert states,
  and unpaid or project evidence counts in full. This matters most for people
  at the start of a career, whose evidence is rarely paid work. The telling
  stays blunt.
- **Adverts are untrusted text.** An advert or a web page can contain words
  written for AI tools. The briefs say never to act on them, the script scans
  each saved advert for the common forms, and the summary must tell the
  candidate. The scan is a tripwire, not a guarantee.
- **The honesty check is a net, not a judge.** It now also catches numbers
  written as words, names not in the candidate's record, and qualification
  or seniority words. It still cannot catch an invented claim in ordinary
  words; the independent checker in stage 7 is the second line.
- **Not every job is on a readable web page.** Web search is one route. The
  candidate's own finds are first class, and sources Claude cannot read are
  listed for the candidate to check weekly.
- **Following up and people.** A follow-up reminder after ten days and a
  short contacts list were added because they are ordinary good practice in
  a job search and cost the candidate little. The numbers are starting
  defaults in the settings, not evidence-based targets.
- **Bounded saves.** Roles close themselves when stale and move to an
  archive a month later, so the everyday save stays small.
- **Two sessions.** A scheduled check and a conversation can overlap. Each
  save carries a number, and a session may write only if nothing saved since
  it opened.
- **Upgrades.** The search carries a format number. A newer plugin brings an
  older search up to date automatically, backing up what it changes. An older
  plugin refuses a newer search. Every format change ships with a migration
  step and a test.
- **Model.** Opus for setup, applications and interview practice; Sonnet for
  the daily check. A starting recommendation, to be confirmed against real
  usage in the pilot.

## Decisions in version 0.7.0: the gap map

- **Why.** Everything up to here optimised how a fixed past is presented.
  For someone at the start of a career the constraint is the past itself. A
  run of honest Stretch and Skip verdicts with nowhere to go is the likeliest
  way this tool fails its first users.
- **Counting, not predicting.** The script counts, across the adverts
  analysed in the last 120 days, how often each skill is asked for, how often
  the candidate cannot show it, and for how many adverts it is the only
  essential missing. That last number is the nearest deterministic thing to
  "what would change the most verdicts". No model estimates it.
- **One name per skill.** The count is only as good as the naming. A shared
  list (`profile/skills.md`) with "also written as" forms, a check that
  refuses unknown names, a single writer (the coordinator) and a monthly
  merge by the reviewer keep names stable. This is the weakest joint and the
  one to watch in the pilot.
- **Evidence only when done.** A project is a file with a status. The script
  refuses "done" without recorded proof and an evidence line whose source
  names the project. The evidence states what was done at the size it was
  done.
- **The candidate's choice, one at a time, no chasing.** The script raises
  the project again only when the date the candidate chose arrives.
- **Not exploitation.** Unpaid work for a commercial employer is never
  proposed as a project.
- **Thresholds are defaults.** Ten adverts before a focus is suggested, a
  gap missing in at least three. Starting values, not evidence-based.
