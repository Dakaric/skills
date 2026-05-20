---
name: diagnose
description: Disziplinierter Diagnose-Loop für harte Bugs und Performance-Regressionen. Reproduzieren → minimieren → hypothetisieren → instrumentieren → fixen → Regression-Test. Nutze, wenn der User "diagnose this" / "debug this" sagt, einen Bug meldet, sagt dass etwas kaputt ist / wirft / failed, oder eine Performance-Regression beschreibt.
---

# Diagnose

Eine Disziplin für harte Bugs. Phasen nur überspringen, wenn explizit begründet.

Beim Erkunden der Codebase nutzt du das Domain-Glossar des Projekts, um ein klares mentales Modell der relevanten Module zu bekommen, und prüfst die ADRs im betroffenen Bereich.

## Phase 1 — Feedback-Loop aufbauen

**Das ist der Skill.** Alles andere ist mechanisch. Wenn du ein schnelles, deterministisches, agent-ausführbares Pass/Fail-Signal für den Bug hast, findest du die Ursache - Bisektion, Hypothesen-Tests und Instrumentierung verbrauchen einfach nur dieses Signal. Hast du keines, rettet dich kein noch so langes Starren auf den Code.

Investiere hier unverhältnismäßig viel Aufwand. **Sei aggressiv. Sei kreativ. Gib nicht auf.**

### Möglichkeiten zum Aufbau - probier sie ungefähr in dieser Reihenfolge

1. **Failender Test** an dem Seam, der den Bug erreicht - Unit, Integration, e2e.
2. **Curl / HTTP-Script** gegen einen laufenden Dev-Server.
3. **CLI-Aufruf** mit einem Fixture-Input, stdout gegen einen bekannten-guten Snapshot diffen.
4. **Headless-Browser-Script** (Playwright / Puppeteer) - steuert die UI, asserted auf DOM / Console / Network.
5. **Captured Trace replayen.** Einen echten Network-Request / Payload / Event-Log auf Platte speichern, isoliert durch den Code-Path replayen.
6. **Throwaway-Harness.** Ein minimales Subset des Systems hochziehen (ein Service, gemockte Deps), das den Bug-Code-Path mit einem einzigen Funktionsaufruf ausübt.
7. **Property- / Fuzz-Loop.** Wenn der Bug "manchmal falscher Output" ist, 1000 zufällige Inputs durchlaufen und den Failure Mode suchen.
8. **Bisection-Harness.** Wenn der Bug zwischen zwei bekannten Zuständen aufgetreten ist (Commit, Datensatz, Version), automatisier "boot at state X, check, repeat", damit du `git bisect run` drauf laufen lassen kannst.
9. **Differential Loop.** Den gleichen Input durch Old-Version vs New-Version (oder zwei Configs) laufen lassen und Outputs diffen.
10. **HITL-Bash-Script.** Letzter Ausweg. Wenn ein Mensch klicken muss, steuer _ihn_ mit `scripts/hitl-loop.template.sh`, damit der Loop strukturiert bleibt. Captured Output speist sich zurück zu dir.

Bau den richtigen Feedback-Loop und der Bug ist zu 90% gefixt.

### Am Loop selbst iterieren

Behandel den Loop wie ein Produkt. Sobald du _einen_ Loop hast, frag:

- Kann ich ihn schneller machen? (Setup cachen, irrelevante Init skippen, Test-Scope einengen.)
- Kann ich das Signal schärfer machen? (Auf das spezifische Symptom asserten, nicht auf "didn't crash".)
- Kann ich ihn deterministischer machen? (Zeit pinnen, RNG seeden, Filesystem isolieren, Netzwerk einfrieren.)

Ein 30-Sekunden-Flaky-Loop ist kaum besser als kein Loop. Ein 2-Sekunden-deterministischer Loop ist eine Debugging-Superkraft.

### Nicht-deterministische Bugs

Das Ziel ist kein sauberer Repro, sondern eine **höhere Reproduktionsrate**. Den Trigger 100× loopen, parallelisieren, Stress hinzufügen, Timing-Fenster einengen, Sleeps injizieren. Ein 50%-Flake-Bug ist debugbar; 1% ist es nicht - heb die Rate, bis es debugbar wird.

### Wenn du ehrlich keinen Loop bauen kannst

Halt an und sag das explizit. Liste, was du probiert hast. Frag den User nach: (a) Zugang zu der Umgebung, die ihn reproduziert, (b) einem captured Artifact (HAR-File, Log-Dump, Core-Dump, Screen-Recording mit Timestamps), oder (c) der Erlaubnis, temporäre Production-Instrumentierung hinzuzufügen. Geh **nicht** weiter zu Hypothesen ohne Loop.

Geh nicht zu Phase 2, bevor du einen Loop hast, an den du glaubst.

## Phase 2 — Reproduzieren

