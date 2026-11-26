# Job search

An honest, systematic job search, run with Claude.

Start with one job: paste an advert and your CV and get a straight verdict in
about ten minutes. If that is useful, let it run your whole search: it finds
openings, judges each one against what you have really done, prepares each
application for you to send, coaches you for interviews and learns from every
result.

You do not need to know anything about AI. You talk to it in ordinary
sentences.

## Who does what

| Step | Claude does | You do |
|---|---|---|
| 1 | Gets to know you, in a 20 minute chat | Share your CV and what you want, once |
| 2 | Looks for openings every weekday | Pass on any you find, and check the few places Claude cannot read |
| 3 | Gives an honest verdict: go for it, or skip | Choose what to pursue |
| 4 | Tailors and checks your CV, using only true things | Read it and press send |
| 5 | Coaches you for the interview, then learns from the result | Go, then say how it went |

It also reminds you to follow up when an application has had no reply, keeps
a short list of people who could help, and tidies away roles that have
closed.

## Closing your biggest gap

Rewording a CV cannot fix a missing skill. Once Claude has read about ten
adverts for you, it counts which missing skills come up again and again, and
shows you the one that would open the most doors: "QLab comes up in 10 of
your 12 adverts. In 3 of them it is the only essential you are missing."

Ask *What is my biggest gap?* and it suggests up to three small, real
projects to close it, each taking a weekend to two weeks and each ending
with something you can show. You pick one, or none, and choose your own
finish date. Nothing goes on your record until you have done it and shown
it. Then every job it affects gets a fresh verdict.

Three promises:

1. It will not apply, email or contact anyone for you.
2. It will not put anything in your CV that you have not told it or shown it.
3. It will tell you when a role is not worth your time, and why.

## Set up in six steps

The full guide, with the instructions to paste into your project and five
short tests to check each part works, is one page:
https://github.com/f0zzy2727/foothold/blob/main/SETUP.md

You need a paid Claude plan, this plugin and your CV. Allow about an hour
the first time. You are only needed for half of it.

**Which model:** choose Claude Opus in the model picker and leave it there.
It is the right balance for this work. If you run short of usage, the daily
check works well on Sonnet. You do not need the most powerful model.

1. **Add the plugin to Claude.** Open Claude. Go to Customize, then Plugins.
   Choose Add, then Add marketplace, and paste `f0zzy2727/foothold`. Updates
   then arrive without you doing anything. If you were sent a plugin file
   instead, choose Upload plugin and pick the file.
2. **Make a home for your search.** Go to Projects and choose New project.
   Call it "My job search". Paste the project instructions from the setup
   guide, and add your CV with the plus button. Then type: *Run the setup
   tests.*
3. **Try it on one job.** Inside that project, start a chat. Paste a job
   advert and type: *Is this job right for me?* You get an honest verdict in
   about ten minutes. If that is not useful, stop here.
4. **Start the full search.** In the same project, type: *Start my search.*
   Claude first checks that your search can be kept safely in this project,
   then asks about you for about 20 minutes, one question at a time.
5. **Research your field.** When Claude asks, press the plus button under the
   message box and choose Research. A blue marker appears. Type: *Research my
   field.* This looks in depth at how your field hires, for your level, your
   location and your goals. It takes a while and needs nothing from you. When
   it is done, press the blue marker to switch Research off.
6. **Keep it going.** On weekdays, open the project and type: *Check for new
   jobs.* To see where everything stands, ask: *Show me my dashboard.* When
   you find a job yourself, paste the advert or add the file and say: *I
   found a job.*

Stuck on any step? Ask Claude in plain words, for example "How do I add a
plugin?" Menu names were checked against Claude's help pages in November 2026
and may change.

A folder on your computer also works as the home for your search, in place of
a Project.

## Your dashboard

One page shows the whole search: what needs you now, every role and where it
stands, and what happened lately. Three signals tell you where to look: a red
triangle means urgent, an amber person means it is your turn, and a green
tick means on track with nothing to do. Claude rebuilds it
after every check and after everything you tell it. It does not change when
something happens outside a conversation with Claude.

## What you can say

