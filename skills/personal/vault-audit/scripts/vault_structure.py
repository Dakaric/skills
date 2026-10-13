"""Strukturbefund des Vaults als JSON: Waisen, tote Links, liegengebliebene aktive Notizen.

Aufruf: python3 -I vault_structure.py <vault-pfad> [--stale-days 45]
Liest nur, schreibt nichts. `08 Privat/` wird nie geöffnet.
"""
import argparse
import json
import re
import time
from collections import Counter, defaultdict
from pathlib import Path

SKIPPED_TOP_DIRS = {".git", ".obsidian", ".trash", "node_modules", ".claude", ".remember", "08 Privat"}
# Handoffs und Rohtranskripte sind Arbeitsmaterial ohne Linkpflicht, sie zählen getrennt.
EXPECTED_ORPHAN_MARKERS = (" Handoffs/", "09 Transcripts/Raw/", "06 Archiv/")
WIKILINK = re.compile(r"!?\[\[([^\]|#^]+)(?:[#^][^\]|]*)?(?:\|[^\]]*)?\]\]")
MARKDOWN_LINK = re.compile(r"\]\(([^)]+\.md)\)")
ACTIVE_STATUS = re.compile(r"^status:\s*['\"]?aktiv['\"]?\s*$", re.M)
FRONTMATTER_SCAN_CHARS = 800
SECONDS_PER_DAY = 86400


def collect_notes(vault: Path) -> list[Path]:
    return [
        path.relative_to(vault)
        for path in vault.rglob("*.md")
        if path.relative_to(vault).parts[0] not in SKIPPED_TOP_DIRS
    ]


def build_name_index(notes: list[Path]) -> dict[str, Path]:
    index: dict[str, Path] = {}
    for note in notes:
        index.setdefault(note.stem.lower(), note)
        index.setdefault(str(note.with_suffix("")).lower(), note)
    return index


def collect_attachment_names(vault: Path) -> set[str]:
    return {path.name.lower() for path in vault.rglob("*") if path.is_file() and path.suffix != ".md"}


def extract_link_targets(text: str) -> set[str]:
    wikilinks = {target.strip() for target in WIKILINK.findall(text)}
    markdown_links = {Path(target).stem for target in MARKDOWN_LINK.findall(text)}
    return wikilinks | markdown_links


def resolve_target(raw_target: str, name_index: dict[str, Path]) -> Path | None:
    key = raw_target.lower().removesuffix(".md")
    return name_index.get(key) or name_index.get(Path(key).name)


def is_expected_orphan(note: Path) -> bool:
    return any(marker in str(note) for marker in EXPECTED_ORPHAN_MARKERS)


def days_since_modified(path: Path) -> int:
    return round((time.time() - path.stat().st_mtime) / SECONDS_PER_DAY)


def analyze(vault: Path, stale_days: int) -> dict:
    notes = collect_notes(vault)
    name_index = build_name_index(notes)
    attachment_names = collect_attachment_names(vault)
    inbound, outbound = Counter(), Counter()
    broken_links, stale_active = [], []

    for note in notes:
        text = (vault / note).read_text(errors="ignore")
        for raw_target in extract_link_targets(text):
            target = resolve_target(raw_target, name_index)
            if target:
                inbound[target] += 1
                outbound[note] += 1
            elif Path(raw_target).name.lower() not in attachment_names:
                broken_links.append({"note": str(note), "target": raw_target})
        age = days_since_modified(vault / note)
        if age > stale_days and ACTIVE_STATUS.search(text[:FRONTMATTER_SCAN_CHARS]):
            stale_active.append({"note": str(note), "days_untouched": age})

    return summarize(notes, inbound, outbound, broken_links, stale_active)


def summarize(notes, inbound, outbound, broken_links, stale_active) -> dict:
    orphans = [note for note in notes if inbound[note] == 0 and outbound[note] == 0]
    real_orphans = [str(note) for note in orphans if not is_expected_orphan(note)]
    return {
        "notes_total": len(notes),
        "orphans_total": len(orphans),
        "expected_orphans_total": len(orphans) - len(real_orphans),
        "real_orphans": sorted(real_orphans),
        "orphans_by_top_folder": dict(Counter(note.parts[0] for note in orphans).most_common()),
        "broken_links": sorted(broken_links, key=lambda link: link["note"]),
        "stale_active": sorted(stale_active, key=lambda entry: -entry["days_untouched"]),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("vault", type=Path)
    parser.add_argument("--stale-days", type=int, default=45)
    args = parser.parse_args()
    print(json.dumps(analyze(args.vault, args.stale_days), ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
