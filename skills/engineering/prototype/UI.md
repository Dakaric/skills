# UI Prototype

Generier **mehrere radikal unterschiedliche UI-Varianten** auf einer Route, umschaltbar über eine floating Bottom Bar. Der User flippt im Browser zwischen Varianten, wählt eine (oder klaut Stücke aus jeder), schmeißt den Rest weg.

Wenn die Frage um Logic / State geht statt darum, wie etwas aussieht - falscher Branch. Nutze [LOGIC.md](LOGIC.md).

## Wann das die richtige Form ist

- "Wie sollte diese Page aussehen?"
- "Ich will ein paar Optionen für dieses Dashboard sehen, bevor ich mich festlege."
- "Probier ein anderes Layout für den Settings-Screen."
- Jedes Mal, wenn der User sonst einen Tag verbringen würde, im Kopf zwischen drei vagen Mockups zu wählen.

## Zwei Sub-Formen — bevorzuge stark Sub-Form A

Ein UI-Prototyp ist viel leichter zu beurteilen, wenn er **gegen den Rest der App stößt** - echter Header, echte Sidebar, echte Daten, echte Density. Eine Wegwerf-Route allein ist ein Vakuum: jede Variante sieht in Isolation okay aus. Default zu Sub-Form A, wann immer es eine plausible bestehende Page zum Hosten der Varianten gibt. Greif nur zu Sub-Form B, wenn der Prototyp genuin kein nahes Zuhause hat.

### Sub-Form A — Anpassung an eine bestehende Page (bevorzugt)

Die Route existiert schon. Varianten werden **auf der gleichen Route** gerendert, gegated durch einen `?variant=` URL-Search-Param. Das bestehende Data Fetching, die Params und Auth bleiben - nur das Rendering swappt. Das ist der Default; nimm das, wenn kein spezifischer Grund dagegen spricht.

Wenn der Prototyp für etwas ist, das noch keine Page hat, aber *natürlich in einer leben würde* (eine neue Section des Dashboards, eine neue Card im Settings-Screen, ein neuer Step in einem bestehenden Flow) - das ist immer noch Sub-Form A. Mount die Varianten in die Host-Page.

### Sub-Form B — eine neue Page (letzter Ausweg)

Nutz das nur, wenn das, was prototypt wird, genuin keine bestehende Page zum Reinpacken hat - z.B. eine komplett neue Top-Level-Surface oder ein Flow, der nirgends sinnvoll einbettbar ist.

Erstell eine **Wegwerf-Route**, die der bestehenden Routing-Konvention des Projekts folgt - erfinde keine neue Top-Level-Struktur. Benenn sie so, dass es offensichtlich ein Prototyp ist (z.B. das Wort `prototype` im Pfad oder Filename). Gleiches `?variant=` Pattern.

Bevor du dich auf Sub-Form B festlegst, sanity-check: gibt's wirklich keine bestehende Page, in die das eingebettet werden könnte? Eine leere Route versteckt Design-Probleme, die eine bevölkerte aufdecken würde.

In beiden Sub-Formen ist die floating Bottom Bar identisch.

## Prozess

### 1. Frage formulieren und N wählen

Default zu **3 Varianten**. Mehr als 5 hört auf, radikal unterschiedlich zu sein und wird Rauschen - cap dort.

Schreib den Plan in eine Zeile, am Ort des Prototyps oder als Kommentar oben im File:

> "Drei Varianten der Settings-Page, umschaltbar via `?variant=`, auf der bestehenden `/settings`-Route."

Das funktioniert, egal ob der User da ist, um zu widersprechen, oder nicht.

### 2. Radikal unterschiedliche Varianten generieren

Entwirf jede Variante. Halt jede an:

- Den Zweck der Page und die Daten, auf die sie Zugriff hat.
- Die Component Library / das Styling-System des Projekts (TailwindCSS, shadcn, MUI, plain CSS, was auch immer).
- Einen klaren exportierten Component-Namen, z.B. `VariantA`, `VariantB`, `VariantC`.

