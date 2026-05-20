# Logic Prototype

Eine winzige interaktive Terminal-App, die den User ein State-Modell von Hand steuern lässt. Nutz das, wenn die Frage um **Business Logic, State Transitions oder Data Shape** geht - das, was auf Papier vernünftig aussieht, sich aber erst falsch anfühlt, wenn du es durch echte Fälle drückst.

## Wann das die richtige Form ist

- "Ich bin mir nicht sicher, ob diese State Machine den Edge Case behandelt, in dem X dann Y passiert."
- "Erlaubt mir dieses Datenmodell überhaupt, den Fall darzustellen, in dem..."
- "Ich will durchspielen, wie die API aussehen sollte, bevor ich sie schreibe."
- Alles, wo der User **Buttons drücken und State sich ändern sehen** will.

Wenn die Frage "wie sollte das aussehen" ist - falscher Branch. Nutze [UI.md](UI.md).

## Prozess

### 1. Frage formulieren

Bevor du Code schreibst, schreib auf, welches State-Modell und welche Frage du prototypest. Ein Absatz, im README des Prototyps oder als Kommentar oben in der Datei. Ein Logic-Prototyp, der die falsche Frage beantwortet, ist reine Verschwendung - mach die Frage explizit, damit sie später geprüft werden kann, egal ob der User jetzt zuschaut oder AFK zurückkommt.

### 2. Sprache wählen

Nimm, was das Host-Projekt nutzt. Wenn das Projekt keine offensichtliche Runtime hat (z.B. ein Docs-Repo), frag.

Match die bestehenden Tooling-Konventionen des Projekts - bring keinen neuen Package Manager oder Runtime nur für den Prototyp.

### 3. Logic in ein portables Modul isolieren

Steck die eigentliche Logic - das Stück, das die Frage beantwortet - hinter ein kleines, pures Interface, das später rausgehoben und in die echte Codebase eingebaut werden könnte. Das TUI drumherum ist Wegwerf; das Logic-Modul sollte das nicht sein.

Die richtige Form hängt von der Frage ab:

- **Ein pure Reducer** - `(state, action) => state`. Gut, wenn Actions diskrete Events sind und State ein einzelner Wert.
- **Eine State Machine** - explizite States und Transitions. Gut, wenn "welche Actions sind jetzt überhaupt legal" Teil der Frage ist.
- **Ein kleines Set pure Functions** über einem Plain-Data-Type. Gut, wenn es keinen impliziten Current State gibt - nur Transformationen.
- **Eine Class oder ein Modul mit klarer Method-Surface**, wenn die Logic genuin laufenden internen State besitzt.

Wähl die Form, die am besten zur gestellten Frage passt, *nicht* die, die am einfachsten ans TUI zu wiren ist. Halt sie pur: kein I/O, kein Terminal-Code, kein `console.log` für Control Flow. Das TUI importiert sie und ruft rein; nichts fließt in die andere Richtung.

Das macht den Prototyp über seine Lebenszeit hinaus nützlich. Wenn die Frage beantwortet ist, kann der validierte Reducer / die Machine / das Function-Set ins echte Modul gehoben werden - die TUI-Shell wird gelöscht.

### 4. Das kleinste TUI bauen, das den State sichtbar macht

Bau es als **leichtgewichtiges TUI** - bei jedem Tick den Screen clearen (`console.clear()` / `print("\033[2J\033[H")` / Äquivalent) und den ganzen Frame neu rendern. Der User sollte immer eine stabile View sehen, keinen wachsenden Scrollback.

Jeder Frame hat zwei Teile, in dieser Reihenfolge:

1. **Current State**, pretty-printed und diff-freundlich (ein Feld pro Zeile oder formatiertes JSON). Nutze **bold** für Feldnamen oder Section-Header und **dim** für weniger wichtigen Context (Timestamps, IDs, abgeleitete Werte). Native ANSI Escape Codes sind okay - `\x1b[1m` bold, `\x1b[2m` dim, `\x1b[0m` reset. Keine Styling-Library reinziehen, wenn nicht schon im Projekt.
2. **Keyboard Shortcuts**, unten gelistet: `[a] add user  [d] delete user  [t] tick clock  [q] quit`. Bold die Taste, dim die Beschreibung oder umgekehrt - was sauber liest.

Verhalten:

1. **State initialisieren** - ein einzelnes In-Memory-Object / Struct. Den ersten Frame beim Start rendern.
2. **Einen Keystroke (oder eine Zeile)** auf einmal lesen, an einen Handler dispatchen, der State mutiert.
3. **Re-rendern** des vollen Frames nach jeder Action - nicht anhängen, ersetzen.
4. **Loopen bis Quit.**

Der ganze Frame sollte auf einen Screen passen.

### 5. Mit einem Command runnable machen

Ein Script zum bestehenden Task Runner des Projekts hinzufügen (`package.json` Scripts, `Makefile`, `justfile`, `pyproject.toml`). Der User soll `pnpm run <prototype-name>` oder Äquivalent ausführen - nie einen Pfad merken müssen.

Wenn das Host-Projekt keinen Task Runner hat, schreib den Command einfach oben ins README des Prototyps.

### 6. Übergeben

Gib dem User den Run-Command. Er wird selbst steuern; die interessanten Momente sind, wenn er sagt "Moment, das sollte gar nicht gehen" oder "huh, ich dachte X wäre anders" - das sind die Bugs in der _Idee_, was der ganze Punkt ist. Wenn er neue Actions will, fügst du sie hinzu. Prototypen evolvieren.

### 7. Antwort festhalten

Wenn der Prototyp seinen Job getan hat, ist die Antwort auf die Frage das Einzige, was sich zu behalten lohnt. Wenn der User da ist, frag, was er gelernt hat. Wenn nicht, lass ein `NOTES.md` neben dem Prototyp, damit die Antwort eingetragen werden kann (oder von dir, falls du der Session zugeschaut hast), bevor der Prototyp gelöscht wird.

## Anti-Patterns

- **Keine Tests hinzufügen.** Ein Prototyp, der Tests braucht, ist kein Prototyp mehr.
- **Nicht an die echte Datenbank wiren.** Nimm einen In-Memory-Store, außer die Frage geht spezifisch um Persistenz.
- **Nicht generalisieren.** Kein "was, wenn wir später X unterstützen wollen". Der Prototyp beantwortet eine Frage.
- **Logic und TUI nicht ineinander verwischen.** Wenn der Reducer / die State Machine `console.log`, Prompts oder Terminal-Escape-Codes referenziert, ist sie nicht mehr portabel. Halt das TUI als dünne Shell über einem puren Modul.
- **Die TUI-Shell nicht in Production shippen.** Die Shell ist dafür optimiert, von Hand aus einem Terminal gesteuert zu werden. Das Logic-Modul dahinter ist das Stück, das zu behalten lohnt.
