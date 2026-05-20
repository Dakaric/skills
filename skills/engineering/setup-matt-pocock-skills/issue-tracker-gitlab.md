# Issue Tracker: GitLab

Issues und PRDs für dieses Repo leben als GitLab Issues. Nutz das [`glab`](https://gitlab.com/gitlab-org/cli) CLI für alle Operationen.

## Konventionen

- **Issue erstellen**: `glab issue create --title "..." --description "..."`. Heredoc für mehrzeilige Descriptions nutzen. `--description -` öffnet einen Editor.
- **Issue lesen**: `glab issue view <number> --comments`. `-F json` für machine-readable Output.
- **Issues listen**: `glab issue list -F json` mit passenden `--label` Filtern.
- **Auf Issue kommentieren**: `glab issue note <number> --message "..."`. GitLab nennt Comments "Notes".
- **Labels anwenden / entfernen**: `glab issue update <number> --label "..."` / `--unlabel "..."`. Mehrere Labels können kommagetrennt oder durch wiederholtes Flag übergeben werden.
- **Schließen**: `glab issue close <number>`. `glab issue close` akzeptiert keinen Closing Comment, also poste zuerst die Erklärung mit `glab issue note <number> --message "..."`, dann schließen.
- **Merge Requests**: GitLab nennt PRs "Merge Requests". Nutz `glab mr create`, `glab mr view`, `glab mr note` etc. - gleiche Form wie `gh pr ...` mit `mr` statt `pr` und `note`/`--message` statt `comment`/`--body`.

Das Repo aus `git remote -v` ableiten - `glab` macht das automatisch, wenn es innerhalb eines Clones läuft.

## Wenn ein Skill sagt "im Issue Tracker veröffentlichen"

Ein GitLab Issue erstellen.

## Wenn ein Skill sagt "das relevante Ticket holen"

`glab issue view <number> --comments` ausführen.