Varianten müssen **strukturell unterschiedlich** sein - anderes Layout, andere Informations-Hierarchie, andere Primary Affordance, nicht nur andere Farben. Drei leicht abgewandelte Card Grids sind kein UI-Prototyp, das ist Tapete. Wenn zwei Entwürfe zu ähnlich rauskommen, mach einen mit explizitem "keine Card Grids verwenden"-Guidance neu.

### 3. Zusammen verdrahten

Erstell eine einzige Switcher-Component auf der Route:

```tsx
// Pseudo-Code — an das Framework des Projekts anpassen
const variant = searchParams.get('variant') ?? 'A';
return (
  <>
    {variant === 'A' && <VariantA {...data} />}
    {variant === 'B' && <VariantB {...data} />}
    {variant === 'C' && <VariantC {...data} />}
    <PrototypeSwitcher variants={['A','B','C']} current={variant} />
  </>
);
```

Für Sub-Form A (bestehende Page): das ganze bestehende Data Fetching über dem Switcher lassen; nur der gerenderte Subtree wechselt pro Variante.

Für Sub-Form B (neue Page): die Wegwerf-Route unter `/prototype/<name>` mountet den gleichen Switcher.

### 4. Floating Switcher bauen

Eine kleine Fixed-Position-Bar unten-mittig auf dem Screen mit drei Teilen:

- **Left Arrow** - cyclet zur vorherigen Variante (wrappt um).
- **Variant Label** - zeigt den aktuellen Variant-Key und, falls die Variante einen Namen exportiert, den auch. z.B. `B — Sidebar layout`.
- **Right Arrow** - cyclet vorwärts (wrappt um).

Verhalten:

- Klick auf einen Pfeil updated den URL-Search-Param (nutz den Router des Frameworks - `router.replace` bei Next, `navigate` bei React Router etc), damit die Variante teilbar und reload-stabil ist.
- Keyboard: `←` und `→` Pfeiltasten cyclen auch. Intercept keine Pfeiltasten, wenn ein `<input>`, `<textarea>` oder `[contenteditable]` fokussiert ist.
- Visuell unterscheidbar von der Page (z.B. high-contrast Pill, leichter Schatten), damit klar wird: nicht Teil des bewerteten Designs.
- Versteckt in Production-Builds - gate auf `process.env.NODE_ENV !== 'production'` oder Äquivalent, damit ein versehentlicher Prototyp-Merge die Bar nicht an User shippt.

Den Switcher in eine einzelne shared Component packen, damit beide Sub-Formen ihn wiederverwenden können. Platzier ihn da, wo shared UI im Projekt lebt.

### 5. Übergeben

Surface die URL (und die `?variant=`-Keys). Der User flippt durch, sobald er Zeit hat. Das interessante Feedback ist meist **"Ich will den Header von B mit der Sidebar von C"** - das ist das eigentliche Design, das er will.

### 6. Antwort festhalten und aufräumen

Sobald eine Variante gewonnen hat, schreib auf, welche und warum (Commit-Message, ADR, Issue oder ein `NOTES.md` neben dem Prototyp, wenn AFK und der User noch nicht reagiert hat). Dann:

- **Sub-Form A** - die verlierenden Varianten und den Switcher löschen; den Gewinner in die bestehende Page falten.
- **Sub-Form B** - die Gewinner-Variante zu einer echten Route befördern, die Wegwerf-Route und den Switcher löschen.

Lass keine Variant-Components oder den Switcher rumliegen. Sie verrotten schnell und verwirren den nächsten Leser.

## Anti-Patterns

- **Varianten, die sich nur in Farbe oder Copy unterscheiden.** Das ist ein Tweak, kein Prototyp. Echte Varianten widersprechen sich strukturell.
- **Zu viel Code zwischen Varianten teilen.** Ein shared `<Header>` ist okay; ein shared `<Layout>` zerstört den Punkt. Jede Variante sollte das Layout wegwerfen dürfen.
- **Varianten an echte Mutations wiren.** Read-only-Prototypen sind okay. Wenn eine Variante mutieren muss, zeig sie auf einen Stub - die Frage ist "wie sollte das aussehen", nicht "funktioniert das Backend".
- **Den Prototyp direkt in Production befördern.** Der Variant-Code wurde unter Prototyp-Constraints geschrieben (keine Tests, minimales Error Handling). Schreib ihn richtig neu, wenn du ihn einfaltest.
