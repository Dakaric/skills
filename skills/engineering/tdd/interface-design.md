# Interface Design für Testbarkeit

Gute Interfaces machen Testen natürlich:

1. **Dependencies akzeptieren, nicht erzeugen**

   ```typescript
   // Testbar
   function processOrder(order, paymentGateway) {}

   // Schwer zu testen
   function processOrder(order) {
     const gateway = new StripeGateway();
   }
   ```

2. **Results zurückgeben, keine Side Effects produzieren**

   ```typescript
   // Testbar
   function calculateDiscount(cart): Discount {}

   // Schwer zu testen
   function applyDiscount(cart): void {
     cart.total -= discount;
   }
   ```

3. **Kleine Surface Area**
   - Weniger Methoden = weniger Tests nötig
   - Weniger Parameter = einfacheres Test-Setup
