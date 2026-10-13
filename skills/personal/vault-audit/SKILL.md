---
name: vault-audit
description: Prüft Christians Vault chris_brain auf Lücken zwischen Daily Notes und Projekten, Rotting, Widersprüche und tote Links, arbeitet Unstrittiges selbst ein und sammelt offene Fragen. Hat einen Interview-Modus, der diese Fragen einzeln mit Christian klärt. Nutze, wenn "vault audit", "audit das vault", "räum das vault auf", "Vault-Interview", "offene Vault-Fragen" fällt oder die Sonntags-Automation ihn startet.
---

# Vault-Audit

Vault: `/Users/chris/Documents/AI/Obsidian/chris_brain`. Heimat aller Ergebnisse: `03 Bereiche/Vault-Pflege/`.
`08 Privat/` wird nie gelesen. Texte für Christian folgen dem Skill `vermenschlichen`: echte Umlaute, kein Gedankenstrich als Einschub.

Zwei Modi: **Audit** (Standard, läuft headless sonntags 16:00 über Orca) und **Interview** (Argument `interview`, nur mit Christian im Gespräch).

## Audit

1. **Struktur messen:** `python3 -I <skill-dir>/scripts/vault_structure.py <vault>` liefert JSON mit echten Waisen, toten Links, aktiven Notizen ohne Änderung seit 45 Tagen. Handoffs, `09 Transcripts/Raw/` und `06 Archiv/` sind erwartete Waisen und zählen nur als Zahl.
2. **Inhalt prüfen**, zwei `sonnet`-Subagents parallel, beide read-only:
   - *Daily-Abgleich:* Daily Notes seit dem letzten Audit (Datum aus dem jüngsten Bericht in `Audits/`, sonst 30 Tage) gegen `02 Projekte`, `03 Bereiche`, `04 Ressourcen`, `00 Kontext`. Meldet nur Lücken: Kernaussage, Fundstelle, Zielnotiz.
   - *Widersprüche und Rotting:* `00 Kontext`, `03 Bereiche`, Projekt-Hauptnotizen (keine Handoff-Ordner), Vault-`CLAUDE.md`/`AGENTS.md` gegen die letzten 14 Dailies.
3. **Unstrittiges selbst erledigen** (Standing-Freigabe für Vault-Pflege):
   - fehlende Fakten aus Dailies in die Zielnotiz unter `## Notizen` eintragen, mit `(Quelle: [[JJJJ-MM-TT]])`
   - in Dailies den Projektnamen zum Wikilink machen, wo eindeutig
   - tote Links reparieren, wenn genau ein Ziel passt
4. **Nie selbst:** löschen, verschieben, archivieren, `status` ändern, einen Widerspruch auflösen, vorhandenen Inhalt überschreiben. Daraus wird eine Frage (Schritt 5).
5. **Fragen anhängen** an `03 Bereiche/Vault-Pflege/Offene Fragen.md` im Format unten. Vorher prüfen, ob dieselbe Frage schon offen ist. Höchstens 10 neue pro Lauf, die mit dem größten Kontextgewinn zuerst.
6. **Bericht** nach `03 Bereiche/Vault-Pflege/Audits/JJJJ-MM-TT.md` (Vorlage unten) und als Zeile in die Liste in `Vault-Pflege.md` eintragen, damit er im Graph hängt.
7. **Abschluss:** Kurzfassung als Ausgabe, eine Zeile in die Daily Note des Tages (Skill `daily-notes`) mit Link auf den Bericht.

## Interview

1. `Offene Fragen.md` lesen, alle Blöcke mit Status `offen`, älteste zuerst.
2. Ansage: wie viele Fragen offen sind, ungefähr wie lange es dauert. Christian darf jederzeit „stopp" oder „überspringen" sagen.
3. Pro Frage: kurz den Befund nennen (ein Satz), dann die Frage. Eine Frage pro Turn. Per Stimme kurz halten, kein Markdown vorlesen.
4. Antwort sofort in die Zielnotiz einarbeiten (an passender Stelle, nicht nur unten anhängen), Block auf `beantwortet` setzen, `**Antwort:**` mit einem Satz und dem Datum füllen. Bei „egal"/„weg damit" Status `verworfen`.
5. Am Ende: was eingearbeitet wurde, was offen bleibt.

## Format `Offene Fragen.md`

Vertrag mit Jarvis OS, Kopfzeile exakt so, ein Block pro Frage:

```markdown
## F-2026-10-13-01 · offen
**Frage:** Ist das Projekt X abgeschlossen oder nur pausiert?
**Befund:** Seit 140 Tagen unverändert, letzte Erwähnung [[2026-05-24]].
**Ziel:** [[Projekt X]]
**Antwort:**
```

Status ist `offen`, `beantwortet` oder `verworfen`. Die ID wird nie neu vergeben.

## Vorlage Bericht

```markdown
---
tags: [vault-pflege, audit]
date: JJJJ-MM-TT
---
# Vault-Audit JJJJ-MM-TT

Zurück zu [[Vault-Pflege]]

## Zahlen
Notizen, echte Waisen, tote Links, liegengebliebene aktive Notizen, jeweils mit Veränderung zum letzten Audit.

## Selbst erledigt
Je Zeile: was, wo ([[Notiz]]).

## Neue Fragen
Liste der IDs mit einer Zeile Inhalt.

## Liegt außerhalb des Vaults
Befunde, die Code oder Jobs betreffen (z.B. Jarvis, LaunchAgents). Nur melden.
```
