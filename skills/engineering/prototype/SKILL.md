---
name: prototype
description: Bau einen Wegwerf-Prototyp, um ein Design auszuarbeiten, bevor du dich darauf festlegst. Routet zwischen zwei Branches - eine ausführbare Terminal-App für State- bzw. Business-Logic-Fragen, oder mehrere radikal unterschiedliche UI-Varianten, umschaltbar über eine Route. Nutze, wenn der User prototypen, ein Datenmodell oder eine State Machine sanity-checken, ein UI mocken, Design-Optionen erkunden will oder "prototype this", "let me play with it", "try a few designs" sagt.
---

# Prototype

Ein Prototyp ist **Wegwerf-Code, der eine Frage beantwortet**. Die Frage entscheidet die Form.

## Branch wählen

Identifizier, welche Frage beantwortet wird - aus dem Prompt des Users, dem umgebenden Code oder durch Nachfragen, wenn der User da ist:

- **"Fühlt sich diese Logic / dieses State-Modell richtig an?"** → [LOGIC.md](LOGIC.md). Bau eine winzige interaktive Terminal-App, die die State Machine durch Fälle drückt, die auf Papier schwer zu denken sind.
- **"Wie sollte das aussehen?"** → [UI.md](UI.md). Generier mehrere radikal unterschiedliche UI-Varianten auf einer Route, umschaltbar über einen URL-Search-Param und eine floating Bottom Bar.

Die zwei Branches produzieren sehr unterschiedliche Artefakte - das hier falsch zu kriegen, vergeudet den ganzen Prototyp. Wenn die Frage genuin mehrdeutig ist und der User unerreichbar, default zu dem Branch, der besser zum umgebenden Code passt (ein Backend-Modul → Logic; eine Page oder Component → UI), und nenn die Annahme oben im Prototyp.

## Regeln, die für beide gelten

1. **Wegwerf ab Tag eins, und klar markiert als solcher.** Den Prototyp-Code nah dort platzieren, wo er tatsächlich genutzt wird (neben dem Modul oder der Page, für die er prototypt), damit der Kontext offensichtlich ist - aber so benennen, dass ein gelegentlicher Leser sieht: Prototyp, nicht Production. Für Wegwerf-UI-Routes der bestehenden Routing-Konvention des Projekts folgen; nicht eine neue Top-Level-Struktur erfinden.
2. **Ein Command zum Ausführen.** Was der bestehende Task Runner des Projekts unterstützt - `pnpm <name>`, `python <path>`, `bun <path>` etc. Der User muss ohne Nachdenken starten können.
3. **Keine Persistenz per Default.** State lebt im Memory. Persistenz ist das, was der Prototyp _prüft_, nicht etwas, worauf er sich stützen sollte. Wenn die Frage explizit eine Datenbank involviert, eine Scratch-DB oder ein lokales File mit klarem "PROTOTYP — bitte löschen"-Namen treffen.
4. **Polish überspringen.** Keine Tests, kein Error Handling über das hinaus, was den Prototyp _runnable_ macht, keine Abstraktionen. Es geht darum, schnell etwas zu lernen und es dann zu löschen.
5. **State sichtbar machen.** Nach jeder Aktion (Logic) oder bei jedem Variant-Switch (UI) den vollen relevanten State printen oder rendern, damit der User sieht, was sich geändert hat.
6. **Bei Erledigung löschen oder absorbieren.** Wenn der Prototyp seine Frage beantwortet hat, entweder löschen oder die validierte Entscheidung in den echten Code falten - nicht im Repo verrotten lassen.

## Wenn fertig

Die _Antwort_ ist das Einzige, was aus einem Prototyp zu behalten lohnt. Halt sie irgendwo dauerhaft fest (Commit-Message, ADR, Issue oder ein `NOTES.md` neben dem Prototyp) zusammen mit der Frage, die er beantwortet hat. Wenn der User da ist, ist dieses Festhalten ein kurzes Gespräch; wenn nicht, lass einen Platzhalter, damit er (oder du beim nächsten Pass) das Urteil eintragen kann, bevor der Prototyp gelöscht wird.
