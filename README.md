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

The site decrypts the bundled payload in the browser after the visitor enters the password. Decrypted messages remain in page memory. To keep refreshes convenient, the password is held in this tab’s `sessionStorage` and the same tab auto-unlocks after refresh; closing the tab normally clears it. This is browser-side plaintext storage, so scripts running on this site can read it. The page does not offer a file upload/import control or an in-page password-change control. On mobile, duplicate previous/next-day controls appear below the conversation; selecting one switches the date and smoothly returns to the conversation header.

To preserve encrypted updates created by an earlier version, the page may restore an existing encrypted update from this browser's IndexedDB after unlock. This compatibility read does not create, modify, or upload updates. Clearing site data removes that browser-local copy.

## On-demand Thai translation

When the selected date contains Thai messages, the conversation header offers a translation button. It asks for confirmation before sending anything. After confirmation, it sends only that date's Thai message bodies to the free ArgosOpenTech public demo at <https://translate.argosopentech.com> for Traditional Chinese translation. Speaker and timestamp fields are excluded, but names or personal details written inside a message body are included. The service handles submitted text under its own policies; avoid using the button if you do not want those messages sent to that service. Translations stay only in page memory and are not written to the public source, browser storage, or the encrypted diary. The public demo can be unavailable or rate-limited.

## Published site

The public GitHub Pages site is <https://fcu-d0449083.github.io/diary/>. Anyone can open the site and download the public repository, including its encrypted ciphertext. The password gate controls client-side decryption; it does not make the site or source private. Use a long, unique password because public ciphertext allows offline guesses.

## Important

Do **not** commit original LINE TXT exports, unencrypted diary HTML, private notes, or any file containing the decryption password. `.gitignore` helps prevent accidental commits.

## Repository

Target repository: `fcu-d0449083/diary`

