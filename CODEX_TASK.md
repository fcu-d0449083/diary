# Codex task: update and deploy encrypted diary

Target GitHub repository:

`fcu-d0449083/diary`

## Deployment status

The repository is Public and GitHub Pages is published from `main` at `/` because the current plan does not permit Pages from a private repository. Public site: <https://fcu-d0449083.github.io/diary/>. Visitors can open the site and download the encrypted ciphertext; the password protects diary decryption, not website access. Do not use a short or reused password.

## Goal

Deploy the existing encrypted static diary website from this folder to GitHub Pages without exposing plaintext LINE chat content.

Add a browser-only import feature for UTF-8 Chinese LINE TXT exports. Follow `LINE_ZH_TO_THAI_RULES.md`: keep ordinary chat text byte-for-byte unchanged, convert supported system text and AM/PM times, and report conversion failures. Merge imported dates by replacing those days while keeping other dates. Re-encrypt the complete updated diary with the entered password and fresh random salt/IV before storing it locally in the browser. Do not upload raw TXT or plaintext messages. Document that static hosting cannot publish a browser import or synchronize it to another device.

## Required steps

1. Inspect the working tree and verify that only safe deployment files are staged. Update the relevant Markdown documentation for import behavior and security.
2. Run:

   ```bash
   python tools/verify_bundle.py
   ```

   Do not proceed if verification fails.
3. Commit the deployment files to the repository's default branch.
4. Keep the repository **Private initially**.
5. Configure GitHub Pages to publish from the default branch root (`/`).
6. If GitHub's current plan does not permit Pages from this private repository, the user has authorized changing `fcu-d0449083/diary` to **Public** solely so GitHub Pages can publish it. This condition was met; the repository is now public.
7. After publishing, verify the Pages URL loads the password screen on mobile Safari/desktop and that a wrong password does not reveal the diary. Verify the import feature keeps TXT contents local and persists only encrypted updates.
8. Report the final Pages URL, repository visibility, and any local-only import limits.

## Privacy requirements

Never commit any of the following:

- original LINE `.txt` exports
- unencrypted diary HTML (`LINE_Diary_Natcha.html`)
- `PRIVATE_NOTES.md`
- any file containing the decryption password in plaintext

If the repository is made Public, this rule is especially important. The public repository may contain JavaScript/CSS and encrypted ciphertext, but not plaintext chat data or the password.

## Do not redesign unless necessary

Preserve the current diary UI and behavior:

- calendar heatmap
- click date to open that day's conversation
- Simplified Chinese / Thai interface toggle
- encrypted password gate
- client-side decryption only

Only make deployment compatibility fixes if required.

The import feature is an explicitly requested addition. Preserve the existing calendar, date navigation, language toggle, password gate, and client-side decryption behavior.

