---
name: handoff
description: Die aktuelle Konversation in ein Handoff-Dokument komprimieren, damit ein anderer Agent die Arbeit aufnehmen kann.
argument-hint: "Wofür wird die nächste Session genutzt?"
---

Schreib ein Handoff-Dokument, das die aktuelle Konversation zusammenfasst, damit ein frischer Agent die Arbeit fortsetzen kann. Speicher in den Temp-Ordner des User-OS - nicht in den aktuellen Workspace.

Beinhalte eine "Suggested Skills" Section im Dokument, die Skills vorschlägt, die der Agent aufrufen sollte.

Dupliziere keinen Content, der schon in anderen Artefakten festgehalten ist (PRDs, Plans, ADRs, Issues, Commits, Diffs). Referenzier sie stattdessen per Pfad oder URL.

Redacte sensible Informationen wie API-Keys, Passwörter oder personenbezogene Daten.

Wenn der User Argumente übergeben hat, behandel sie als Beschreibung dessen, worauf die nächste Session fokussiert, und richte das Doc danach aus.
