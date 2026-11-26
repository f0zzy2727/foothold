# Security

## Reporting a problem

Please do not open a public issue for a security problem. Use GitHub's
private reporting on this repository: the Security tab, then "Report a
vulnerability". Say what you did, what happened and what you expected.

Never include a real CV, a real advert with personal details, or a saved
search in a report. Reproduce the problem with the invented sample in
`tests/fixtures/` where you can.

## What the plugin does and does not do

- It has no server and no accounts. It makes no network requests of its own.
  Web searches and page reads are done by Claude, under the person's own
  Claude settings.
- Its one script uses the Python standard library only, and reads and writes
  files inside the search's own folder. It refuses to restore a save that
  names a path outside that folder.
- Adverts, web pages and uploaded files are treated as untrusted text. The
  skills tell Claude never to act on words in them addressed to an AI, the
  script scans each saved advert for the common forms, and a verdict cannot
  be issued until the person has been told. The scan catches common
  phrasings only. It is a tripwire, not a guarantee.
- It never sends anything to anyone. Applications, messages and follow-ups
  are sent by the person.

## Known limits

- The honesty checks compare an application with the person's own CV and
  evidence. They cannot detect an invented claim written in ordinary words,
  and they cannot tell whether the person's own statements are true.
