# Gute und schlechte Tests

## Gute Tests

**Integration-style**: durch echte Interfaces testen, nicht durch Mocks interner Teile.

```typescript
// GUT: Testet beobachtbares Behavior
test("User kann mit validem Cart einchecken", async () => {
  const cart = createCart();
  cart.add(product);
  const result = await checkout(cart, paymentMethod);
  expect(result.status).toBe("confirmed");
});
```

Eigenschaften:

- Testen Behavior, das Users / Callers interessiert
- Nutzen nur Public API
- Überleben interne Refactors
- Beschreiben WAS, nicht WIE
- Eine logische Assertion pro Test

## Schlechte Tests

**Implementation-Detail-Tests**: an interne Struktur gekoppelt.

```typescript
// SCHLECHT: Testet Implementierungsdetails
test("checkout ruft paymentService.process auf", async () => {
  const mockPayment = jest.mock(paymentService);
  await checkout(cart, payment);
  expect(mockPayment.process).toHaveBeenCalledWith(cart.total);
});
```

Red Flags:

- Interne Collaborators mocken
- Private Methods testen
- Auf Call Counts / Order asserten
- Test bricht bei Refactor ohne Behavior-Change
- Test-Name beschreibt WIE, nicht WAS
- Über externe Wege verifizieren statt durchs Interface

```typescript
// SCHLECHT: Umgeht das Interface zur Verifikation
test("createUser speichert in der Datenbank", async () => {
  await createUser({ name: "Alice" });
  const row = await db.query("SELECT * FROM users WHERE name = ?", ["Alice"]);
  expect(row).toBeDefined();
});

// GUT: Verifiziert durchs Interface
test("createUser macht User abrufbar", async () => {
  const user = await createUser({ name: "Alice" });
  const retrieved = await getUser(user.id);
  expect(retrieved.name).toBe("Alice");
});
```
