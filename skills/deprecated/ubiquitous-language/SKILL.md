---
name: ubiquitous-language
description: Extrahier ein DDD-style Ubiquitous-Language-Glossar aus der aktuellen Konversation, flagge Mehrdeutigkeiten und schlag kanonische Begriffe vor. Speichert in UBIQUITOUS_LANGUAGE.md. Nutze, wenn der User Domain-Begriffe definieren, ein Glossar bauen, Terminologie härten, eine Ubiquitous Language anlegen will oder "Domain-Modell" oder "DDD" erwähnt.
disable-model-invocation: true
---

# Ubiquitous Language

Extrahier und formalisier Domain-Terminologie aus der aktuellen Konversation in ein konsistentes Glossar, gespeichert in einer lokalen Datei.

## Prozess

1. **Konversation scannen** nach domain-relevanten Nomen, Verben und Konzepten
2. **Probleme identifizieren**:
   - Gleiches Wort für verschiedene Konzepte (Ambiguität)
   - Verschiedene Wörter für das gleiche Konzept (Synonyme)
   - Vage oder überladene Begriffe
3. **Ein kanonisches Glossar vorschlagen** mit meinungsstarken Begriffswahlen
4. **Nach `UBIQUITOUS_LANGUAGE.md`** im Working Directory schreiben, im Format unten
5. **Eine Summary** inline in der Konversation ausgeben

## Output-Format

Schreib ein `UBIQUITOUS_LANGUAGE.md` File mit dieser Struktur:

```md
# Ubiquitous Language

## Order Lifecycle

| Term        | Definition                                                       | Zu vermeidende Aliasse |
| ----------- | ---------------------------------------------------------------- | ---------------------- |
| **Order**   | Eine Customer-Anfrage, ein oder mehrere Items zu kaufen          | Purchase, transaction  |
| **Invoice** | Eine Zahlungsaufforderung, nach Lieferung an einen Customer gesendet | Bill, payment request  |

## People

| Term         | Definition                                          | Zu vermeidende Aliasse |
| ------------ | --------------------------------------------------- | ---------------------- |
| **Customer** | Eine Person oder Organisation, die Orders aufgibt   | Client, buyer, account |
| **User**     | Eine Authentifizierungs-Identität im System         | Login, account         |

## Relationships

- Ein **Invoice** gehört zu genau einem **Customer**
- Ein **Order** erzeugt ein oder mehrere **Invoices**

## Example Dialogue

> **Dev:** "Wenn ein **Customer** einen **Order** aufgibt, erstellen wir den **Invoice** sofort?"
> **Domain Expert:** "Nein — ein **Invoice** wird erst generiert, sobald ein **Fulfillment** bestätigt ist. Ein einzelner **Order** kann mehrere **Invoices** produzieren, wenn Items in separaten **Shipments** verschickt werden."
> **Dev:** "Wenn also ein **Shipment** vor dem Versand gecancelt wird, existiert kein **Invoice** dafür?"
> **Domain Expert:** "Genau. Der **Invoice**-Lifecycle ist an das **Fulfillment** gebunden, nicht an den **Order**."

## Flagged Ambiguities

- "account" wurde sowohl für **Customer** als auch **User** verwendet — das sind unterschiedliche Konzepte: ein **Customer** gibt Orders auf, während ein **User** eine Authentifizierungs-Identität ist, die einen **Customer** repräsentieren kann, aber nicht muss.
```

## Regeln

- **Sei meinungsstark.** Wenn mehrere Wörter für das gleiche Konzept existieren, wähl das beste und liste die anderen als zu vermeidende Aliasse.
- **Konflikte explizit flaggen.** Wenn ein Begriff mehrdeutig in der Konversation genutzt wird, ruf's in der "Flagged ambiguities" Section aus mit klarer Empfehlung.
- **Nur Begriffe aufnehmen, die für Domain-Experten relevant sind.** Skip die Namen von Modulen oder Klassen, außer sie haben Bedeutung in der Domain-Sprache.
- **Definitionen straff halten.** Maximal ein Satz. Definier, was es IST, nicht was es tut.
- **Beziehungen zeigen.** Begriffsnamen fett, Kardinalität ausdrücken, wo offensichtlich.
- **Nur Domain-Begriffe.** Skip generische Programmierkonzepte (Array, Function, Endpoint), außer sie haben domain-spezifische Bedeutung.
- **Begriffe in mehrere Tabellen gruppieren**, wenn natürliche Cluster entstehen (z.B. nach Subdomain, Lifecycle oder Actor). Jede Gruppe bekommt eigene Heading und Tabelle. Wenn alle Begriffe zu einer kohärenten Domain gehören, ist eine Tabelle okay - erzwing keine Gruppierungen.
- **Beispiel-Dialog schreiben.** Eine kurze Konversation (3-5 Wechsel) zwischen einem Dev und einem Domain-Experten, die zeigt, wie die Begriffe natürlich interagieren. Der Dialog sollte Grenzen zwischen verwandten Konzepten klären und zeigen, wie Begriffe präzise genutzt werden.

<example>

## Example Dialogue

> **Dev:** "Wie teste ich den **sync service** ohne Docker?"

> **Domain Expert:** "Stell den **filesystem layer** statt des **Docker layer** bereit. Er implementiert das gleiche **Sandbox service**-Interface, nutzt aber ein lokales Verzeichnis als **sandbox**."

> **Dev:** "Also erstellt **sync-in** weiterhin ein **bundle** und entpackt es?"

> **Domain Expert:** "Genau. Der **sync service** weiß nicht, mit welchem Layer er spricht. Er ruft `exec` und `copyIn` auf — der **filesystem layer** führt das einfach als lokale Shell-Commands aus."

</example>

## Re-Running

Beim erneuten Auslösen in derselben Konversation:

1. Die bestehende `UBIQUITOUS_LANGUAGE.md` lesen
2. Neue Begriffe aus nachfolgender Diskussion einarbeiten
3. Definitionen updaten, falls sich das Verständnis entwickelt hat
4. Neue Mehrdeutigkeiten neu flaggen
5. Den Beispiel-Dialog umschreiben, um neue Begriffe einzubauen
