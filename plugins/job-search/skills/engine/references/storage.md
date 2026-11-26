# Where the search lives

The workspace is the candidate's set of files. Work on it in a folder on
disk, because the script reads files. Where that folder is kept between
sessions depends on what this session can reach. Check in this order.

## A. A folder on the candidate's computer (local mode)

Use this when a connected folder already contains a `.job-search` file, or
when the candidate asks to keep the search in a folder they can see.

- **Open:** use the folder as the workspace. If it is new, run
  `pipeline init <folder>`, then `pipeline storage-test make`, which checks
  the folder can be written to.
- **Close:** run `pipeline close "<what happened>"`, for
  example `pipeline close "the daily check"` or `pipeline close "you said you
  applied to Acme"`. It records the event, runs the checks, and rebuilds the
  tracker, `NEXT.md` and `dashboard.html` in the folder. Nothing else to do.
  Roles that closed more than a month ago move to `archive/`.
- Scheduled runs may not be able to reach a folder on a computer. If the
  candidate wants unattended daily checks, recommend B.

## B. The candidate's Claude account (cloud mode, the default)

Use this when the session is attached to a Project and has a tool that can
list, read and write that Project's documents. The workspace is stored there
as a few plain text save files under `job-search/`.

| Save file | Holds | Restore it when |
|---|---|---|
| `job-search/core.txt` | profile, evidence bank, text CV, questions, settings, every status | every session |
| `job-search/opp-<slug>.txt` | one opportunity's documents | you will work on that opportunity |
| `job-search/research.txt` | market map, targets, sources | the scout or researcher runs |
| `job-search/signals-<yyyy-mm>.txt` | that month's signals log | the scout runs |
| `job-search/review-<name>.txt` | one review | rarely; reviews are for reading |
| `job-search/latest.txt` | one line: the number of the latest save | read at every close, written last |

### Open

1. `pipeline init ./job-search --cloud` in the working directory. Use
   `./job-search` as the workspace for the rest of the session.
2. List the Project's documents. If there is no `job-search/core.txt`, this
   is a new search: continue with setup.
3. Read `job-search/core.txt` and get it onto disk **exactly as stored**. If
   the tool hands back a file path, use that file. If it hands back text,
   write that text to a file without changing a character.
4. `pipeline restore <file>`. The save carries a checksum. If the script says
   REFUSED, the text was cut short or altered: fetch it and write it once
   more. If it is refused again, stop, change nothing, and hand over to the
   `doctor` skill. Never continue from a partial restore.
5. Restore other save files only as the table says. An opportunity that is
   not restored still appears in the tracker; the script reports it as
   "stored, not loaded" and will not move it past a gate.
6. Pass the names of the Project's other documents to `pipeline newfiles`.
   Anything it reports as NEW may be an advert or a CV the candidate added.

### The storage test (at setup, and whenever the doctor runs)

1. `pipeline storage-test make`. It writes a test file of about the size a
   real search reaches.
2. Write that file to the Project as `job-search/setup-test.txt`, passing the
   file itself.
3. Read `job-search/setup-test.txt` back and get it onto disk exactly as
   returned.
4. `pipeline storage-test check <that file>`. PASS means this place can keep
   a search. FAIL means it cannot: say so plainly and do not continue setup.

### Close

Do this before the final reply of every session that changed anything, however
small: a scheduled check, or one thing the candidate told you.

1. If there is something the candidate should know that the script cannot
   work out for itself, add it as a line under a `## Notes` heading in
   `NEXT.md`. The script writes the rest of that file and keeps your notes.
2. Run `pipeline close "<what happened>"`, in plain words the candidate would
   recognise, for example `pipeline close "the daily check"` or
   `pipeline close "you said you applied to Acme"`. In one step it records the
   event, runs the checks, rebuilds the tracker, `NEXT.md` and
   `dashboard.html`, and writes the save files. It prints one SAVE line for each file that changed.
3. Read `job-search/latest.txt` from the Project and run
   `pipeline guard <its text>`, or `pipeline guard none` if the Project has
   no such document yet. If the script says REFUSED, another conversation or
   a scheduled check saved the search after this session opened it. Write
   nothing. In an attended session, open the search again in a new folder,
   make this session's change again, and close. In a scheduled run, stop and
   report it in one sentence.
4. Publish the dashboard, if this session can publish a web page. The first
   time, publish `dashboard.html` as a private page titled "<Name>'s job
   search", write its address and id on one line in
   `.state/dashboard-link.txt`, and run `pipeline save` again. Every later
   time, republish to that same page so the candidate's link never changes.
   Never make the page public. If this session cannot publish pages, skip
   this step.
5. For each SAVE line, write that file to the Project path shown, passing the
   file itself. Write `job-search/latest.txt` last. Never retype a save
   file's content: a retyped file fails its checksum next time.
6. Also write three readable documents the candidate can open directly:
   `job-search/NEXT.md`, `job-search/pipeline.md` and
   `job-search/leverage.md`.
7. When an application becomes ready the script writes the CV and the
   covering note as Word files and prints a DOCUMENT line for each. Send
   those files to the candidate. Word files are not kept in the save; run
   `pipeline export <slug>` to make them again at any time.
8. Confirm every write succeeded. If one failed, say so plainly in the reply.

An ARCHIVED line means a role that closed more than a month ago has left the
everyday save. Its documents stay in the Project in its own
`job-search/opp-<slug>.txt`, and it is listed in `archive/index.md`.

The dashboard is only as fresh as the last close. It updates after every
scheduled check and after everything the candidate tells Claude. It does not
update when something changes outside a conversation with Claude.

### The CV

Save files hold text only. At setup, save a faithful text copy of the CV as
`profile/cv/cv-master.md`. Ask the candidate to keep their original file and
to add it to the Project so it is there when a formatted version is needed.

## C. Nowhere to keep it

In a plain conversation with no Project and no folder, nothing survives the
conversation.

- The try-one-job skill works fully here. It needs no storage.
- For anything else, say: "To keep your search going between conversations I
  need somewhere to keep it: a Project in Claude, or a folder on your
  computer." Offer to carry on for this conversation only, and say at the end
  that nothing was kept.

## Scheduled runs

A scheduled run starts a fresh session. At its start, open the workspace as
above. If neither a Project nor a folder can be reached, write nothing and
report in one sentence that the saved search could not be reached. Do not
start a new search from a scheduled run. Close with
`pipeline close --scheduled "<what happened>"`, so the dashboard and the
doctor can show the candidate that the automatic check is reaching their
search.
