---
name: qa
description: Interaktive QA-Session, in der der User Bugs oder Issues konversational meldet und der Agent GitHub Issues anlegt. Erkundet die Codebase im Hintergrund für Kontext und Domain-Sprache. Nutze, wenn der User Bugs melden, QA machen, Issues konversational ablegen will oder "QA session" erwähnt.
---

# QA Session

Führ eine interaktive QA-Session. Der User beschreibt Probleme, die er erlebt. Du klärst, erkundest die Codebase für Kontext und legst GitHub Issues an, die durable, user-fokussiert sind und die Domain-Sprache des Projekts nutzen.

## Für jedes Issue, das der User raised

### 1. Zuhören und leicht klären

Lass den User das Problem in eigenen Worten beschreiben. Stell **maximal 2-3 kurze klärende Fragen** fokussiert auf:

- Was er erwartet hat vs was tatsächlich passierte
- Schritte zur Reproduktion (falls nicht offensichtlich)
- Ob es konsistent oder intermittent ist

KEIN Over-Interview. Wenn die Beschreibung klar genug ist zum Ablegen, weiter.

### 2. Codebase im Hintergrund erkunden

Während du mit dem User redest, kickst du einen Agent (subagent_type=Explore) im Hintergrund, um den relevanten Bereich zu verstehen. Das Ziel ist NICHT, einen Fix zu finden - sondern:

- Die Domain-Sprache in dem Bereich zu lernen (UBIQUITOUS_LANGUAGE.md prüfen)
- Zu verstehen, was das Feature tun soll
- Die User-gerichtete Verhaltens-Boundary identifizieren

Dieser Kontext hilft dir, ein besseres Issue zu schreiben - aber das Issue selbst sollte KEINE spezifischen Files, Zeilennummern oder interne Implementation-Details referenzieren.

### 3. Scope abschätzen: Single Issue oder Breakdown?

Vor dem Ablegen entscheiden, ob das ein **Single Issue** ist oder in mehrere Issues **aufgeteilt** werden muss.

Aufteilen, wenn:

- Der Fix mehrere unabhängige Bereiche umspannt (z.B. "die Form-Validierung ist falsch UND die Success-Message fehlt UND der Redirect ist kaputt")
- Klar trennbare Concerns existieren, an denen verschiedene Leute parallel arbeiten könnten
- Der User etwas mit mehreren distincten Failure Modes oder Symptomen beschreibt

Als Single Issue halten, wenn:

- Es ein Verhalten ist, das an einer Stelle falsch ist
- Die Symptome alle vom gleichen Root Behavior verursacht werden

### 4. Die GitHub Issues ablegen

Issues mit `gh issue create` erstellen. Frag den User NICHT vorher zum Reviewen - leg ab und teil die URLs.

Issues müssen **durable** sein - sie sollten nach großen Refactors noch Sinn machen. Aus der User-Perspektive schreiben.

#### Für ein Single Issue

Dieses Template nutzen:

```
## Was passiert ist

[Beschreib das tatsächliche Verhalten, das der User erlebt hat, in einfacher Sprache]

## Was ich erwartet habe

[Beschreib das erwartete Verhalten]

## Schritte zur Reproduktion

1. [Konkrete, nummerierte Schritte, denen ein Entwickler folgen kann]
2. [Domain-Begriffe aus der Codebase nutzen, keine internen Modul-Namen]
3. [Relevante Inputs, Flags oder Configuration aufnehmen]

## Zusätzlicher Kontext

[Weitere Beobachtungen vom User oder aus der Codebase-Exploration, die helfen, das Issue einzuordnen — z.B. "das passiert nur, wenn der Docker-Layer genutzt wird, nicht der Filesystem-Layer" — Domain-Sprache nutzen, aber keine Files zitieren]
```

#### Für einen Breakdown (mehrere Issues)

Issues in Dependency-Reihenfolge anlegen (Blockers zuerst), damit du echte Issue-Nummern referenzieren kannst.

Dieses Template für jedes Sub-Issue nutzen:

```
## Parent Issue

#<parent-issue-number> (falls du ein Tracking-Issue erstellt hast) oder "Während der QA-Session gemeldet"

## Was kaputt ist

[Beschreib dieses spezifische Verhaltensproblem — nur diesen Slice, nicht den ganzen Report]

## Was ich erwartet habe

[Erwartetes Verhalten für diesen spezifischen Slice]

## Schritte zur Reproduktion

1. [Schritte spezifisch für DIESES Issue]

## Blocked by

- #<issue-number> (falls dieses Issue nicht gefixt werden kann, bis ein anderes gelöst ist)

Oder "Keine — kann sofort starten", wenn keine Blocker.

## Zusätzlicher Kontext

[Weitere Beobachtungen relevant für diesen Slice]
```

Beim Erstellen eines Breakdowns:

- **Bevorzug viele dünne Issues gegenüber wenigen dicken** - jedes sollte unabhängig fixbar und verifizierbar sein
- **Blocking-Beziehungen ehrlich markieren** - wenn Issue B genuin nicht testbar ist, bis A gefixt ist, sag das. Wenn unabhängig, markier beide als "Keine — kann sofort starten"
- **Issues in Dependency-Reihenfolge erstellen**, damit du echte Issue-Nummern in "Blocked by" referenzieren kannst
- **Parallelisierung maximieren** - das Ziel ist, dass mehrere Leute (oder Agents) verschiedene Issues simultan grabben können

#### Regeln für alle Issue Bodies

- **Keine File-Pfade oder Zeilennummern** - die werden stale
- **Die Domain-Sprache des Projekts nutzen** (UBIQUITOUS_LANGUAGE.md prüfen, falls existent)
- **Behaviors beschreiben, nicht Code** - "der Sync-Service schafft es nicht, den Patch anzuwenden", nicht "applyPatch() throws on line 42"
- **Reproduktions-Schritte sind Pflicht** - wenn du sie nicht bestimmen kannst, frag den User
- **Knapp halten** - ein Dev sollte das Issue in 30 Sekunden lesen können

Nach dem Ablegen alle Issue-URLs printen (mit zusammengefassten Blocking-Beziehungen) und fragen: "Nächstes Issue, oder sind wir fertig?"

### 5. Session fortsetzen

Weitermachen, bis der User sagt, dass er fertig ist. Jedes Issue ist unabhängig - batch sie nicht.
