<p>
  <a href="https://www.aihero.dev/s/skills-newsletter">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skills-repo-dark_2x.png">
      <source media="(prefers-color-scheme: light)" srcset="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skill-repo-light_2x.png">
      <img alt="Skills" src="https://res.cloudinary.com/total-typescript/image/upload/v1777382277/skill-repo-light_2x.png" width="369">
    </picture>
  </a>
</p>

# Skills For Real Engineers

[![skills.sh](https://skills.sh/b/mattpocock/skills)](https://skills.sh/mattpocock/skills)

Meine Agent-Skills, die ich täglich für echtes Engineering nutze - kein Vibe-Coding.

Echte Anwendungen zu entwickeln ist hart. Ansätze wie GSD, BMAD und Spec-Kit versuchen zu helfen, indem sie den Prozess übernehmen. Dabei nehmen sie dir aber die Kontrolle weg und machen Bugs im Prozess schwer auflösbar.

Diese Skills sind klein, einfach anpassbar und kombinierbar. Sie funktionieren mit jedem Modell. Sie basieren auf jahrzehntelanger Engineering-Erfahrung. Bastel daran herum. Mach sie zu deinen eigenen. Viel Spaß.

Wenn du Änderungen an diesen Skills und neue Skills mitbekommen willst, kannst du dich zu ~60.000 anderen Devs auf meinem Newsletter eintragen:

[Zum Newsletter anmelden](https://www.aihero.dev/s/skills-newsletter)

## Quickstart (30-Sekunden-Setup)

1. Den skills.sh Installer ausführen:

```bash
npx skills@latest add mattpocock/skills
```

2. Wähle die Skills, die du willst, und die Coding-Agents, auf denen sie installiert werden sollen. **Stell sicher, dass du `/setup-matt-pocock-skills` auswählst**.

3. Führe `/setup-matt-pocock-skills` in deinem Agent aus. Er wird:
   - Dich fragen, welchen Issue Tracker du nutzen willst (GitHub, Linear oder lokale Dateien)
   - Dich fragen, welche Labels du bei der Triage auf Tickets anwendest (`/triage` arbeitet mit Labels)
   - Dich fragen, wo du die Docs speichern willst, die wir anlegen

4. Bam - du bist startklar.

## Warum es diese Skills gibt

Ich habe diese Skills gebaut, um typische Failure Modes zu beheben, die ich bei Claude Code, Codex und anderen Coding-Agents sehe.

### #1: Der Agent hat nicht das gemacht, was ich wollte

> "No-one knows exactly what they want"
>
> David Thomas & Andrew Hunt, [The Pragmatic Programmer](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V)

**Das Problem**. Der häufigste Failure Mode in der Softwareentwicklung ist Misalignment. Du denkst, der Dev weiß, was du willst. Dann siehst du, was er gebaut hat - und du merkst, er hat dich überhaupt nicht verstanden.

Im KI-Zeitalter ist das genauso. Es gibt eine Kommunikationslücke zwischen dir und dem Agent. Der Fix dafür ist eine **Grilling-Session** - der Agent stellt dir detaillierte Fragen zu dem, was du baust.

**Der Fix** ist die Nutzung von:

- [`/grill-me`](./skills/productivity/grill-me/SKILL.md) - für Anwendungen ohne Code
- [`/grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md) - wie [`/grill-me`](./skills/productivity/grill-me/SKILL.md), aber mit mehr Goodies (siehe unten)

Das sind meine beliebtesten Skills. Sie helfen dir, dich mit dem Agent abzustimmen, bevor du loslegst, und tief über die Änderung nachzudenken, die du vornimmst. Nutze sie _jedes Mal_, wenn du eine Änderung machen willst.

### #2: Der Agent ist viel zu geschwätzig

> With a ubiquitous language, conversations among developers and expressions of the code are all derived from the same domain model.
>
> Eric Evans, [Domain-Driven-Design](https://www.amazon.co.uk/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

**Das Problem**: Am Projektstart sprechen Devs und die Leute, für die sie die Software bauen (die Domain-Experten), normalerweise verschiedene Sprachen.

Die gleiche Spannung habe ich mit meinen Agents gespürt. Agents werden meist in ein Projekt geworfen und sollen sich den Jargon selbst beibringen. Also nutzen sie 20 Wörter, wo eines reichen würde.

**Der Fix** dafür ist eine gemeinsame Sprache. Ein Dokument, das Agents hilft, den im Projekt verwendeten Jargon zu dekodieren.

<details>
<summary>
Beispiel
</summary>

Hier ein Beispiel einer [`CONTEXT.md`](https://github.com/mattpocock/course-video-manager/blob/076a5a7a182db0fe1e62971dd7a68bcadf010f1c/CONTEXT.md) aus meinem `course-video-manager` Repo. Welche Variante ist leichter zu lesen?

- **VORHER**: "There's a problem when a lesson inside a section of a course is made 'real' (i.e. given a spot in the file system)"
- **NACHHER**: "There's a problem with the materialization cascade"

Diese Knappheit zahlt sich Session für Session aus.

</details>

Das ist in [`/grill-with-docs`](./skills/engineering/grill-with-docs/SKILL.md) eingebaut. Eine Grilling-Session, die dir hilft, eine gemeinsame Sprache mit der KI aufzubauen und schwer erklärbare Entscheidungen in ADRs zu dokumentieren.

Wie mächtig das ist, lässt sich schwer in Worte fassen. Es ist vielleicht die coolste Technik in diesem Repo. Probier's aus und sieh selbst.

> [!TIP]
> Eine gemeinsame Sprache hat viele weitere Vorteile, nicht nur die Reduktion von Geschwätzigkeit:
>
> - **Variablen, Funktionen und Dateien werden konsistent benannt** mit der gemeinsamen Sprache
> - Dadurch lässt sich die **Codebase leichter navigieren** für den Agent
> - Der Agent **verbraucht außerdem weniger Tokens beim Denken**, weil er Zugriff auf eine knappere Sprache hat

### #3: Der Code funktioniert nicht

> "Always take small, deliberate steps. The rate of feedback is your speed limit. Never take on a task that's too big."
>
> David Thomas & Andrew Hunt, [The Pragmatic Programmer](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V)

**Das Problem**: Sagen wir, du und der Agent seid euch einig, was gebaut werden soll. Was passiert, wenn der Agent _trotzdem_ Mist produziert?

Dann musst du dir deine Feedback-Loops anschauen. Ohne Feedback darüber, wie der produzierte Code tatsächlich läuft, fliegt der Agent blind.

**Der Fix**: Du brauchst die üblichen Feedback-Loops: statische Typen, Browser-Zugang und automatisierte Tests.

Bei automatisierten Tests ist ein Red-Green-Refactor Loop entscheidend. Hier schreibt der Agent zuerst einen failenden Test und fixt ihn dann. Das gibt dem Agent ein konsistentes Feedback-Level und führt zu deutlich besserem Code.

Ich habe einen **[`/tdd`](./skills/engineering/tdd/SKILL.md) Skill** gebaut, den du in jedes Projekt einbauen kannst. Er fördert Red-Green-Refactor und gibt dem Agent reichlich Guidance, was gute und schlechte Tests ausmacht.

Fürs Debugging habe ich außerdem einen **[`/diagnose`](./skills/engineering/diagnose/SKILL.md)** Skill gebaut, der Best Debugging Practices in einen einfachen Loop verpackt.

### #4: Wir haben einen Ball of Mud gebaut

> "Invest in the design of the system _every day_."
>
> Kent Beck, [Extreme Programming Explained](https://www.amazon.co.uk/Extreme-Programming-Explained-Embrace-Change/dp/0321278658)

> "The best modules are deep. They allow a lot of functionality to be accessed through a simple interface."
>
> John Ousterhout, [A Philosophy Of Software Design](https://www.amazon.co.uk/Philosophy-Software-Design-2nd/dp/173210221X)

**Das Problem**: Die meisten Apps, die mit Agents gebaut werden, sind komplex und schwer zu ändern. Weil Agents das Coden radikal beschleunigen, beschleunigen sie auch Software-Entropie. Codebases werden in beispiellosem Tempo komplexer.

**Der Fix** ist ein radikal neuer Ansatz für KI-gestützte Entwicklung: sich um das Design des Codes kümmern.

Das ist in jeder Schicht dieser Skills eingebaut:

- [`/to-prd`](./skills/engineering/to-prd/SKILL.md) fragt dich ab, welche Module du anfasst, bevor ein PRD erstellt wird
- [`/zoom-out`](./skills/engineering/zoom-out/SKILL.md) weist den Agent an, Code im Kontext des Gesamtsystems zu erklären

Und vor allem: [`/improve-codebase-architecture`](./skills/engineering/improve-codebase-architecture/SKILL.md) hilft dir, eine Codebase zu retten, die zum Ball of Mud geworden ist. Ich empfehle, das alle paar Tage auf deiner Codebase laufen zu lassen.

### Zusammenfassung

Software-Engineering-Fundamentals sind wichtiger denn je. Diese Skills sind mein bester Versuch, diese Fundamentals in wiederholbare Praktiken zu kondensieren, damit du die besten Apps deiner Karriere shippen kannst. Viel Spaß.

## Referenz

### Engineering

Skills, die ich täglich für Code-Arbeit nutze.

- **[diagnose](./skills/engineering/diagnose/SKILL.md)** — Disziplinierter Diagnose-Loop für harte Bugs und Performance-Regressionen: reproduzieren → minimieren → hypothetisieren → instrumentieren → fixen → Regression-Test.
- **[grill-with-docs](./skills/engineering/grill-with-docs/SKILL.md)** — Grilling-Session, die deinen Plan gegen das bestehende Domain-Modell prüft, Terminologie schärft und `CONTEXT.md` plus ADRs inline aktualisiert.
- **[triage](./skills/engineering/triage/SKILL.md)** — Issues durch eine State Machine aus Triage Roles triagen.
- **[improve-codebase-architecture](./skills/engineering/improve-codebase-architecture/SKILL.md)** — Deepening-Möglichkeiten in einer Codebase finden, gestützt auf die Domain-Sprache in `CONTEXT.md` und die Entscheidungen in `docs/adr/`.
- **[setup-matt-pocock-skills](./skills/engineering/setup-matt-pocock-skills/SKILL.md)** — Per-Repo-Konfiguration aufsetzen (Issue Tracker, Triage-Label-Vokabular, Domain-Doc-Layout), die die anderen Engineering-Skills konsumieren. Einmal pro Repo ausführen, bevor du `to-issues`, `to-prd`, `triage`, `diagnose`, `tdd`, `improve-codebase-architecture` oder `zoom-out` nutzt.
- **[tdd](./skills/engineering/tdd/SKILL.md)** — Test-driven Development mit Red-Green-Refactor Loop. Baut Features oder fixt Bugs, ein Vertical Slice nach dem anderen.
- **[to-issues](./skills/engineering/to-issues/SKILL.md)** — Jeden Plan, jede Spec oder jedes PRD in unabhängig greifbare GitHub Issues zerlegen, per Vertical Slices.
- **[to-prd](./skills/engineering/to-prd/SKILL.md)** — Den aktuellen Konversationskontext in ein PRD verwandeln und als GitHub Issue einreichen. Kein Interview - es synthetisiert nur, was du schon besprochen hast.
- **[zoom-out](./skills/engineering/zoom-out/SKILL.md)** — Den Agent anweisen, herauszuzoomen und breiteren Kontext oder eine höhere Perspektive auf einen unbekannten Code-Abschnitt zu geben.
- **[prototype](./skills/engineering/prototype/SKILL.md)** — Einen Wegwerf-Prototyp bauen, um ein Design auszuarbeiten. Entweder eine ausführbare Terminal-App für State- bzw. Business-Logic-Fragen, oder mehrere radikal unterschiedliche UI-Varianten, umschaltbar über eine einzige Route.

### Productivity

Allgemeine Workflow-Tools, nicht code-spezifisch.

- **[caveman](./skills/productivity/caveman/SKILL.md)** — Ultra-komprimierter Kommunikationsmodus. Senkt Token-Verbrauch um ~75%, indem Füllwörter wegfallen, aber die volle technische Genauigkeit bleibt.
- **[grill-me](./skills/productivity/grill-me/SKILL.md)** — Werde unerbittlich zu einem Plan oder Design befragt, bis jeder Zweig des Decision Trees aufgelöst ist.
- **[handoff](./skills/productivity/handoff/SKILL.md)** — Die aktuelle Konversation in ein Handoff-Dokument komprimieren, damit ein anderer Agent die Arbeit fortsetzen kann.
- **[write-a-skill](./skills/productivity/write-a-skill/SKILL.md)** — Neue Skills mit richtiger Struktur, Progressive Disclosure und gebündelten Ressourcen erstellen.

### Misc

Tools, die ich behalte, aber selten nutze.

- **[git-guardrails-claude-code](./skills/misc/git-guardrails-claude-code/SKILL.md)** — Claude Code Hooks einrichten, die gefährliche Git-Commands (push, reset --hard, clean, etc.) blockieren, bevor sie ausgeführt werden.
- **[migrate-to-shoehorn](./skills/misc/migrate-to-shoehorn/SKILL.md)** — Test-Files von `as` Type Assertions auf @total-typescript/shoehorn migrieren.
- **[scaffold-exercises](./skills/misc/scaffold-exercises/SKILL.md)** — Exercise-Verzeichnisstrukturen mit Sections, Problems, Solutions und Explainern anlegen.
- **[setup-pre-commit](./skills/misc/setup-pre-commit/SKILL.md)** — Husky Pre-Commit Hooks mit lint-staged, Prettier, Type Checking und Tests aufsetzen.
