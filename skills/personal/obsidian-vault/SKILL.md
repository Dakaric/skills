---
name: obsidian-vault
description: Notes im Obsidian Vault suchen, anlegen und managen, mit Wikilinks und Index-Notes. Nutze, wenn der User Notes in Obsidian finden, anlegen oder organisieren will.
---

# Obsidian Vault

## Vault-Location

`/mnt/d/Obsidian Vault/AI Research/`

Größtenteils flach im Root-Level.

## Naming-Konventionen

- **Index-Notes**: aggregieren verwandte Themen (z.B. `Ralph Wiggum Index.md`, `Skills Index.md`, `RAG Index.md`)
- **Title Case** für alle Note-Namen
- Keine Ordner zur Organisation - stattdessen Links und Index-Notes nutzen

## Linking

- Obsidian `[[wikilinks]]` Syntax nutzen: `[[Note Title]]`
- Notes linken auf Dependencies / verwandte Notes am unteren Ende
- Index-Notes sind nur Listen aus `[[wikilinks]]`

## Workflows

### Notes suchen

```bash
# Search by filename
find "/mnt/d/Obsidian Vault/AI Research/" -name "*.md" | grep -i "keyword"

# Search by content
grep -rl "keyword" "/mnt/d/Obsidian Vault/AI Research/" --include="*.md"
```

Oder Grep- / Glob-Tools direkt auf dem Vault-Pfad nutzen.

### Eine neue Note anlegen

1. **Title Case** für den Filename nutzen
2. Content als Lern-Einheit schreiben (gemäß Vault-Regeln)
3. `[[wikilinks]]` zu verwandten Notes am unteren Ende hinzufügen
4. Falls Teil einer nummerierten Sequenz, das hierarchische Nummerierungs-Schema nutzen

### Verwandte Notes finden

`[[Note Title]]` über den Vault suchen, um Backlinks zu finden:

```bash
grep -rl "\\[\\[Note Title\\]\\]" "/mnt/d/Obsidian Vault/AI Research/"
```

### Index-Notes finden

```bash
find "/mnt/d/Obsidian Vault/AI Research/" -name "*Index*"
```
