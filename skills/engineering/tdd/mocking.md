# Wann mocken

Mock nur an **System Boundaries**:

- Externe APIs (Payment, Email etc.)
- Datenbanken (manchmal - bevorzug Test-DB)
- Zeit / Randomness
- Filesystem (manchmal)

Nicht mocken:

- Deine eigenen Classes / Modules
- Interne Collaborators
- Alles, was du kontrollierst

## Für Mockability designen

An System Boundaries Interfaces designen, die leicht zu mocken sind:

**1. Dependency Injection nutzen**

Externe Dependencies reinreichen, statt sie intern zu erzeugen:

```typescript
// Leicht zu mocken
function processPayment(order, paymentClient) {
  return paymentClient.charge(order.total);
}

// Schwer zu mocken
function processPayment(order) {
  const client = new StripeClient(process.env.STRIPE_KEY);
  return client.charge(order.total);
}
```

**2. SDK-style Interfaces gegenüber generischen Fetchers bevorzugen**

Spezifische Functions für jede externe Operation erstellen, statt einer generischen Function mit Conditional-Logic:

```typescript
// GUT: Jede Function ist unabhängig mockbar
const api = {
  getUser: (id) => fetch(`/users/${id}`),
  getOrders: (userId) => fetch(`/users/${userId}/orders`),
  createOrder: (data) => fetch('/orders', { method: 'POST', body: data }),
};

// SCHLECHT: Mocking erfordert Conditional-Logic im Mock
const api = {
  fetch: (endpoint, options) => fetch(endpoint, options),
};
```

Der SDK-Ansatz heißt:
- Jeder Mock returnt eine spezifische Form
- Keine Conditional-Logic im Test-Setup
- Leichter zu sehen, welche Endpoints ein Test ausübt
- Type Safety pro Endpoint
