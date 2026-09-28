# Security notes

## Current protection

The chat payload is encrypted client-side using AES-256-GCM. The encryption key is derived from the password via PBKDF2-HMAC-SHA256 with 600,000 iterations.

The deployed static site contains UI source code, public salt and IV, the iteration count, and encrypted chat ciphertext. The repository and GitHub Pages site are public so Pages can run on the current plan. Anyone can visit the site or download the ciphertext and source code. The password gate controls client-side decryption only; it does not make the website private. Use a long, unique password to make offline guessing impractical.

## Browser behavior

The page has no TXT upload/import control and no in-page password-change control. It decrypts the bundled ciphertext locally and holds decrypted diary content in memory while the page is open. The password is stored as plaintext in this tab’s `sessionStorage` so the same tab auto-unlocks after refresh; a newly opened tab does not share it, and closing the tab normally clears it. Any script executing on this site can read the stored password. The site does not persist a plaintext diary copy.

For compatibility, the page may read a previously saved encrypted diary update from this browser's IndexedDB after unlocking. It does not write new updates. This browser-local ciphertext is not uploaded or synchronized; clearing the site's browser data removes it.

## Threat model

A public static site cannot prevent attackers from downloading the ciphertext and attempting offline password guesses. Therefore password strength matters. A long, unique password is substantially safer than a short PIN. AES-GCM authentication ensures an incorrect password cannot silently produce a valid diary payload.

## Operational rules

- Never place the password in JavaScript, README, commit messages, GitHub Actions logs, issues, or repository secrets unless a future deployment architecture explicitly requires it.
- Never commit raw LINE TXT files, plaintext diary exports, or private notes.
- Any future data encryption must use a fresh random salt and IV.
- Treat browser storage as local to the browser profile; anyone with access to that profile can access its stored data.
