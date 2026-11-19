#!/usr/bin/env python3
"""Remove duplicate 256-tile cells from map folders, keeping one owner.

KnoxMap places maps on 300-tile world cells but compiles files on the 256-tile
grid. Adjacent maps can therefore contain the same compiled cell. PZ must see
exactly one cell file for each coordinate, so the duplicate is moved to
dist/overlap-trim-backup/ and removed from the losing map.

Run:
    .venv/bin/python tools/trim_overlaps.py --dry-run
    .venv/bin/python tools/trim_overlaps.py
"""
from __future__ import annotations

import argparse
import shutil
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAPS = ROOT / "dist" / "omsk-expansion" / "common" / "media" / "maps"
BACKUP = ROOT / "dist" / "overlap-trim-backup"

# Higher priority owns a shared compiled cell. Main cities win over their
# rural neighbours; Moscow wins its eastern overlap with Novosibirsk.
PRIORITY = [
    "Омск, Омская область",
    "Краснодар, Краснодарский край",
    "Москва",
    "Новосибирск, Новосибирская область",
    "Солнцевка и Водяное, Омская область",
    "Isilkul, Omsk Oblast",
]
RANK = {name: index for index, name in enumerate(PRIORITY)}


def cell_key(path: Path) -> tuple[int, int] | None:
    parts = path.stem.split("_")
    if len(parts) < 2:
        return None
    try:
        return int(parts[-2]), int(parts[-1])
    except ValueError:
        return None


def owner(names: list[str]) -> str:
    return min(names, key=lambda name: RANK.get(name, 999))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    maps = [path for path in MAPS.iterdir() if path.is_dir()]
    cells: dict[tuple[int, int], list[tuple[str, Path]]] = defaultdict(list)
    for map_dir in maps:
        for header in map_dir.glob("*.lotheader"):
            key = cell_key(header)
            if key is not None:
                cells[key].append((map_dir.name, header))
    duplicates = {key: entries for key, entries in cells.items() if len(entries) > 1}
    removed = Counter()
    kept = Counter()
    for key in sorted(duplicates):
        names = [name for name, _ in duplicates[key]]
        winner = owner(names)
        kept[winner] += 1
        for name, header in duplicates[key]:
            if name == winner:
                continue
            stem = header.stem
            for path in list((MAPS / name).glob(stem + ".*")):
                removed[name] += 1
                if args.dry_run:
                    print(f"would remove {path}")
                    continue
                target = BACKUP / name / path.name
                target.parent.mkdir(parents=True, exist_ok=True)
                if target.exists():
                    target.unlink()
                shutil.move(str(path), str(target))
            print(f"cell {key}: keep {winner}, remove {name}")
    print(f"duplicates={len(duplicates)} removed={sum(removed.values())}")
    if removed:
        print("removed per map:", dict(removed))
    print("kept per owner:", dict(kept))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
