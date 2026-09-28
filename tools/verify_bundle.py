from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
errors = []
if not INDEX.exists():
    errors.append("index.html is missing")
else:
    html = INDEX.read_text(encoding="utf-8", errors="replace")
    if "AES-GCM" not in html or "PBKDF2" not in html:
        errors.append("expected WebCrypto AES-GCM/PBKDF2 code not found")
    if 'data:"' not in html or 'iterations:600000' not in html.replace(" ", ""):
        errors.append("encrypted payload metadata not found")
    private_notes = ROOT / "PRIVATE_NOTES.md"
    if private_notes.exists():
        notes = private_notes.read_text(encoding="utf-8", errors="replace")
        match = re.search(r"(?im)^Current diary password:\s*\n\s*`([^`]+)`", notes)
        if match and match.group(1) in html:
            errors.append("plaintext password from local private notes appears in index.html")
    required_features = ["decryptDiary", "unlockDiary", "renderAll", "renderCalendar", "renderMessages", "renderNav", "renderSummary", "AES-GCM", "PBKDF2", "lineDiaryTabUnlock", "translateThaiBtn", "toggleThaiTranslation", "THAI_TRANSLATE_ENDPOINT='https://translate.argosopentech.com/translate'", "const approved=confirm(", "currentThaiRows()", "source:'th'", "target:'zt'", "credentials:'omit'"]
    missing = [feature for feature in required_features if feature not in html]
    if missing:
        errors.append("encrypted diary viewer code is missing: " + ", ".join(missing))
    removed_features = ["parseLineExport", "importLineTxt", "importTxtBtn", "diaryTxtFile", "changePasswordBtn", "changePasswordPanel", "exportReencryptedSite", "exportReencryptedBtn"]
    present = [feature for feature in removed_features if feature in html]
    if present:
        errors.append("removed browser controls are still present: " + ", ".join(present))

for p in ROOT.rglob("*.txt"):
    errors.append(f"raw .txt file present in deploy tree: {p.relative_to(ROOT)}")

if errors:
    print("VERIFY FAILED")
    for e in errors:
        print("-", e)
    sys.exit(1)

print("VERIFY OK")
print("- encrypted index.html found")
print("- plaintext password not present in index.html")
print("- no .txt chat exports in deployment tree")

