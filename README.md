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

The LINE chat payload embedded in `index.html` is **not plaintext**. It is encrypted with:

- AES-256-GCM
- PBKDF2-HMAC-SHA256 key derivation
- 600,000 PBKDF2 iterations
- random salt
- random IV

The browser derives the decryption key locally from the visitor-entered password. The password itself is not stored in plaintext in `index.html`.

## Published site

The public GitHub Pages site is <https://fcu-d0449083.github.io/diary/>. Anyone can open the site and download the public repository, including its encrypted ciphertext. The password gate protects access to decrypted diary content; it does not restrict access to the website or source files. Use a long, unique password because public ciphertext permits offline password guesses.

## Import a Chinese LINE export

After unlocking, choose **匯入中文 LINE TXT** (or the Thai label) to load a UTF-8 LINE export. The browser preserves chat text, converts the supported LINE system labels and morning/afternoon times, and replaces existing entries for dates in the imported file. Other dates remain in the diary.

The import is processed locally. The full updated diary is encrypted again with AES-256-GCM and a fresh random salt and IV before it is saved in this browser's IndexedDB. Plaintext is held in memory only while the page is open; the TXT is not uploaded. Updates stay in this browser and do not change the published website or synchronize to other devices. Clearing this site's browser data removes the saved update.

The converter follows [`LINE_ZH_TO_THAI_RULES.md`](LINE_ZH_TO_THAI_RULES.md). It does not translate or edit ordinary chat text. Matching dates are replaced as a group to prevent importing the same export twice from duplicating messages.

## Important

Do **not** commit the original LINE TXT exports, the unencrypted diary HTML, or private notes. `.gitignore` is included to reduce accidental commits.

## Repository

Target repository: `fcu-d0449083/diary`

