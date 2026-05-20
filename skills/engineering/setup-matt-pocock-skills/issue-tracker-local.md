# Issue Tracker: Local Markdown

Issues und PRDs für dieses Repo leben als Markdown-Files in `.scratch/`.

## Konventionen

- Ein Feature pro Verzeichnis: `.scratch/<feature-slug>/`
- Das PRD ist `.scratch/<feature-slug>/PRD.md`
- Implementation-Issues sind `.scratch/<feature-slug>/issues/<NN>-<slug>.md`, nummeriert ab `01`
- Triage-State wird als `Status:` Zeile oben im jeweiligen Issue-File festgehalten (siehe `triage-labels.md` für die Rollen-Strings)
- Comments und Konversations-Historie hängen unten im File unter einer `## Comments` Heading an

## Wenn ein Skill sagt "im Issue Tracker veröffentlichen"

Ein neues File unter `.scratch/<feature-slug>/` anlegen (Verzeichnis bei Bedarf erstellen).

## Wenn ein Skill sagt "das relevante Ticket holen"

Das File am referenzierten Pfad lesen. Der User übergibt normalerweise den Pfad oder die Issue-Nummer direkt.
