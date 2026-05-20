---
name: to-prd
description: Den aktuellen Konversationskontext in ein PRD verwandeln und im Projekt-Issue-Tracker veröffentlichen. Nutze, wenn der User ein PRD aus dem aktuellen Kontext erstellen will.
---

Dieser Skill nimmt den aktuellen Konversationskontext und das Codebase-Verständnis und produziert ein PRD. Interviewe den User NICHT - synthesier nur, was du schon weißt.

Der Issue Tracker und das Triage-Label-Vokabular sollten dir mitgegeben worden sein — falls nicht, `/setup-matt-pocock-skills` ausführen.

## Prozess

1. Erkunde das Repo, um den aktuellen Stand der Codebase zu verstehen, falls noch nicht geschehen. Nutz das Domain-Glossar-Vokabular des Projekts durchgängig im PRD und respektier ADRs im betroffenen Bereich.

2. Skizzier die wichtigsten Module, die du bauen oder modifizieren musst, um die Implementation abzuschließen. Such aktiv nach Gelegenheiten, Deep Modules zu extrahieren, die isoliert getestet werden können.

Ein Deep Module (im Gegensatz zu einem Shallow Module) kapselt viel Funktionalität in einem einfachen, testbaren Interface, das sich selten ändert.

Prüf mit dem User, ob diese Module zu seinen Erwartungen passen. Prüf mit dem User, für welche Module er Tests geschrieben haben will.

3. Schreib das PRD mit dem Template unten und veröffentlich es im Projekt-Issue-Tracker. Wende das `ready-for-agent` Triage-Label an - keine zusätzliche Triage nötig.

<prd-template>

## Problembeschreibung

Das Problem, mit dem der User konfrontiert ist, aus Sicht des Users.

## Lösung

Die Lösung für das Problem, aus Sicht des Users.

## User Stories

Eine LANGE, nummerierte Liste von User Stories. Jede User Story sollte folgendes Format haben:

1. Als <Akteur> möchte ich ein <Feature>, sodass <Benefit>

<user-story-example>
1. Als Mobile-Banking-Kunde möchte ich den Kontostand auf meinen Konten sehen, sodass ich besser informierte Entscheidungen über meine Ausgaben treffen kann
</user-story-example>

Diese Liste von User Stories sollte extrem umfangreich sein und alle Aspekte des Features abdecken.

## Implementierungs-Entscheidungen

Eine Liste der Implementierungs-Entscheidungen, die getroffen wurden. Das kann beinhalten:

- Die Module, die gebaut/modifiziert werden
- Die Interfaces dieser Module, die modifiziert werden
- Technische Klärungen vom Entwickler
- Architektur-Entscheidungen
- Schema-Änderungen
- API-Verträge
- Spezifische Interaktionen

KEINE konkreten Dateipfade oder Code-Snippets aufnehmen. Die können sehr schnell veralten.

Ausnahme: Wenn ein Prototyp ein Snippet produziert hat, das eine Entscheidung präziser kodiert als Prosa es kann (State Machine, Reducer, Schema, Type-Shape), inlinet es bei der relevanten Entscheidung und notiert kurz, dass es aus einem Prototyp stammt. Auf die entscheidungsrelevanten Teile zuschneiden, kein lauffähiges Demo, nur die wichtigen Bits.

## Test-Entscheidungen

Eine Liste der Test-Entscheidungen, die getroffen wurden. Aufnehmen:

- Eine Beschreibung dessen, was einen guten Test ausmacht (nur externes Verhalten testen, keine Implementierungsdetails)
- Welche Module getestet werden
- Prior Art für die Tests (also ähnliche Tests in der Codebase)

## Out of Scope

Eine Beschreibung der Dinge, die für dieses PRD out of scope sind.

## Weitere Anmerkungen

Weitere Anmerkungen zum Feature.

</prd-template>
