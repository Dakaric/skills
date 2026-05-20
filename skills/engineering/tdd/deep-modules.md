# Deep Modules

Aus "A Philosophy of Software Design":

**Deep Module** = kleines Interface + viel Implementation

```
┌─────────────────────┐
│   Small Interface   │  ← Wenige Methoden, einfache Params
├─────────────────────┤
│                     │
│                     │
│  Deep Implementation│  ← Komplexe Logik versteckt
│                     │
│                     │
└─────────────────────┘
```

**Shallow Module** = großes Interface + wenig Implementation (vermeiden)

```
┌─────────────────────────────────┐
│       Large Interface           │  ← Viele Methoden, komplexe Params
├─────────────────────────────────┤
│  Thin Implementation            │  ← Nur Durchreichung
└─────────────────────────────────┘
```

Beim Designen von Interfaces frag:

- Kann ich die Anzahl Methoden reduzieren?
- Kann ich die Parameter vereinfachen?
- Kann ich mehr Komplexität nach innen verstecken?
