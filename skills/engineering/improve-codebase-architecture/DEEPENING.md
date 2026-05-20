# Deepening

Wie ein Cluster shallowe Module sicher deepened wird, gegeben seine Abhängigkeiten. Setzt das Vokabular in [LANGUAGE.md](LANGUAGE.md) voraus — **Module**, **Interface**, **Seam**, **Adapter**.

## Abhängigkeits-Kategorien

Wenn du einen Kandidaten fürs Deepening bewertest, klassifizier seine Abhängigkeiten. Die Kategorie bestimmt, wie das deepened Modul über seinen Seam getestet wird.

### 1. In-process

Pure Berechnung, In-Memory State, kein I/O. Immer deepenbar - die Module mergen und durchs neue Interface direkt testen. Kein Adapter nötig.

### 2. Local-substitutable

Abhängigkeiten, die lokale Test-Stand-ins haben (PGLite für Postgres, In-Memory-Filesystem). Deepenbar, wenn das Stand-in existiert. Das deepened Modul wird mit dem Stand-in getestet, das in der Test-Suite läuft. Der Seam ist intern; kein Port am externen Interface des Moduls.

### 3. Remote but owned (Ports & Adapters)

Eigene Services über eine Netzwerk-Boundary (Microservices, interne APIs). Definier einen **Port** (Interface) am Seam. Das tiefe Modul besitzt die Logik; der Transport wird als **Adapter** injiziert. Tests nutzen einen In-Memory-Adapter. Production nutzt einen HTTP- / gRPC- / Queue-Adapter.

Form der Empfehlung: *"Definier einen Port am Seam, implementier einen HTTP-Adapter für Production und einen In-Memory-Adapter fürs Testing, sodass die Logik in einem tiefen Modul sitzt, auch wenn sie übers Netzwerk deployed ist."*

### 4. True external (Mock)

Third-Party-Services (Stripe, Twilio etc.), die du nicht kontrollierst. Das deepened Modul nimmt die externe Abhängigkeit als injizierten Port; Tests liefern einen Mock-Adapter.

## Seam-Disziplin

- **Ein Adapter heißt hypothetischer Seam. Zwei Adapter heißen echter.** Führ keinen Port ein, wenn nicht mindestens zwei Adapter gerechtfertigt sind (typisch Production + Test). Ein Single-Adapter-Seam ist nur Indirection.
- **Interne Seams vs externe Seams.** Ein tiefes Modul kann interne Seams haben (privat zur Implementation, von eigenen Tests genutzt) sowie den externen Seam an seinem Interface. Expose interne Seams nicht durchs Interface nur weil Tests sie nutzen.

## Test-Strategie: replace, don't layer

- Alte Unit-Tests auf shallowen Modulen werden Waste, sobald Tests am Interface des deepened Moduls existieren - löschen.
- Neue Tests am Interface des deepened Moduls schreiben. Das **Interface ist die Test-Surface**.
- Tests asserten auf beobachtbare Outcomes durchs Interface, nicht auf internen State.
- Tests sollten interne Refactors überleben - sie beschreiben Verhalten, nicht Implementation. Wenn ein Test sich ändern muss, wenn die Implementation sich ändert, testet er an der Interface vorbei.
