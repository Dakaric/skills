---
name: write-a-skill
description: Neue Agent-Skills mit richtiger Struktur, Progressive Disclosure und gebündelten Ressourcen erstellen. Nutze, wenn der User einen neuen Skill erstellen, schreiben oder bauen will.
---

# Writing Skills

## Prozess

1. **Requirements sammeln** - den User fragen zu:
   - Welche Aufgabe / Domain deckt der Skill ab?
   - Welche spezifischen Use Cases soll er handlen?
   - Braucht er ausführbare Scripts oder nur Instructions?
   - Etwaige Referenz-Materialien zum Einbinden?

2. **Den Skill draften** - anlegen:
   - SKILL.md mit knappen Instructions
   - Zusätzliche Referenz-Files, falls Content 500 Zeilen übersteigt
   - Utility-Scripts, falls deterministische Operationen nötig

3. **Mit dem User reviewen** - Draft präsentieren und fragen:
   - Deckt das deine Use Cases ab?
   - Fehlt was oder ist unklar?
   - Sollte eine Section detaillierter / weniger detailliert sein?

## Skill-Struktur

```
skill-name/
├── SKILL.md           # Haupt-Instructions (pflicht)
├── REFERENCE.md       # Detailierte Docs (falls nötig)
├── EXAMPLES.md        # Usage-Beispiele (falls nötig)
└── scripts/           # Utility-Scripts (falls nötig)
    └── helper.js
```

## SKILL.md Template

```md
---
name: skill-name
description: Knappe Beschreibung der Capability. Nutze, wenn [spezifische Trigger].
---

# Skill Name

## Quick Start

[Minimales lauffähiges Beispiel]

## Workflows

[Schritt-für-Schritt-Prozesse mit Checklisten für komplexere Aufgaben]

## Advanced Features

[Link auf separate Files: Siehe [REFERENCE.md](REFERENCE.md)]
```

## Anforderungen an die Description

Die Description ist **das Einzige, was dein Agent sieht**, wenn er entscheidet, welchen Skill er lädt. Sie taucht im System Prompt neben allen anderen installierten Skills auf. Dein Agent liest diese Descriptions und wählt den relevanten Skill basierend auf der Anfrage des Users.

**Ziel**: Gib deinem Agent gerade genug Info, um zu wissen:

1. Welche Capability dieser Skill bietet
2. Wann / warum er ihn triggern soll (spezifische Keywords, Kontexte, File-Typen)

**Format**:

- Max 1024 Zeichen
- Dritter Person schreiben
- Erster Satz: was er tut
- Zweiter Satz: "Nutze, wenn [spezifische Trigger]"

**Gutes Beispiel**:

```
Extrahiert Text und Tabellen aus PDF-Dateien, füllt Formulare aus, merged Dokumente. Nutze, wenn mit PDF-Dateien gearbeitet wird oder der User PDFs, Formulare oder Document-Extraction erwähnt.
```

**Schlechtes Beispiel**:

```
Hilft mit Dokumenten.
```

Das schlechte Beispiel gibt deinem Agent keine Möglichkeit, das von anderen Document-Skills zu unterscheiden.

## Wann Scripts hinzufügen

Utility-Scripts hinzufügen, wenn:

- Die Operation deterministisch ist (Validation, Formatting)
- Der gleiche Code wiederholt generiert werden würde
- Errors explizites Handling brauchen

Scripts sparen Tokens und verbessern die Zuverlässigkeit gegenüber generiertem Code.

## Wann Files splitten

In separate Files splitten, wenn:

- SKILL.md 100 Zeilen übersteigt
- Content distincte Domains hat (Finance- vs Sales-Schemas)
- Advanced Features selten gebraucht werden

## Review-Checkliste

Nach dem Draften verifizieren:

- [ ] Description enthält Trigger ("Nutze, wenn...")
- [ ] SKILL.md unter 100 Zeilen
- [ ] Keine zeit-sensitiven Infos
- [ ] Konsistente Terminologie
- [ ] Konkrete Beispiele enthalten
- [ ] References eine Ebene tief
