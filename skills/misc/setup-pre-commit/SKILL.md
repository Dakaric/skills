---
name: setup-pre-commit
description: Husky Pre-Commit Hooks mit lint-staged (Prettier), Type Checking und Tests im aktuellen Repo aufsetzen. Nutze, wenn der User Pre-Commit Hooks hinzufügen, Husky aufsetzen, lint-staged konfigurieren oder Commit-Time Formatting / Typechecking / Testing hinzufügen will.
---

# Setup Pre-Commit Hooks

## Was hier aufgesetzt wird

- **Husky** Pre-Commit Hook
- **lint-staged** läuft Prettier auf alle staged Files
- **Prettier** Config (falls fehlt)
- **typecheck** und **test** Scripts im Pre-Commit Hook

## Steps

### 1. Package Manager erkennen

Prüf auf `package-lock.json` (npm), `pnpm-lock.yaml` (pnpm), `yarn.lock` (yarn), `bun.lockb` (bun). Nutz den vorhandenen. Default zu npm, wenn unklar.

### 2. Dependencies installieren

Als devDependencies installieren:

```
husky lint-staged prettier
```

### 3. Husky initialisieren

```bash
npx husky init
```

Das erstellt das `.husky/` Dir und fügt `prepare: "husky"` zur package.json hinzu.

### 4. `.husky/pre-commit` anlegen

Dieses File schreiben (kein Shebang nötig bei Husky v9+):

```
npx lint-staged
npm run typecheck
npm run test
```

**Anpassen**: `npm` durch den erkannten Package Manager ersetzen. Wenn das Repo kein `typecheck` oder `test` Script in package.json hat, diese Zeilen weglassen und dem User sagen.

### 5. `.lintstagedrc` anlegen

```json
{
  "*": "prettier --ignore-unknown --write"
}
```

### 6. `.prettierrc` anlegen (falls fehlt)

Nur anlegen, wenn keine Prettier-Config existiert. Diese Defaults nutzen:

```json
{
  "useTabs": false,
  "tabWidth": 2,
  "printWidth": 80,
  "singleQuote": false,
  "trailingComma": "es5",
  "semi": true,
  "arrowParens": "always"
}
```

### 7. Verifizieren

- [ ] `.husky/pre-commit` existiert und ist ausführbar
- [ ] `.lintstagedrc` existiert
- [ ] `prepare` Script in package.json ist `"husky"`
- [ ] `prettier` Config existiert
- [ ] `npx lint-staged` laufen lassen zum Verifizieren

### 8. Committen

Alle changed / created Files stagen und committen mit Message: `Add pre-commit hooks (husky + lint-staged + prettier)`

Das läuft durch die neuen Pre-Commit Hooks - ein guter Smoke-Test, dass alles funktioniert.

## Notes

- Husky v9+ braucht keine Shebangs in Hook-Files
- `prettier --ignore-unknown` skipt Files, die Prettier nicht parsen kann (Bilder etc.)
- Der Pre-Commit läuft erst lint-staged (schnell, nur staged), dann vollen Typecheck und Tests
