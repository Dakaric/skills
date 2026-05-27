---
name: youtube-transcribe
description: Erstellt aus einer YouTube-URL ein sauberes Markdown-Transkript (optional mit deutscher Übersetzung) und legt es in Christians Staging-Ordner /Users/chris/Documents/AI/Obsidian/raw/ ab, damit es danach per vault-ingest ins Vault wandern kann. Zieht vorhandene Untertitel per yt-dlp (kein eigenes Whisper-Transkribieren nötig), räumt die Caption-Überlappungen auf und gliedert den Fließtext lesbar. Nutze diesen Skill, wenn Christian eine YouTube-URL schickt und ein Transkript will, "transkribiere das Video", "mach ein Transkript", "youtube transcribe", "zieh mir das Transkript", "transkript in den raw-Ordner" oder Ähnliches sagt.
---

# YouTube Transcribe

URL rein → sauberes Markdown-Transkript in `raw/` → bereit für `vault-ingest`.

## Voraussetzungen

```bash
command -v yt-dlp || brew install yt-dlp   # ffmpeg ist meist schon da
```

## Workflow

1. **Metadaten holen:**
   ```bash
   yt-dlp --skip-download --print "%(title)s | %(duration_string)s | %(uploader)s | %(id)s" "<URL>"
   ```

2. **Untertitel listen** (welche Sprachen / ob manuell vs. auto):
   ```bash
   yt-dlp --list-subs "<URL>"
   ```
   Bevorzuge die **Originalsprache** (`<lang>-orig`, sonst `<lang>`). Manuelle Subs schlagen Auto-Captions.

3. **Untertitel als SRT ziehen** (Auto + manuell, Originalspur):
   ```bash
   cd /tmp && yt-dlp --skip-download --write-subs --write-auto-subs \
     --sub-langs "<lang>-orig,<lang>" --sub-format srt --convert-subs srt \
     -o "yt_%(id)s.%(ext)s" "<URL>"
   ```

4. **Säubern** (Indizes/Timestamps weg, Caption-Wiederholungen dedupen):
   ```bash
   python3 <skill-dir>/scripts/srt_to_md.py /tmp/yt_<id>.<lang>.srt
   ```
   Output ist ein Fließtext. Daraus ein **lesbares Markdown** machen: Absätze setzen, bei langen Videos sinnvolle Zwischenüberschriften nach Themen. Inhalt nicht umschreiben, nur formatieren.

5. **Optional übersetzen:** Ist die Originalsprache nicht Deutsch und Christian will eine Übersetzung (oder fragt explizit danach) → deutsche Übersetzung erstellen. Stil: „KI" statt „AI", Tool-/Dateinamen im Original lassen, keine Emojis.

6. **Datei schreiben** nach `/Users/chris/Documents/AI/Obsidian/raw/<slug>.md`:
   - `<slug>` = entschärfter Titel (Leerzeichen→`-`, Sonderzeichen weg).
   - Eine Datei pro Video. Aufbau siehe Template unten.

7. **Melden:** Pfad nennen und anbieten, direkt `vault-ingest` laufen zu lassen (optional mit Ziel-Projekt).

## Datei-Template

```markdown
---
tags: [transkript, youtube]
quelle: <URL>
kanal: <Uploader>
laenge: <mm:ss>
erstellt: YYYY-MM-DD
---

# <Video-Titel>

> Transkript via youtube-transcribe (yt-dlp Untertitel). Original: <Sprache>.

## Deutsche Übersetzung
<nur wenn übersetzt — sonst Abschnitt weglassen>

## Transkript (Original)
<lesbar gegliederter Fließtext>
```

## Hinweise

- **Keine Untertitel verfügbar?** Dann Audio ziehen (`yt-dlp -x --audio-format mp3`) und Christian fragen, ob lokal mit Whisper transkribiert werden soll — das ist der langsame Fallback.
- **Mehrere URLs:** nacheinander, je eine Datei.
- **Ziel-Projekt:** Wenn Christian sagt „das ergänzt Projekt X" → den Hinweis an `vault-ingest` durchreichen, dieser Skill legt nur die Roh-Datei in `raw/` ab.
