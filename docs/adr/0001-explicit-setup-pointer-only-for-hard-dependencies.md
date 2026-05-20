# Expliziter `/setup-matt-pocock-skills` Pointer nur für Hard Dependencies

Engineering-Skills hängen von per-Repo-Konfig ab (Issue Tracker, Triage-Label-Vokabular, Domain-Doc-Layout), die `/setup-matt-pocock-skills` seedet. Manche Skills können ohne diese Konfig nicht sinnvoll funktionieren - sie müssen in einen bestimmten Issue Tracker publishen oder einen bestimmten Label-String anwenden. Andere nutzen sie nur, um den Output zu schärfen (Vokabular, ADR-Awareness), und degradieren ohne sie sanft.

Wir teilen das auf in **Hard-Dependency**- und **Soft-Dependency**-Skills:

- **Hard Dependency** (`to-issues`, `to-prd`, `triage`) — enthalten einen expliziten Einzeiler: _"… should have been provided to you — run `/setup-matt-pocock-skills` if not."_ Ohne das Mapping ist der Output falsch, nicht nur unscharf.
- **Soft Dependency** (`diagnose`, `tdd`, `improve-codebase-architecture`, `zoom-out`) — referenzieren "das Domain-Glossar des Projekts" und "ADRs im betroffenen Bereich" nur in unverbindlicher Prosa. Wenn die Docs nicht da sind, funktioniert der Skill trotzdem; der Output ist nur weniger scharf.

Die Aufteilung hält Soft-Dependency-Skills token-light und vermeidet, den Setup-Pointer per Cargo-Cult an Stellen einzubauen, wo er nicht load-bearing ist.
