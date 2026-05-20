---
name: improve-codebase-architecture
description: Findet Deepening-Möglichkeiten in einer Codebase, gestützt auf die Domain-Sprache in CONTEXT.md und die Entscheidungen in docs/adr/. Nutze, wenn der User die Architektur verbessern, Refactor-Möglichkeiten finden, eng gekoppelte Module konsolidieren oder eine Codebase testbarer und KI-navigierbarer machen will.
---

# Improve Codebase Architecture

Architektur-Reibung sichtbar machen und **Deepening-Möglichkeiten** vorschlagen - Refactors, die flache Module in tiefe verwandeln. Ziel ist Testbarkeit und KI-Navigierbarkeit.

## Glossar

Diese Begriffe in jedem Vorschlag exakt verwenden. Konsistente Sprache ist der ganze Punkt - drift nicht in "Component", "Service", "API" oder "Boundary" ab. Vollständige Definitionen in [LANGUAGE.md](LANGUAGE.md).

- **Module** — alles mit einem Interface und einer Implementation (Function, Class, Package, Slice).
- **Interface** — alles, was ein Caller wissen muss, um das Modul zu nutzen: Typen, Invarianten, Error-Modes, Ordering, Config. Nicht nur die Typ-Signatur.
- **Implementation** — der Code innendrin.
- **Depth** — Leverage am Interface: viel Verhalten hinter einem kleinen Interface. **Deep** = hohe Leverage. **Shallow** = Interface fast so komplex wie die Implementation.
- **Seam** — wo ein Interface lebt; eine Stelle, an der Verhalten geändert werden kann, ohne in-place zu editieren. (Diesen Begriff nutzen, nicht "Boundary".)
- **Adapter** — etwas Konkretes, das ein Interface an einem Seam erfüllt.
- **Leverage** — was Caller von Depth bekommen.
- **Locality** — was Maintainer von Depth bekommen: Change, Bugs, Wissen konzentriert an einer Stelle.

Schlüsselprinzipien (siehe [LANGUAGE.md](LANGUAGE.md) für die volle Liste):

- **Deletion-Test**: stell dir vor, du löschst das Modul. Wenn Komplexität verschwindet, war es ein Pass-Through. Wenn Komplexität bei N Callern wieder auftaucht, hat es seinen Job gemacht.
- **Das Interface ist die Test-Surface.**
- **Ein Adapter = hypothetischer Seam. Zwei Adapter = echter Seam.**

Dieser Skill ist _gestützt_ auf das Domain-Modell des Projekts. Die Domain-Sprache benennt gute Seams; ADRs halten Entscheidungen fest, die der Skill nicht neu aufrollen soll.

## Prozess

### 1. Explore

Erst das Domain-Glossar des Projekts und alle ADRs im betroffenen Bereich lesen.

Dann das Agent-Tool mit `subagent_type=Explore` nutzen, um durch die Codebase zu gehen. Folge keinen starren Heuristiken - explorier organisch und notier, wo du Reibung erlebst:

- Wo erfordert das Verstehen eines Konzepts, zwischen vielen kleinen Modulen hin und her zu springen?
- Wo sind Module **shallow** - Interface fast so komplex wie die Implementation?
- Wo wurden pure Functions nur für Testbarkeit extrahiert, aber die echten Bugs verstecken sich darin, wie sie aufgerufen werden (keine **Locality**)?
- Wo lecken eng gekoppelte Module über ihre Seams?
- Welche Teile der Codebase sind ungetestet oder schwer durch ihr aktuelles Interface zu testen?

Wende den **Deletion-Test** auf alles an, was du als Shallow vermutest: würde das Löschen Komplexität konzentrieren oder nur verschieben? Ein "ja, konzentriert" ist das Signal, das du suchst.

### 2. Kandidaten präsentieren

Eine nummerierte Liste von Deepening-Möglichkeiten präsentieren. Für jeden Kandidaten:

- **Files** — welche Files / Module beteiligt sind
- **Problem** — warum die aktuelle Architektur Reibung erzeugt
- **Solution** — Plain-English-Beschreibung dessen, was sich ändern würde
- **Benefits** — erklärt anhand von Locality und Leverage, und wie Tests sich verbessern würden

**Nutze das CONTEXT.md-Vokabular für die Domain und das [LANGUAGE.md](LANGUAGE.md)-Vokabular für die Architektur.** Wenn `CONTEXT.md` "Order" definiert, sprich vom "Order intake module" - nicht vom "FooBarHandler" und nicht vom "Order service".

**ADR-Konflikte**: wenn ein Kandidat einem bestehenden ADR widerspricht, bring ihn nur, wenn die Reibung echt genug ist, um das ADR neu aufzurollen. Markier es klar (z.B. _"widerspricht ADR-0007 — aber wert wieder aufzumachen, weil…"_). List nicht jeden theoretischen Refactor, den ein ADR verbietet.

Schlage noch KEINE Interfaces vor. Frag den User: "Welche davon willst du erkunden?"

### 3. Grilling-Loop

Sobald der User einen Kandidaten wählt, drop in eine Grilling-Konversation. Geh den Design-Tree mit ihm durch - Constraints, Abhängigkeiten, die Form des deepened Modules, was hinter dem Seam sitzt, welche Tests überleben.

Side Effects passieren inline, sobald Entscheidungen sich verfestigen:

- **Ein deepened Module nach einem Konzept benennen, das nicht in `CONTEXT.md` steht?** Den Begriff in `CONTEXT.md` aufnehmen - gleiche Disziplin wie `/grill-with-docs` (siehe [CONTEXT-FORMAT.md](../grill-with-docs/CONTEXT-FORMAT.md)). File lazy anlegen, wenn es nicht existiert.
- **Einen unscharfen Begriff während der Konversation schärfen?** `CONTEXT.md` sofort dort updaten.
- **User lehnt den Kandidaten mit einem load-bearing Grund ab?** Bietet ein ADR an, formuliert als: _"Soll ich das als ADR festhalten, damit künftige Architecture-Reviews es nicht erneut vorschlagen?"_ Nur anbieten, wenn der Grund von einem zukünftigen Explorer tatsächlich gebraucht würde, um nicht das Gleiche wieder vorzuschlagen - skip ephemere Gründe ("aktuell nicht wert") und selbstevidente. Siehe [ADR-FORMAT.md](../grill-with-docs/ADR-FORMAT.md).
- **Alternative Interfaces für das deepened Module erkunden wollen?** Siehe [INTERFACE-DESIGN.md](INTERFACE-DESIGN.md).
