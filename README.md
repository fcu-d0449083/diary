# Henry & Natcha Diary

Encrypted static LINE diary viewer designed for GitHub Pages.

## What is safe to commit

- `index.html`
- `.nojekyll`
- `.gitignore`
- `README.md`
- `CODEX_TASK.md`
- `SECURITY.md`
- `tools/verify_bundle.py`
- `LINE_ZH_TO_THAI_RULES.md`

## Security model

The LINE chat payload embedded in `index.html` is encrypted with AES-256-GCM. The key is derived in the browser using PBKDF2-HMAC-SHA256 with 600,000 iterations, a random salt, and a random IV. The password is not stored in source code.

The site decrypts the bundled payload in the browser after the visitor enters the password. Decrypted messages remain in page memory. To keep refreshes convenient, the password is held in this tab’s `sessionStorage` and the same tab auto-unlocks after refresh; closing the tab normally clears it. This is browser-side plaintext storage, so scripts running on this site can read it. The page does not offer a file upload/import control or an in-page password-change control. On mobile, duplicate previous/next-day controls are available after the conversation so users can move between days without scrolling back to the top.

To preserve encrypted updates created by an earlier version, the page may restore an existing encrypted update from this browser's IndexedDB after unlock. This compatibility read does not create, modify, or upload updates. Clearing site data removes that browser-local copy.

## Published site

The public GitHub Pages site is <https://fcu-d0449083.github.io/diary/>. Anyone can open the site and download the public repository, including its encrypted ciphertext. The password gate controls client-side decryption; it does not make the site or source private. Use a long, unique password because public ciphertext allows offline guesses.

## Important

Do **not** commit original LINE TXT exports, unencrypted diary HTML, private notes, or any file containing the decryption password. `.gitignore` helps prevent accidental commits.

## Repository

Target repository: `fcu-d0449083/diary`
