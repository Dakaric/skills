---
name: request-refactor-plan
description: Erstell einen detaillierten Refactor-Plan mit winzigen Commits per User-Interview und leg ihn als GitHub Issue ab. Nutze, wenn der User einen Refactor planen, ein Refactoring-RFC erstellen oder einen Refactor in sichere inkrementelle Schritte zerlegen will.
---

Dieser Skill wird ausgelöst, wenn der User einen Refactor-Request erstellen will. Geh die Schritte unten durch. Schritte können übersprungen werden, wenn nicht nötig.

1. Frag den User nach einer langen, detaillierten Beschreibung des Problems, das er lösen will, und etwaigen Lösungsideen.

2. Erkunde das Repo, um seine Aussagen zu verifizieren und den aktuellen Stand der Codebase zu verstehen.

3. Frag, ob er andere Optionen erwogen hat, und präsentier ihm andere Optionen.

4. Interviewe den User zur Implementation. Sei extrem detailliert und gründlich.

5. Hämmer den exakten Scope der Implementation aus. Arbeite raus, was du ändern willst und was nicht.

6. Schau in die Codebase, ob es Test-Abdeckung in diesem Bereich gibt. Wenn unzureichend, frag den User nach seinen Testing-Plänen.

7. Zerleg die Implementation in einen Plan aus winzigen Commits. Erinner dich an Martin Fowlers Rat: "mach jeden Refactoring-Schritt so klein wie möglich, damit du das Programm immer laufend sehen kannst."

8. Erstell ein GitHub Issue mit dem Refactor-Plan. Nutz das folgende Template für die Issue-Description:

<refactor-plan-template>

## Problembeschreibung

Das Problem, mit dem der Entwickler konfrontiert ist, aus Sicht des Entwicklers.

## Lösung

Die Lösung für das Problem, aus Sicht des Entwicklers.

## Commits

Ein LANGER, detaillierter Implementierungsplan. Schreib den Plan in Klartext und zerleg die Implementation in die kleinstmöglichen Commits. Jeder Commit sollte die Codebase in einem lauffähigen Zustand hinterlassen.

## Decision Document

Eine Liste der Implementierungs-Entscheidungen, die getroffen wurden. Das kann beinhalten:

- Die Module, die gebaut/modifiziert werden
- Die Interfaces dieser Module, die modifiziert werden
- Technische Klärungen vom Entwickler
- Architektur-Entscheidungen
- Schema-Änderungen
- API-Verträge
- Spezifische Interaktionen

KEINE konkreten Dateipfade oder Code-Snippets aufnehmen. Die können sehr schnell veralten.

## Test-Entscheidungen

Eine Liste der Test-Entscheidungen, die getroffen wurden. Aufnehmen:

- Eine Beschreibung dessen, was einen guten Test ausmacht (nur externes Verhalten testen, keine Implementierungsdetails)
- Welche Module getestet werden
- Prior Art für die Tests (also ähnliche Tests in der Codebase)

## Out of Scope

Eine Beschreibung der Dinge, die für diesen Refactor out of scope sind.

## Weitere Anmerkungen (optional)

Weitere Anmerkungen zum Refactor.

</refactor-plan-template>
