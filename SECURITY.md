# Security notes

## Current protection

The chat payload is encrypted client-side using AES-256-GCM. The encryption key is derived from the password via PBKDF2-HMAC-SHA256 with 600,000 iterations.

The deployed static site contains:

- UI source code
- salt and IV (these are not secrets)
- PBKDF2 iteration count
- encrypted chat ciphertext

The repository and GitHub Pages site are public so Pages can run on the current plan. Anyone can visit the site or download the ciphertext and source code. The password gate controls client-side decryption only; it does not make the website private. Use a long, unique password to make offline guessing impractical.

## Uploaded TXT files

The TXT importer runs entirely in the browser after the password gate opens. It does not send the selected file to a server. Imported text is parsed in memory, and the merged diary is encrypted with AES-256-GCM using the entered password, a new random salt, a new random IV, and 600,000 PBKDF2-HMAC-SHA256 iterations before it is written to IndexedDB. IndexedDB stores ciphertext only. The password is retained in page memory for the current session so the app can save later imports.

The encrypted update is local to that browser profile and origin. It is not committed, uploaded, or synchronized, and clearing site data deletes it. A static GitHub Pages site cannot update its published bundled ciphertext from a browser upload; distributing an update to other devices requires a separate encrypted export/import or a new deployment workflow.

The importer replaces all records on dates present in an uploaded export and preserves other dates. It keeps user-authored message bodies unchanged and only applies the documented system-text conversions. Imports require a UTF-8 LINE text export and are limited to 25 MiB.

It does **not** need to contain:

- plaintext chat exports
- plaintext decryption password

## Threat model

A public static site cannot prevent attackers from downloading the ciphertext and attempting offline password guesses. Therefore password strength matters. A long, unique password is substantially safer than a short PIN.

AES-GCM authentication ensures an incorrect key/password cannot silently produce a valid diary payload.

## Operational rules

- Never place the password in JavaScript, README, commit messages, GitHub Actions logs, issues, or repository secrets unless a future deployment architecture explicitly requires it.
- Never commit raw LINE TXT files.
- Re-encryption should use a fresh random salt and IV.
- Never store imported plaintext in localStorage, IndexedDB, logs, or generated repository files.
- Treat browser storage as encrypted but local: browser profile access and offline password guessing against ciphertext remain in scope.

