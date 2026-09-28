# Codex task: maintain encrypted diary deployment

Target GitHub repository: `fcu-d0449083/diary`.

## Deployment status

The repository is Public and GitHub Pages is published from `main` at `/` because the current plan does not permit Pages from a private repository. Public site: <https://fcu-d0449083.github.io/diary/>. Visitors can open the site and download encrypted ciphertext; the password protects diary decryption, not website access.

## Goal

Maintain the encrypted static diary website without committing plaintext LINE chat content. The web page provides password-gated, client-side decryption and diary viewing. It does not provide TXT upload/import or an in-page password-change control. For convenience, the current tab keeps the password in `sessionStorage` and auto-unlocks after refresh; this is plaintext browser storage accessible to scripts running on the site. An optional Thai-to-Traditional-Chinese control sends only the selected date's Thai message text to a free external demo after an explicit confirmation; returned translations remain in page memory.

## Required steps for deployment changes

1. Inspect the working tree and verify that only safe deployment files are included. Update relevant Markdown documentation.
2. Run `python tools/verify_bundle.py`; do not proceed if verification fails.
3. Publish approved changes to the repository default branch.
4. Keep GitHub Pages configured to publish from the default branch root.
5. After publishing, verify the Pages URL loads the password screen and that a wrong password does not reveal the diary. Confirm the upload and in-page password-change controls are absent.
6. Report the Pages URL and repository visibility.

## Privacy requirements

Never commit any of the following:

- original LINE `.txt` exports
- unencrypted diary HTML (`LINE_Diary_Natcha.html`)
- `PRIVATE_NOTES.md`
- any file containing the decryption password in plaintext

The public repository may contain JavaScript/CSS and encrypted ciphertext, but not plaintext chat data or the password.

## Preserve the diary viewer

Keep the calendar heatmap, date navigation (including bottom mobile controls that return to the conversation header after changing dates), Chinese/Thai interface toggle, encrypted password gate, on-demand Thai translation with a clear data-transfer confirmation, and client-side decryption behavior. Do not add file import/upload or in-page password rotation unless the user requests those features again.

