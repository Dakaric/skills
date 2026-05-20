# Issue Tracker: GitHub

Issues und PRDs für dieses Repo leben als GitHub Issues. Nutz das `gh` CLI für alle Operationen.

## Konventionen

- **Issue erstellen**: `gh issue create --title "..." --body "..."`. Heredoc für mehrzeilige Bodies nutzen.
- **Issue lesen**: `gh issue view <number> --comments`, Comments per `jq` filtern und auch Labels holen.
- **Issues listen**: `gh issue list --state open --json number,title,body,labels,comments --jq '[.[] | {number, title, body, labels: [.labels[].name], comments: [.comments[].body]}]'` mit passenden `--label` und `--state` Filtern.
- **Auf Issue kommentieren**: `gh issue comment <number> --body "..."`
- **Labels anwenden / entfernen**: `gh issue edit <number> --add-label "..."` / `--remove-label "..."`
- **Schließen**: `gh issue close <number> --comment "..."`

Das Repo aus `git remote -v` ableiten - `gh` macht das automatisch, wenn es innerhalb eines Clones läuft.

## Wenn ein Skill sagt "im Issue Tracker veröffentlichen"

Ein GitHub Issue erstellen.

## Wenn ein Skill sagt "das relevante Ticket holen"

`gh issue view <number> --comments` ausführen.
