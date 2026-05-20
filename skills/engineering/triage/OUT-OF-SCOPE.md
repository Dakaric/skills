# Out-of-Scope Knowledge Base

Das `.out-of-scope/` Verzeichnis in einem Repo speichert persistente Records abgelehnter Feature Requests. Es dient zwei Zwecken:

1. **Institutional Memory** - warum ein Feature abgelehnt wurde, damit die Begründung nicht verloren geht, wenn das Issue geschlossen wird
2. **Deduplizierung** - wenn ein neues Issue reinkommt, das einer früheren Ablehnung entspricht, kann der Skill die frühere Entscheidung rausbringen, statt sie neu zu verhandeln

## Directory-Struktur

```
.out-of-scope/
├── dark-mode.md
├── plugin-system.md
└── graphql-api.md
```

Ein File pro **Konzept**, nicht pro Issue. Mehrere Issues, die das Gleiche fordern, werden unter einem File gruppiert.

## File-Format

Das File sollte in einem entspannten, lesbaren Stil geschrieben sein - mehr wie ein kurzes Design-Dokument als ein Datenbankeintrag. Nutz Absätze, Code-Beispiele und Beispiele, um die Begründung klar und nützlich für jemanden zu machen, der ihr zum ersten Mal begegnet.

```markdown
# Dark Mode

Dieses Projekt unterstützt keinen Dark Mode oder user-facing Theming.

## Warum das out of scope ist

Die Rendering-Pipeline geht von einer einzigen Color-Palette aus, definiert in
`ThemeConfig`. Mehrere Themes zu unterstützen würde Folgendes erfordern:

- Einen Theme-Context-Provider, der den gesamten Component-Tree umschließt
- Per-Component theme-aware Style-Resolution
- Eine Persistenz-Schicht für User-Theme-Präferenzen

Das ist eine signifikante Architektur-Änderung, die nicht zum Fokus des
Projekts auf Content-Authoring passt. Theming ist ein Anliegen für
Downstream-Consumer, die den Output einbetten oder weitergeben.

```ts
// Das aktuelle ThemeConfig-Interface ist nicht für Runtime-Switching designt:
interface ThemeConfig {
  colors: ColorPalette; // einzelne Palette, zur Build-Zeit aufgelöst
  fonts: FontStack;
}
```

## Prior requests

- #42 — "Add dark mode support"
- #87 — "Night theme for accessibility"
- #134 — "Dark theme option"
```

### File benennen

Nutz einen kurzen, beschreibenden Kebab-Case-Namen für das Konzept: `dark-mode.md`, `plugin-system.md`, `graphql-api.md`. Der Name sollte erkennbar genug sein, dass jemand, der das Verzeichnis browst, versteht, was abgelehnt wurde, ohne das File zu öffnen.

### Den Reason schreiben

Der Reason sollte substanziell sein - nicht "we don't want this", sondern warum. Gute Reasons referenzieren:

- Projekt-Scope oder -Philosophie ("Dieses Projekt fokussiert sich auf X; Theming ist ein Downstream-Anliegen")
- Technische Constraints ("Das zu unterstützen würde Y erfordern, was mit unserer Z-Architektur kollidiert")
- Strategische Entscheidungen ("Wir haben uns für A statt B entschieden, weil...")

Der Reason sollte durable sein. Vermeid Referenzen auf temporäre Umstände ("wir sind grad zu busy") - das sind keine echten Rejections, das sind Deferrals.

## Wann `.out-of-scope/` checken

Während der Triage (Step 1: Kontext sammeln), alle Files in `.out-of-scope/` lesen. Beim Bewerten eines neuen Issues:

- Prüfen, ob der Request einem bestehenden Out-of-Scope-Konzept entspricht
- Matching geht nach Konzept-Ähnlichkeit, nicht Keyword - "night theme" matcht `dark-mode.md`
- Wenn es einen Match gibt, dem Maintainer zeigen: "Das ist ähnlich zu `.out-of-scope/dark-mode.md` — wir haben das früher abgelehnt, weil [Reason]. Siehst du das immer noch genauso?"

Der Maintainer kann:

- **Bestätigen** - das neue Issue wird zur "Prior requests" Liste des bestehenden Files hinzugefügt und dann geschlossen
- **Reconsidern** - das Out-of-Scope-File wird gelöscht oder aktualisiert, und das Issue läuft durch normale Triage
- **Disagreen** - die Issues sind verwandt, aber distinct, weiter mit normaler Triage

## Wann nach `.out-of-scope/` schreiben

Nur wenn ein **Enhancement** (kein Bug) als `wontfix` abgelehnt wird. Der Flow:

1. Maintainer entscheidet, dass ein Feature-Request out of scope ist
2. Prüfen, ob ein matchendes `.out-of-scope/` File schon existiert
3. Wenn ja: das neue Issue an die "Prior requests" Liste anhängen
4. Wenn nein: ein neues File mit Konzeptname, Entscheidung, Reason und erstem Prior Request erstellen
5. Einen Comment am Issue posten, der die Entscheidung erklärt und das `.out-of-scope/` File erwähnt
6. Das Issue mit dem `wontfix` Label schließen

## Out-of-Scope-Files updaten oder entfernen

Wenn der Maintainer es sich bei einem vorher abgelehnten Konzept anders überlegt:

- Das `.out-of-scope/` File löschen
- Der Skill muss keine alten Issues wieder öffnen - die sind historische Records
- Das neue Issue, das das Reconsidern ausgelöst hat, läuft durch normale Triage
