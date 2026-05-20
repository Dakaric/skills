# Interface Design

Wenn der User alternative Interfaces für einen gewählten Deepening-Kandidaten erkunden will, nutze dieses parallele Sub-Agent-Pattern. Basiert auf "Design It Twice" (Ousterhout) - deine erste Idee ist selten die beste.

Nutzt das Vokabular in [LANGUAGE.md](LANGUAGE.md) - **Module**, **Interface**, **Seam**, **Adapter**, **Leverage**.

## Prozess

### 1. Problemraum framen

Bevor du Sub-Agents spawnst, schreib eine user-gerichtete Erklärung des Problemraums für den gewählten Kandidaten:

- Die Constraints, die jedes neue Interface erfüllen müsste
- Die Abhängigkeiten, auf die es sich stützen würde, und in welche Kategorie sie fallen (siehe [DEEPENING.md](DEEPENING.md))
- Eine grobe illustrative Code-Skizze, um die Constraints zu erden - kein Vorschlag, nur ein Weg, die Constraints konkret zu machen

Zeig das dem User und geh sofort zu Schritt 2. Der User liest und denkt, während die Sub-Agents parallel arbeiten.

### 2. Sub-Agents spawnen

3+ Sub-Agents parallel mit dem Agent-Tool spawnen. Jeder muss ein **radikal anderes** Interface fürs deepened Modul produzieren.

Prompte jeden Sub-Agent mit einem separaten technischen Brief (File-Pfade, Coupling-Details, Dependency-Kategorie aus [DEEPENING.md](DEEPENING.md), was hinter dem Seam sitzt). Der Brief ist unabhängig von der user-gerichteten Problemraum-Erklärung aus Schritt 1. Gib jedem Agent eine andere Design-Constraint:

- Agent 1: "Minimier das Interface — ziel auf max. 1–3 Entry Points. Maximier Leverage pro Entry Point."
- Agent 2: "Maximier Flexibilität — unterstütz viele Use Cases und Extension."
- Agent 3: "Optimier für den häufigsten Caller — mach den Default-Fall trivial."
- Agent 4 (falls anwendbar): "Designe um Ports & Adapter für Cross-Seam-Dependencies herum."

Nimm sowohl das [LANGUAGE.md](LANGUAGE.md)-Vokabular als auch das CONTEXT.md-Vokabular in den Brief auf, damit jeder Sub-Agent Dinge konsistent mit der Architektursprache und der Domainsprache des Projekts benennt.

Jeder Sub-Agent gibt aus:

1. Interface (Typen, Methoden, Parameter - plus Invarianten, Ordering, Error-Modes)
2. Usage-Beispiel, das zeigt, wie Caller es nutzen
3. Was die Implementation hinterm Seam versteckt
4. Dependency-Strategie und Adapter (siehe [DEEPENING.md](DEEPENING.md))
5. Trade-offs - wo Leverage hoch, wo dünn ist

### 3. Präsentieren und vergleichen

Die Designs sequenziell präsentieren, damit der User jedes aufnehmen kann, dann in Prosa vergleichen. Kontrastier nach **Depth** (Leverage am Interface), **Locality** (wo Change sich konzentriert) und **Seam-Platzierung**.

Nach dem Vergleichen gib deine eigene Empfehlung: welches Design du am stärksten findest und warum. Wenn Elemente verschiedener Designs gut kombinierbar wären, schlag ein Hybrid vor. Sei meinungsstark - der User will eine starke Einschätzung, kein Menü.