Den Loop laufen lassen. Den Bug auftreten sehen.

Bestätigen:

- [ ] Der Loop produziert den Failure Mode, den der **User** beschrieben hat - nicht ein anderes Failure, das zufällig in der Nähe passiert. Falscher Bug = falscher Fix.
- [ ] Das Failure ist über mehrere Runs hinweg reproduzierbar (oder, für nicht-deterministische Bugs, mit einer Rate hoch genug zum Debuggen reproduzierbar).
- [ ] Du hast das exakte Symptom captured (Error-Message, falscher Output, langsames Timing), damit spätere Phasen verifizieren können, dass der Fix es wirklich adressiert.

Geh nicht weiter, bis du den Bug reproduzierst.

## Phase 3 — Hypothetisieren

Generiere **3-5 gerankte Hypothesen**, bevor du irgendeine testest. Single-Hypothesis-Generation verankert auf die erste plausible Idee.

Jede Hypothese muss **falsifizierbar** sein: nenn die Vorhersage, die sie macht.

> Format: "Wenn <X> die Ursache ist, dann wird <Änderung Y> den Bug verschwinden lassen / <Änderung Z> wird ihn schlimmer machen."

Wenn du die Vorhersage nicht aussprechen kannst, ist die Hypothese ein Vibe - verwerfen oder schärfen.

**Zeig die gerankte Liste dem User, bevor du testest.** Er hat oft Domain-Wissen, das sofort umsortiert ("wir haben gerade eine Änderung an #3 deployed"), oder kennt Hypothesen, die er schon ausgeschlossen hat. Billiger Checkpoint, große Zeitersparnis. Blockier nicht darauf - geh mit deinem Ranking weiter, wenn der User AFK ist.

## Phase 4 — Instrumentieren

Jede Probe muss auf eine spezifische Vorhersage aus Phase 3 mappen. **Eine Variable nach der anderen ändern.**

Tool-Präferenz:

1. **Debugger / REPL-Inspection**, wenn die Env das unterstützt. Ein Breakpoint schlägt zehn Logs.
2. **Targeted Logs** an den Boundaries, die Hypothesen unterscheiden.
3. Niemals "alles loggen und greppen".

**Jedes Debug-Log taggen** mit einem eindeutigen Prefix, z.B. `[DEBUG-a4f2]`. Cleanup am Ende wird zu einem einzigen Grep. Ungetaggte Logs überleben; getaggte Logs sterben.

**Perf-Branch.** Bei Performance-Regressionen sind Logs meist falsch. Stattdessen: Baseline-Messung aufbauen (Timing-Harness, `performance.now()`, Profiler, Query-Plan), dann bisektieren. Erst messen, dann fixen.

## Phase 5 — Fix + Regression Test

Schreib den Regression-Test **vor dem Fix** - aber nur, wenn es einen **korrekten Seam** dafür gibt.

Ein korrekter Seam ist einer, an dem der Test das **echte Bug-Pattern** ausübt, wie es an der Call-Site auftritt. Wenn der einzige verfügbare Seam zu flach ist (Single-Caller-Test, wenn der Bug mehrere Caller braucht, Unit-Test, der die Kette, die den Bug auslöste, nicht replizieren kann), gibt ein Regression-Test dort falsches Vertrauen.

**Wenn kein korrekter Seam existiert, ist das selbst der Befund.** Notier es. Die Codebase-Architektur verhindert, dass der Bug festgenagelt werden kann. Flag das für die nächste Phase.

Wenn ein korrekter Seam existiert:

1. Verwandel den minimierten Repro in einen failenden Test an diesem Seam.
2. Schau zu, wie er failed.
3. Wende den Fix an.
4. Schau zu, wie er passt.
5. Lass den Phase-1-Feedback-Loop gegen das ursprüngliche (un-minimierte) Szenario nochmal laufen.

## Phase 6 — Cleanup + Post-Mortem

Pflicht vor "fertig":

- [ ] Der ursprüngliche Repro reproduziert nicht mehr (Phase-1-Loop nochmal laufen lassen)
- [ ] Regression-Test passt (oder das Fehlen eines Seams ist dokumentiert)
- [ ] Alle `[DEBUG-...]`-Instrumentierung entfernt (`grep` auf den Prefix)
- [ ] Throwaway-Prototypen gelöscht (oder an einen klar markierten Debug-Ort verschoben)
- [ ] Die Hypothese, die richtig war, steht in der Commit- / PR-Message - damit der nächste Debugger lernt

**Dann frag: was hätte diesen Bug verhindert?** Wenn die Antwort einen architektonischen Change beinhaltet (kein guter Test-Seam, verworrene Caller, versteckte Kopplung), übergib an den `/improve-codebase-architecture` Skill mit den Details. Mach die Empfehlung **nach** dem Fix, nicht davor - du hast jetzt mehr Informationen als am Anfang.
