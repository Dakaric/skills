---
name: vault-ingest
description: Verarbeitet Rohdokumente aus Christians Staging-Ordner /Users/chris/Documents/AI/Obsidian/raw/ (PDF, DOCX, MD, TXT, HTML, Transkripte) und integriert das Wissen vollautomatisch an der passenden Stelle in den Obsidian Vault chris_brain/. Parst jede Datei, gleicht per chris-brain semantisch gegen bestehende Notizen ab (Dubletten vermeiden), schreibt neu oder hängt an, verschiebt verarbeitete Dateien nach raw/_processed/ und liefert am Ende einen Report. Optional kann Christian ein Ziel-Projekt angeben ("das ergänzt Projekt X") — dann wird das Wissen dem Projekt zugeordnet und die Projekt-Notiz bei Bedarf angelegt. Nutze diesen Skill, wenn Christian "verarbeite den raw-Ordner", "integrier die raw Docs ins Vault", "schau dir raw an", "ingest raw", "räum raw ins Vault ein", "verarbeite die Dokumente in raw" oder Ähnliches sagt, oder direkt nachdem eine Datei in raw/ abgelegt wurde.
---

# Vault Ingest

Pipeline: Roh-Dokument aus `raw/` → parsen → semantisch gegen Vault abgleichen → automatisch an der richtigen Stelle in `chris_brain/` integrieren → Roh-Datei nach `_processed/` archivieren.

## Pfade

```
Staging:   /Users/chris/Documents/AI/Obsidian/raw/
Archiv:    /Users/chris/Documents/AI/Obsidian/raw/_processed/
Vault:     /Users/chris/Documents/AI/Obsidian/chris_brain/
```

## Modus

**Vollautomatisch.** Christian integriert ohne Einzel-Bestätigung. Nicht für jede Datei nachfragen — nur am Ende einen Report liefern. Ausnahme: Bei echter Ambiguität oder sensiblem/geringwertigem Inhalt → in `01 Inbox/Brain Dump.md` ablegen statt wild zu raten, und im Report flaggen.

## Optional: Ziel-Projekt

