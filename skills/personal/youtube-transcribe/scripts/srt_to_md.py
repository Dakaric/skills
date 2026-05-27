#!/usr/bin/env python3
"""SRT -> sauberer, fortlaufender Text.

Entfernt Indizes und Timestamps, dedupliziert aufeinanderfolgende identische
Zeilen (rolling captions wiederholen oft die Vorzeile), strippt Tags und
normalisiert Whitespace. Gibt einen einzigen Fliesstext auf stdout aus.

Usage: srt_to_md.py <datei.srt>
"""
import re
import sys


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("Usage: srt_to_md.py <datei.srt>")
    with open(sys.argv[1], encoding="utf-8") as f:
        raw = f.read()

    lines: list[str] = []
    for block in re.split(r"\n\s*\n", raw):
        rows = block.strip().splitlines()
        if rows and rows[0].strip().isdigit():
            rows = rows[1:]
        for row in rows:
            if "-->" in row:
                continue
            row = re.sub(r"<[^>]+>", "", row).strip()
            if row and (not lines or lines[-1] != row):
                lines.append(row)

    print(re.sub(r"\s+", " ", " ".join(lines)).strip())


if __name__ == "__main__":
    main()
