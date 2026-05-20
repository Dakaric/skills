# Language

Gemeinsames Vokabular für jeden Vorschlag, den dieser Skill macht. Diese Begriffe exakt nutzen - kein Substituieren durch "Component", "Service", "API" oder "Boundary". Konsistente Sprache ist der ganze Punkt.

## Begriffe

**Module**
Alles mit einem Interface und einer Implementation. Bewusst skalen-agnostisch - gilt gleichermaßen für eine Function, Class, Package oder Tier-übergreifenden Slice.
_Vermeiden_: Unit, Component, Service.

**Interface**
Alles, was ein Caller wissen muss, um das Modul korrekt zu nutzen. Beinhaltet die Typ-Signatur, aber auch Invarianten, Ordering-Constraints, Error-Modes, erforderliche Konfiguration und Performance-Charakteristiken.
_Vermeiden_: API, Signature (zu eng - die meinen nur die Typ-Ebene).

**Implementation**
Was in einem Modul drin ist - sein Code-Körper. Unterschieden von **Adapter**: ein Ding kann ein kleiner Adapter mit großer Implementation sein (ein Postgres-Repo) oder ein großer Adapter mit kleiner Implementation (ein In-Memory-Fake). Greif zu "Adapter", wenn der Seam das Thema ist; sonst zu "Implementation".

**Depth**
Leverage am Interface - die Menge an Verhalten, die ein Caller (oder Test) pro Einheit Interface ausüben kann, die er lernen muss. Ein Modul ist **deep**, wenn eine große Menge Verhalten hinter einem kleinen Interface sitzt. Ein Modul ist **shallow**, wenn das Interface fast so komplex ist wie die Implementation.

**Seam** _(von Michael Feathers)_
Eine Stelle, an der du Verhalten ändern kannst, ohne an dieser Stelle zu editieren. Die *Position*, an der das Interface eines Moduls lebt. Wo der Seam hingehört, ist eine eigene Design-Entscheidung, getrennt von dem, was dahinter steht.
_Vermeiden_: Boundary (überladen mit DDDs Bounded Context).

**Adapter**
Eine konkrete Sache, die ein Interface an einem Seam erfüllt. Beschreibt *Rolle* (welchen Slot es füllt), nicht Substanz (was drin ist).

**Leverage**
Was Caller von Depth bekommen. Mehr Capability pro Einheit Interface, die sie lernen müssen. Eine Implementation zahlt sich über N Call-Sites und M Tests aus.

**Locality**
Was Maintainer von Depth bekommen. Change, Bugs, Wissen und Verification konzentrieren sich an einer Stelle, statt sich über Caller zu verteilen. Einmal fixen, überall gefixt.

## Prinzipien

- **Depth ist eine Eigenschaft des Interfaces, nicht der Implementation.** Ein tiefes Modul kann intern aus kleinen, mockbaren, austauschbaren Teilen bestehen - die sind einfach nicht Teil des Interfaces. Ein Modul kann **interne Seams** haben (privat zur Implementation, von eigenen Tests genutzt) sowie den **externen Seam** an seinem Interface.
- **Der Deletion-Test.** Stell dir vor, du löschst das Modul. Wenn Komplexität verschwindet, hat das Modul nichts versteckt (war ein Pass-Through). Wenn Komplexität bei N Callern wieder auftaucht, hat das Modul seinen Job gemacht.
- **Das Interface ist die Test-Surface.** Caller und Tests kreuzen den gleichen Seam. Wenn du *hinter* das Interface testen willst, hat das Modul wahrscheinlich die falsche Form.
- **Ein Adapter heißt hypothetischer Seam. Zwei Adapter heißen echter.** Führ keinen Seam ein, wenn nicht tatsächlich etwas darüber variiert.

## Beziehungen

- Ein **Module** hat genau ein **Interface** (die Oberfläche, die es Callern und Tests präsentiert).
- **Depth** ist eine Eigenschaft eines **Module**, gemessen gegen sein **Interface**.
- Ein **Seam** ist, wo das **Interface** eines **Module** lebt.
- Ein **Adapter** sitzt an einem **Seam** und erfüllt das **Interface**.
- **Depth** produziert **Leverage** für Caller und **Locality** für Maintainer.

## Verworfene Framings

- **Depth als Ratio Implementation-Lines zu Interface-Lines** (Ousterhout): belohnt das Aufblähen der Implementation. Wir nutzen Depth-als-Leverage stattdessen.
- **"Interface" als das TypeScript-Keyword `interface` oder die public Methods einer Class**: zu eng - Interface hier beinhaltet jeden Fakt, den ein Caller wissen muss.
- **"Boundary"**: überladen mit DDDs Bounded Context. Sag **Seam** oder **Interface**.