Christian kann ein Dokument explizit einem Projekt zuweisen — entweder beim Aufruf („verarbeite raw, das Transkript ergänzt das Jarvis-Dashboard") oder per Frontmatter `projekt: <Name>` in der Roh-Datei selbst.

So damit umgehen:
1. **Projekt finden:** `ls "02 Projekte/"` und matchen. Den Projekt-**Inhalt** prüfen, nicht nur den Dateinamen — ein Substring-Treffer ist kein sicherer Match. **Guardrail (wichtig):** Wenn der Match nur auf einem Teilwort beruht, mehrdeutig ist, oder der gemeinte Begriff inhaltlich nicht zur gefundenen Notiz passt → **kurz nachfragen statt raten** (auch im Auto-Modus). Lieber eine Rückfrage als das Wissen am falschen Projekt. Beispiel-Miss: „Jarvis-OS" ≠ `Hermes Dashboard JARVIS Cockpit.md` (altes Hermes-Ding), gemeint war das eigenständige Claude-Code-`Jarvis OS`. Im Zweifel zusätzlich `chris-brain` befragen. Kein Duplikat anlegen, wenn ein passendes Projekt existiert.
2. **Projekt fehlt wirklich?** Neue Projekt-Notiz unter `02 Projekte/<Name>.md` aus dem Template anlegen (siehe `vault-capture`), Status `aktiv`.
3. **Einordnen je nach Inhaltstyp:**
   - **Projektspezifisch** (Meeting-Notes, Spec, Entscheidung) → direkt in der Projekt-Notiz im passenden Abschnitt anhängen.
   - **Konzeptuell/Referenz** (Transkript, Artikel, Whitepaper) → volles Wissen als **Ressourcen-Notiz** (`04 Ressourcen/...`), und in der Projekt-Notiz unter `## Referenzen` einen Wikilink + 3-5 Kern-Takeaways mit Projektbezug ergänzen. So bleibt die Projekt-Notiz schlank und die Quelle wiederfindbar.

## Workflow

1. **Scannen:** `raw/` auf Top-Level listen. Ignorieren: `_processed/`, `_README.md`, versteckte Dateien (`.DS_Store` etc.). Gibt es nichts zu verarbeiten → kurz melden und stoppen.

2. **Pro Datei: zu Markdown-Text konvertieren**
   - `.md` / `.txt` → direkt mit Read lesen.
   - `.pdf` / `.docx` / `.doc` / `.odt` / `.rtf` / `.xlsx` / `.xls` / `.html` → über den Skill **`firecrawl-parse`** nach Markdown parsen.
   - Unbekannter Typ → in den Report als „übersprungen" und Datei in `raw/` belassen.

3. **Verstehen:** Kerninhalt, Themen, Entitäten, Datum/Quelle erfassen. Bei Transkripten/Artikeln: worum geht es, welches projekt-/ressourcen-relevante Wissen steckt drin.

4. **Semantisch abgleichen:** Über die `chris-brain` MCP-Tools (`vault_search`, ggf. `vault_related`) den Vault nach verwandten Notizen durchsuchen.
   - Treffer → an bestehende Notiz **anhängen** (passender Abschnitt).
   - Inhalt existiert bereits (Dublette) → **nicht** doppelt schreiben, im Report als „bereits vorhanden, übersprungen" vermerken, Datei trotzdem nach `_processed/`.
   - Kein Treffer → **neue Notiz** anlegen.

5. **Einsortieren (Routing):** Ist ein **Ziel-Projekt** vorgegeben → Abschnitt „Optional: Ziel-Projekt" anwenden. Sonst die Routing-Logik aus dem Skill **`vault-capture`** anwenden:
   - `00 Kontext/` — Identität, ICP, Angebot, Schreibstil, Branding
   - `02 Projekte/` — vorher `ls "02 Projekte/"`, an bestehende Projekt-Notiz anhängen oder neue anlegen
   - `03 Bereiche/` — laufende Verantwortungsbereiche
   - `04 Ressourcen/` — technisches Wissen, Tools, Frameworks, Tutorials, News (KI & AI / Wissenschaft / 3D Druck). **Default für Transkripte/Artikel ohne klaren Projektbezug.**
   - `05 Daily Notes/` — nur wenn es um Tageslog/Session geht
   - `01 Inbox/Brain Dump.md` — bei Unsicherheit

6. **Schreiben:** Edit (anhängen) bzw. Write (neue Notiz). Regeln unten beachten.

7. **Archivieren:** Roh-Datei nach `raw/_processed/` verschieben, mit Datumspräfix:
   ```bash
   mv "raw/<datei>" "raw/_processed/$(date +%Y-%m-%d)_<datei>"
   ```

8. **Report:** Tabelle/Liste am Ende — pro Datei: Zielnotiz, neu vs. angehängt vs. übersprungen, ggf. gesetzte Wikilinks.

## Regeln beim Schreiben (Christians Vault-Konventionen)

- **Stil** (`00 Kontext/Schreibstil.md`): „KI" statt „AI", keine Emojis im professionellen Kontext, „preisintensiv"/„günstig" statt „teuer"/„billig", keine KI-typischen Gedankenstriche als Stilmittel, Backticks für Code/Pfade/Begriffe.
- **Frontmatter** bei neuen Notizen:
  ```yaml
  ---
  tags: [projekt|bereich|ressource|kontext|inbox]
  status: aktiv          # nur bei Projekten
  erstellt: YYYY-MM-DD
  quelle: <Original-Dateiname oder URL>
  ---
  ```
- **Quelle vermerken:** Bei eingespeistem Wissen Herkunft notieren (Dateiname, ggf. URL/Autor), damit später nachvollziehbar.
- **Nie überschreiben:** Bestehende Inhalte nur anhängen oder in passenden Abschnitt einfügen.
- **Wikilinks** `[[Notiz]]` bei echtem thematischem Bezug setzen — zur Navigation, nicht zur Graph-Deko.

## Beispiel

**Situation:** In `raw/` liegen `transkript_de.md` (YouTube-Transkript zu Agentic OS) und `whitepaper-rag.pdf`. Christian: *"verarbeite den raw-Ordner."*

**Ablauf:**
1. Beide Dateien gefunden, `_README.md` ignoriert.
2. `transkript_de.md` direkt gelesen; `whitepaper-rag.pdf` via `firecrawl-parse` zu Markdown.
3. `chris-brain`-Suche: „Agentic OS" → kein direkter Treffer; „RAG" → Treffer in `04 Ressourcen/KI & AI/RAG.md`.
4. Transkript → neue Notiz `04 Ressourcen/KI & AI/Agentic OS.md` (Frontmatter, `quelle:` = YouTube-Link), Wikilink zu `[[Memory Systeme]]` wenn vorhanden.
5. Whitepaper → an `04 Ressourcen/KI & AI/RAG.md` unter `## Quellen` angehängt.
6. Beide nach `raw/_processed/2026-05-27_*` verschoben.
7. Report: 1 neue Notiz, 1 angehängt, 0 Dubletten.
