---
name: design-an-interface
description: Generier mehrere radikal unterschiedliche Interface-Designs für ein Modul per parallelen Sub-Agents. Nutze, wenn der User eine API designen, Interface-Optionen erkunden, Modul-Formen vergleichen oder "design it twice" erwähnt.
---

# Design an Interface

Basiert auf "Design It Twice" aus "A Philosophy of Software Design": deine erste Idee ist selten die beste. Generier mehrere radikal unterschiedliche Designs und vergleich sie dann.

## Workflow

### 1. Requirements sammeln

Vor dem Designen verstehen:

- [ ] Welches Problem löst dieses Modul?
- [ ] Wer sind die Caller? (andere Module, externe User, Tests)
- [ ] Was sind die zentralen Operationen?
- [ ] Constraints? (Performance, Kompatibilität, bestehende Patterns)
- [ ] Was sollte innen versteckt vs außen exposed sein?

Frag: "Was muss dieses Modul tun? Wer wird es nutzen?"

### 2. Designs generieren (Parallel Sub-Agents)

Spawn 3+ Sub-Agents gleichzeitig mit dem Task-Tool. Jeder muss einen **radikal unterschiedlichen** Ansatz produzieren.

```
Prompt-Template für jeden Sub-Agent:

Designe ein Interface für: [Modul-Beschreibung]

Requirements: [gesammelte Requirements]

Constraints für dieses Design: [jedem Agent ein anderes Constraint zuweisen]
- Agent 1: "Minimier die Method-Anzahl - ziel auf max. 1-3 Methoden"
- Agent 2: "Maximier Flexibilität - unterstütz viele Use Cases"
- Agent 3: "Optimier für den häufigsten Fall"
- Agent 4: "Lass dich von [spezifischem Paradigma/Library] inspirieren"

Output-Format:
1. Interface-Signature (Typen/Methoden)
2. Usage-Beispiel (wie Caller es nutzen)
3. Was dieses Design intern versteckt
4. Trade-offs dieses Ansatzes
```

### 3. Designs präsentieren

Jedes Design zeigen mit:

1. **Interface Signature** - Typen, Methoden, Parameter
2. **Usage Examples** - wie Caller es in der Praxis nutzen
3. **What it hides** - intern gehaltene Komplexität

Designs sequenziell präsentieren, damit der User jeden Ansatz aufnehmen kann, bevor verglichen wird.

### 4. Designs vergleichen

Nachdem alle Designs gezeigt sind, vergleich sie nach:

- **Interface-Einfachheit**: weniger Methoden, einfachere Parameter
- **General-Purpose vs spezialisiert**: Flexibilität vs Fokus
- **Implementation-Effizienz**: erlaubt die Form effiziente Internals?
- **Depth**: kleines Interface, das signifikante Komplexität versteckt (gut) vs großes Interface mit dünner Implementation (schlecht)
- **Einfachheit der korrekten Nutzung** vs **Einfachheit der Fehlnutzung**

Trade-offs in Prosa diskutieren, nicht in Tabellen. Heb hervor, wo Designs am stärksten divergieren.

### 5. Synthetisieren

Oft kombiniert das beste Design Insights aus mehreren Optionen. Frag:

- "Welches Design passt am besten zu deinem Primary Use Case?"
- "Gibt es Elemente aus anderen Designs, die's wert sind, übernommen zu werden?"

## Evaluierungskriterien

Aus "A Philosophy of Software Design":

**Interface-Einfachheit**: weniger Methoden, einfachere Parameter = leichter zu lernen und korrekt zu nutzen.

**General-Purpose**: kann zukünftige Use Cases ohne Änderungen handlen. Aber Vorsicht vor Over-Generalization.

**Implementation-Effizienz**: erlaubt die Interface-Form effiziente Implementation? Oder zwingt sie zu awkward Internals?

**Depth**: kleines Interface, das signifikante Komplexität versteckt = Deep Module (gut). Großes Interface mit dünner Implementation = Shallow Module (vermeiden).

## Anti-Patterns

- Lass Sub-Agents keine ähnlichen Designs produzieren - erzwing radikale Differenz
- Skip den Vergleich nicht - der Wert ist im Kontrast
- Implementier nicht - hier geht's rein um Interface-Form
- Evaluier nicht nach Implementations-Aufwand
