---
name: git-guardrails-claude-code
description: Claude Code Hooks einrichten, die gefährliche Git-Commands (push, reset --hard, clean, branch -D etc.) blockieren, bevor sie ausgeführt werden. Nutze, wenn der User destruktive Git-Operationen verhindern, Git-Safety-Hooks hinzufügen oder git push / reset in Claude Code blocken will.
---

# Setup Git Guardrails

Setzt einen PreToolUse Hook auf, der gefährliche Git-Commands abfängt und blockt, bevor Claude sie ausführt.

## Was geblockt wird

- `git push` (alle Varianten inklusive `--force`)
- `git reset --hard`
- `git clean -f` / `git clean -fd`
- `git branch -D`
- `git checkout .` / `git restore .`

Wenn geblockt, sieht Claude eine Message, die ihm sagt, dass er keine Autorität für diese Commands hat.

## Steps

### 1. Scope abfragen

Den User fragen: für **dieses Projekt only** (`.claude/settings.json`) oder **alle Projekte** (`~/.claude/settings.json`) installieren?

### 2. Hook-Script kopieren

Das gebündelte Script liegt unter: [scripts/block-dangerous-git.sh](scripts/block-dangerous-git.sh)

Es je nach Scope an den Zielort kopieren:

- **Project**: `.claude/hooks/block-dangerous-git.sh`
- **Global**: `~/.claude/hooks/block-dangerous-git.sh`

Mit `chmod +x` ausführbar machen.

### 3. Hook in Settings hinzufügen

Zur passenden Settings-Datei hinzufügen:

**Project** (`.claude/settings.json`):

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/block-dangerous-git.sh"
          }
        ]
      }
    ]
  }
}
```

**Global** (`~/.claude/settings.json`):

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "~/.claude/hooks/block-dangerous-git.sh"
          }
        ]
      }
    ]
  }
}
```

Wenn die Settings-Datei schon existiert, den Hook ins bestehende `hooks.PreToolUse` Array mergen - keine anderen Settings überschreiben.

### 4. Nach Customization fragen

Frag, ob der User Patterns aus der Blocked-Liste hinzufügen oder entfernen will. Das kopierte Script entsprechend editieren.

### 5. Verifizieren

Ein kurzer Test:

```bash
echo '{"tool_input":{"command":"git push origin main"}}' | <path-to-script>
```

Sollte mit Exit-Code 2 enden und eine BLOCKED Message nach stderr printen.
