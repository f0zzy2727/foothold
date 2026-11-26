# Facts

Things learned about how Foothold behaves in the Claude app that the code
does not show. Each entry says how it was learned and when. An entry marked
"observed" was seen once and is not documented by Anthropic: treat it as
advisory and check it again before building on it.

Rules live in `AGENTS.md`. This file holds facts only.

## Project documents

1. **Size decides how a project document comes back.** Measured in the Claude
   app on 26 November 2026. A project document of about 120,000 characters
   came back as text in the tool reply, which Claude must copy to disk by
   hand. One of about 300,000 characters came back as a file, byte for byte.
   The threshold is somewhere between the two. A second reading the same day,
   with plugin 0.7.0 on Opus 5.5: a test file of about 49,000 characters also
   came back as text, so the plugin's own storage check could not run and
   Claude compared a few lines by hand instead.
2. **Do not pad a save to cross that threshold.** Project documents are part
   of the project's knowledge, so padding would pollute every chat in the
   project.
3. **A write can be verified cheaply.** Observed on 26 November 2026: the
   reply to a project write carried a `version` equal to the sha256 of the
   content. This is not documented, so the plugin treats it as advisory. Each
   `SAVE` line prints the file's sha256 so the two can be compared.

## Folders attached to a project

4. **An attached folder did not mount.** In the Claude app session on 26
   November 2026 the folder attached to the project never mounted, and the
   device tools refused it. Folder support in the plugin is therefore
   instructions only (an in-tray and an out-tray) and is untested. The saved
   search stays in the project's documents.

## The repository

5. **Git does not keep empty folders.** Two tests failed on a fresh clone of
   0.7.0 for this reason. The script and the tests now create the folders
   they need.
6. **The Claude app session could not push.** On 26 November 2026 the Claude
   GitHub app was not installed on this repository, so work done in the app
   left as a patch file.

## Testing

7. **Old instructions compete.** A `CLAUDE.md` describing an earlier workflow
   sits in J's old "Paul Resume" folder. Never test the plugin with that
   folder attached.
8. **The browser extension cannot open the Plugins page.** Found on 26
   November 2026: Claude in Chrome is barred from the Claude app's Settings,
   Customize and Plugins pages. An agent driving the browser cannot add the
   plugin or confirm its version there. Step 1 of `SETUP.md` has to be done
   by a person.

## The two pages

9. **The "how it works" page began life outside the repository.** Until 26
   November 2026 its only copy was a published page in J's Claude account.
   Its source is now `docs/how-it-works.html`. The dashboard's source is
   `plugins/job-search/skills/engine/references/dashboard-template.html`.
