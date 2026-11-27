# Set up Foothold

This one page takes you from nothing to a working job search. Follow it from
top to bottom. You do not need to know anything about AI.

Want to see the whole thing first? [How your job search works](https://f0zzy2727.github.io/foothold/how-it-works.html) shows
it on one page.

**You need:** a paid Claude plan, your CV as a file, and one job advert you
are curious about.

**Time:** about 15 minutes for steps 1 to 5. Step 6 takes about 45 minutes,
and you are needed for half of it.

Use Claude on the web or the Claude desktop app. If a menu name here does not
match what you see, ask Claude "How do I add a plugin?" Names were checked in
November 2026 and may change.

## Step 1. Add the plugin

1. Open Claude and go to **Customize**, then **Plugins**.
2. Choose **Add**, then **Add marketplace**.
3. Paste this and confirm:

   ```
   f0zzy2727/foothold
   ```

4. Add the plugin called **foothold** and make sure it is switched on.

Added this way, new versions arrive without you doing anything.

Prefer a file? Download `foothold.plugin` from the
[latest release](https://github.com/f0zzy2727/foothold/releases/latest),
then choose **Upload plugin** in the same menu.

## Step 2. Create a project

Go to **Projects** and choose **New project**. Call it "My job search".

A project is where Claude keeps your search between conversations. Always
talk to Claude about your search inside this project.

## Step 3. Paste the instructions

Open [the instructions for your project](PROJECT-INSTRUCTIONS.md). Copy
everything in the box there. Then open your project's instructions in Claude
and paste it in.

The text tells Claude how to run your search and what it must never do.

## Step 4. Add your CV

Add your CV to the project as a file. Word, PDF or plain text all work.

## Step 5. Check it works

Start a chat inside the project. Choose **Claude Opus** as the model. Then
run these three tests in order. Each tells you what you should see.

| Test | Type this | You should see | If you do not |
|---|---|---|---|
| 1 | `Run the setup tests` | A short table. "The plugin is switched on" and "Your search can be stored here and read back" both say PASS. | If Claude says the plugin is not switched on, go back to step 1. If storing fails, tell us (see the end of this page) and do not go further. |
| 2 | Start a **new chat** in the project, then `Run the setup tests` again | The line "This project remembers between conversations" now says PASS. | Check you are inside the project, not in an ordinary chat. |
| 3 | Paste your job advert, then `Is this job right for me?` | A verdict in about ten minutes: one of Strong fit, Worth tailoring, Stretch or Skip, with the reasons, and one thing that would change it. | Type `Check my setup` and follow what Claude says. |

If test 3 was useful, carry on. If it was not, you can stop here. Nothing
else has been set up.

## Step 6. Start your search

1. Type `Start my search`. Claude asks about you for about 20 minutes, one
   question at a time. Say "I do not know" whenever that is the honest
   answer.
2. When Claude asks, press the plus button under the message box and choose
   **Research**. Then type `Research my field`. This looks in depth at how
   your field hires. It takes a while and needs nothing from you. Switch
   Research off again when it is done.
3. Say yes when Claude offers to check for new jobs every weekday.

Then run two last tests:

| Test | Type this | You should see |
|---|---|---|
| 4 | Start a **new chat**, then `What should I do today?` | Claude answers from your saved search, without asking who you are. |
| 5 | `Show me my dashboard` | One page with your name on it, showing what needs you. |

The next day, look at the foot of your dashboard. A line saying "Last
automatic check" means the daily check is running by itself. If the line is
not there, type `Check for new jobs` yourself on weekdays.

## What to say from now on

| Say | What happens |
|---|---|
| `What should I do today?` | The few things that need you |
| `Check for new jobs` | Claude looks for openings and gives a verdict on each |
| `I found a job` | Paste or upload the advert with it, or send the advert on its own. You get a verdict, and it joins your search |
| `I applied to the Acme role` | Your search is updated |
| `I've got an interview` | Preparation, and a practice run if you want one |
| `What is my biggest gap?` | The missing skill that would open the most doors |
| `Review my search` | For when nothing new is turning up. Claude suggests ways to widen it, and changes nothing unless you say yes |
| `Show me my dashboard` | The whole search on one page |
| `How does this work?` | The whole thing explained in plain words |
| `Check my setup` | A full check, with safe repairs |

## Optional: a folder on your computer

In the Claude desktop app you can attach a folder to the project. Claude then
treats it as an in-tray and an out-tray: you drop your CV and adverts in, and
Claude puts your dashboard and finished Word documents there. This part is
new and less tested. If the folder gives trouble, leave it out. Nothing else
changes.

## If something goes wrong

Type `Check my setup`. Claude checks everything, repairs what it safely can,
and tells you plainly if anything needs you. A repair never deletes anything
and never changes your CV or your applications.

Still stuck? Tell us what happened at
https://github.com/f0zzy2727/foothold/issues. Remove anything personal first.
Never post your CV there.

## Before you rely on it

Foothold helps you run your own job search. It is not careers, legal or
financial advice, and nobody can promise an interview or an offer. Claude can
be wrong, so read everything before you send it. The full text is in
[DISCLAIMER.md](DISCLAIMER.md).
