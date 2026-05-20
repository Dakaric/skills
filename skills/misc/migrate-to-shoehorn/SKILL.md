---
name: migrate-to-shoehorn
description: Test-Files von `as` Type Assertions auf @total-typescript/shoehorn migrieren. Nutze, wenn der User shoehorn erwähnt, `as` in Tests ersetzen will oder partielle Test-Daten braucht.
---

# Migrate to Shoehorn

## Warum shoehorn?

`shoehorn` lässt dich Partial-Daten in Tests übergeben, während TypeScript zufrieden bleibt. Es ersetzt `as` Assertions durch type-safe Alternativen.

**Nur Test-Code.** Niemals shoehorn in Production-Code nutzen.

Probleme mit `as` in Tests:

- Trainiert, es nicht zu nutzen
- Muss manuell den Target-Type spezifizieren
- Double-as (`as unknown as Type`) für absichtlich falsche Daten

## Install

```bash
npm i @total-typescript/shoehorn
```

## Migrations-Patterns

### Große Objekte mit wenigen benötigten Properties

Vorher:

```ts
type Request = {
  body: { id: string };
  headers: Record<string, string>;
  cookies: Record<string, string>;
  // ...20 weitere Properties
};

it("gets user by id", () => {
  // Nur body.id interessiert, aber das ganze Request muss gefaked werden
  getUser({
    body: { id: "123" },
    headers: {},
    cookies: {},
    // ...alle 20 Properties faken
  });
});
```

Nachher:

```ts
import { fromPartial } from "@total-typescript/shoehorn";

it("gets user by id", () => {
  getUser(
    fromPartial({
      body: { id: "123" },
    }),
  );
});
```

### `as Type` → `fromPartial()`

Vorher:

```ts
getUser({ body: { id: "123" } } as Request);
```

Nachher:

```ts
import { fromPartial } from "@total-typescript/shoehorn";

getUser(fromPartial({ body: { id: "123" } }));
```

### `as unknown as Type` → `fromAny()`

Vorher:

```ts
getUser({ body: { id: 123 } } as unknown as Request); // absichtlich falscher Type
```

Nachher:

```ts
import { fromAny } from "@total-typescript/shoehorn";

getUser(fromAny({ body: { id: 123 } }));
```

## Wann was nutzen

| Function        | Use Case                                           |
| --------------- | -------------------------------------------------- |
| `fromPartial()` | Partial-Daten übergeben, die trotzdem type-checken |
| `fromAny()`     | Absichtlich falsche Daten übergeben (behält Autocomplete) |
| `fromExact()`   | Volles Object erzwingen (später mit fromPartial swappen) |

## Workflow

1. **Requirements sammeln** - den User fragen:
   - Welche Test-Files haben `as` Assertions, die Probleme machen?
   - Hat er es mit großen Objekten zu tun, wo nur manche Properties zählen?
   - Muss er absichtlich falsche Daten fürs Error-Testing übergeben?

2. **Installieren und migrieren**:
   - [ ] Installieren: `npm i @total-typescript/shoehorn`
   - [ ] Test-Files mit `as` Assertions finden: `grep -r " as [A-Z]" --include="*.test.ts" --include="*.spec.ts"`
   - [ ] `as Type` durch `fromPartial()` ersetzen
   - [ ] `as unknown as Type` durch `fromAny()` ersetzen
   - [ ] Imports aus `@total-typescript/shoehorn` hinzufügen
   - [ ] Type-Check laufen lassen zum Verifizieren
