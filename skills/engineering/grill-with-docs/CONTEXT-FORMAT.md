# CONTEXT.md Format

## Struktur

```md
# {Context-Name}

{Ein- bis zweisätzige Beschreibung, was dieser Context ist und warum er existiert.}

## Language

**Order**:
{Ein- bis zweisätzige Beschreibung des Begriffs}
_Avoid_: Purchase, transaction

**Invoice**:
Eine Zahlungsanforderung, die nach Lieferung an einen Kunden geschickt wird.
_Avoid_: Bill, payment request

**Customer**:
Eine Person oder Organisation, die Orders aufgibt.
_Avoid_: Client, buyer, account
```

## Regeln

- **Sei meinungsstark.** Wenn es mehrere Wörter für dasselbe Konzept gibt, wähl das beste und liste die anderen als zu vermeidende Aliasse.
- **Konflikte explizit flaggen.** Wenn ein Begriff mehrdeutig genutzt wird, ruf es unter "Flagged ambiguities" aus mit klarer Auflösung.
- **Definitionen straff halten.** Maximal ein bis zwei Sätze. Definier, was es IST, nicht was es tut.
- **Beziehungen zeigen.** Begriffsnamen fett, Kardinalität ausdrücken, wo offensichtlich.
- **Nur Begriffe aufnehmen, die spezifisch für den Context des Projekts sind.** Allgemeine Programmierkonzepte (Timeouts, Error-Typen, Utility-Patterns) gehören nicht rein, auch wenn das Projekt sie ausgiebig nutzt. Bevor du einen Begriff hinzufügst, frag: ist das ein Konzept einzigartig für diesen Context, oder ein allgemeines Programmierkonzept? Nur Ersteres gehört rein.
- **Begriffe unter Subheadings gruppieren**, wenn natürliche Cluster entstehen. Wenn alle Begriffe zu einem zusammenhängenden Bereich gehören, ist eine flache Liste okay.
- **Beispiel-Dialog schreiben.** Eine Konversation zwischen einem Dev und einem Domain-Experten, die zeigt, wie die Begriffe natürlich interagieren und die Grenzen zwischen verwandten Konzepten klärt.

## Single- vs Multi-Context-Repos

**Single Context (die meisten Repos):** Eine `CONTEXT.md` im Repo-Root.

**Mehrere Contexts:** Eine `CONTEXT-MAP.md` im Repo-Root listet die Contexts, wo sie liegen und wie sie zusammenhängen:

```md
# Context Map

## Contexts

- [Ordering](./src/ordering/CONTEXT.md) — nimmt Customer-Orders entgegen und trackt sie
- [Billing](./src/billing/CONTEXT.md) — generiert Invoices und verarbeitet Payments
- [Fulfillment](./src/fulfillment/CONTEXT.md) — managt Warehouse-Picking und Shipping

## Relationships

- **Ordering → Fulfillment**: Ordering emittiert `OrderPlaced`-Events; Fulfillment konsumiert sie, um mit dem Picking zu starten
- **Fulfillment → Billing**: Fulfillment emittiert `ShipmentDispatched`-Events; Billing konsumiert sie, um Invoices zu generieren
- **Ordering ↔ Billing**: Shared Types für `CustomerId` und `Money`
```

Der Skill leitet ab, welche Struktur greift:

- Wenn `CONTEXT-MAP.md` existiert, sie lesen, um die Contexts zu finden
- Wenn nur eine Root `CONTEXT.md` existiert, Single Context
- Wenn keines existiert, lazy eine Root `CONTEXT.md` anlegen, sobald der erste Begriff aufgelöst wird

Wenn mehrere Contexts existieren, ableiten, zu welchem das aktuelle Thema gehört. Wenn unklar, fragen.