| Say | What happens | Skill |
|---|---|---|
| "Is this job right for me?" | A verdict on one job, no setup | `try-one-job` |
| "Start my search" | The interview and the schedule | `start-my-search` |
| "Research my field" or "Refresh the research" | In-depth research for your field, level, location and goals | `research-my-field` |
| "What should I do today?" | The three things that need you | `my-search` |
| "I applied to the Acme role" | Your tracker is updated | `my-search` |
| "I found a job" (paste or add the advert) | A verdict on it, and it joins your search | `my-search` |
| "I followed up with them" | The reminder is cleared | `my-search` |
| "I know someone at Acme" | They go on your list of people, with a next step if you want one | `my-search` |
| "Give me my CV as a Word file" | The tailored CV and covering note as Word files | `my-search` |
| "What is my biggest gap?" | The missing skill that would open the most doors, and project ideas to close it | `close-the-gap` |
| "I finished my project" | It goes on your record, and affected jobs get a fresh verdict | `close-the-gap` |
| "Why did you say skip?" | The reasoning, with the evidence | `my-search` |
| "Show me my dashboard" | One page with the whole search | `my-search` |
| "Check my setup" or "Something is not working" | A full check, with safe repairs | `doctor` |
| "I've got an interview" | Preparation, and a practice run if you want one | `interview-coach` |
| "I had the interview today" | A short debrief, so the next one goes better | `interview-coach` |
| "How is my search going?" | The weekly review | `weekly-review` |

Two skills normally run on a schedule and not by hand: `daily-check` on
weekdays, and `weekly-review` on Fridays and once a month. Claude offers to
set these up at the end of "Start my search".

## If something seems wrong

Say: *Check my setup.* Claude checks the plugin, where your search is kept,
your schedule and every saved document. It repairs what it safely can and
tells you plainly if anything needs you. A repair never deletes anything and
never changes your profile, your evidence, your CV or your applications.
Every file it does change is backed up first.

## Getting a newer version

If you added the plugin from a marketplace address, Claude picks up new
versions for you. If you were sent a file, add the new file the same way as
the first. Either way your search is safe: the first time the new version
opens it, your search is brought up to date automatically, with a backup, and
nothing you wrote is changed.

## Where it works

| | One job verdict | Full search | Unattended daily checks |
|---|---|---|---|
| Claude on the web or phone, in a Project | yes | yes | to be confirmed, see below |
| Claude desktop app, in a Project | yes | yes | to be confirmed, see below |
| Claude desktop app, with a folder on your computer | yes | yes | not relied on |
| A plain conversation, no Project | yes | this conversation only | no |

## What is in the plugin

- Nine skills you can use: `try-one-job`, `start-my-search`,
  `research-my-field`, `my-search`, `close-the-gap`, `interview-coach`,
  `daily-check`, `weekly-review`, `doctor`
- One internal skill, `engine`, which holds the method: twelve specialist
  briefs, the document templates, the sector packs and a checking script
- No connectors are required. Mail and calendar connectors are useful later.
- A sector pack for the music industry. Any other career works: Claude drafts
  a pack for it at setup.

## Honest status, version 0.9.1

Tested by an automated test suite that ships with the source: the checking
script against a deliberately dishonest application, an advert with planted
instructions, the status rules, the dashboard, saving and restoring a search,
refusal of a damaged save, two sessions saving at once, closing and archiving
stale roles, the Word documents, the gap map and its projects, the upgrade
from earlier formats, and the doctor against a deliberately broken search.

The research runs in Claude's Research mode, which you switch on yourself. It
is refreshed every 90 days, or whenever you say "Refresh the research".

Not yet tested: installing on a real account, a real Research mode run
started by this plugin, a full search with a real candidate, and whether a
scheduled run can reach the Project that holds the saved search. The setup
check now tests the first of those storage questions for real in your own
project, and your dashboard shows when an automatic check last reached your
search. Until you see that line appear, start the daily check yourself by
saying "check for new jobs".

The gap map is counting, not prediction. It tells you which missing skill
recurs and where it is the only essential missing. It cannot promise that
closing it will win an interview, and it depends on Claude giving the same
skill the same name each time, which a shared list of names and a check help
with but cannot guarantee. Whether the projects Claude suggests are good ones
is untested with real candidates.

The honesty check is stronger than before but is still a net, not a judge.
It catches numbers, names, qualifications and seniority words that are not in
your CV or your evidence. It cannot catch an invented claim written in
ordinary words, which is why a second, independent check reads every
application as well.

The checks confirm that every claim in a tailored CV traces to something you
said. They cannot tell whether what you said is true.

## Please read

This is a tool to help you run your own job search. It is not careers, legal
or financial advice, and nobody can promise an interview or an offer. Claude
can be wrong, so read everything before you send it: what goes out under your
name is yours. The full disclaimer, the privacy note and the licence (MIT)
are in the project's repository, https://github.com/f0zzy2727/foothold. This
is an independent project and is not affiliated with or endorsed by
Anthropic.

## For whoever sets this up for someone else

The search works only if the candidate owns it. Agree what they want before
setup and let them do the interview with Claude themselves. A good role for a
parent or friend is supporter: the person the candidate shares their weekly
goal with.
