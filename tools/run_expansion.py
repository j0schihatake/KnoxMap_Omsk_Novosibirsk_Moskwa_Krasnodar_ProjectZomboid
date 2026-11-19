#!/usr/bin/env python3
"""Run the Omsk expansion plan sequentially through the local KnoxMap API.

Run with the KnoxMap virtualenv:

    .venv/bin/python tools/run_expansion.py --dry-run
    .venv/bin/python tools/run_expansion.py
    .venv/bin/python tools/run_expansion.py --force --only omsk-city

The script never edits the game or the Workshop. It writes generated maps under
output/, packages them under dist/_packages/, and merges the map folders into
dist/omsk-expansion/.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLAN = ROOT / "plans" / "omsk_expansion.json"
SERVER = "http://127.0.0.1:5056"
MERGED = ROOT / "dist" / "omsk-expansion"
PACKAGES = ROOT / "dist" / "_packages"
LOG = ROOT / "logs" / "expansion-plan.log"


def log(message: str) -> None:
    line = f"{time.strftime('%H:%M:%S')} {message}"
    print(line, flush=True)
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a", encoding="utf-8") as handle:
        handle.write(line + "\n")


def api(path: str, body: dict | None = None, timeout: int = 60):
    data = None if body is None else json.dumps(body).encode()
    request = urllib.request.Request(
        SERVER + path, data=data,
        headers={"Content-Type": "application/json"} if body is not None else {})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.URLError as error:
        raise SystemExit(f"KnoxMap API is not reachable at {SERVER}: {error}") from error
    return json.loads(raw) if raw else {}


def wait_health() -> None:
    health = api("/api/health")
    if not health.get("ready"):
        raise SystemExit(f"KnoxMap is not ready: {health}")
    log("KnoxMap API ready")


def wait_generate(map_name: str) -> None:
    deadline = time.time() + 8 * 3600
    while time.time() < deadline:
        state = api(f"/api/progress?map={map_name}")
        stage = state.get("stage")
        if stage in ("done", "error", "idle"):
            if stage == "error":
                raise SystemExit(f"generate {map_name} failed: {state}")
            log(f"generate {map_name}: {stage}")
            return
        log(f"generate {map_name}: {stage} done={state.get('done')} total={state.get('total')} "
            f"eta={state.get('etaSeconds')}")
        time.sleep(30)
    raise SystemExit(f"generate {map_name} timed out")


def place(map_name: str, cell_x: int, cell_y: int) -> None:
    result = api(f"/api/placement/{map_name}", {"cell_x": cell_x, "cell_y": cell_y})
    if result.get("error"):
        raise SystemExit(f"placement {map_name}: {result['error']}")
    log(f"placement {map_name}: cell {cell_x},{cell_y}")


def generate(map_name: str, spec: dict, settings: dict) -> None:
    body = {
        "south": spec["south"], "west": spec["west"],
        "north": spec["north"], "east": spec["east"],
        "metersPerTile": spec["scale"], "mapName": map_name,
        "settings": settings,
    }
    log(f"generate {map_name}: downloading OSM/WorldCover then rendering")
    result = api("/api/generate", body, timeout=8 * 3600)
    if result.get("error"):
        raise SystemExit(f"generate {map_name}: {result['error']}")
    log(f"generate {map_name}: {result.get('width')}x{result.get('height')} "
        f"cells={result.get('cellsX')}x{result.get('cellsY')} "
        f"features={result.get('featureCount')}")


def build(map_name: str) -> None:
    log(f"build {map_name}: interiors and .tbx")
    result = api("/api/buildings", {"mapName": map_name}, timeout=8 * 3600)
    if result.get("error"):
        raise SystemExit(f"build {map_name}: {result['error']}")
    log(f"build {map_name}: buildings={result.get('count')} pzw={result.get('pzw')}")


def compile_map(map_name: str) -> None:
    result = api("/api/compile", {"mapName": map_name}, timeout=120)
    if result.get("error"):
        raise SystemExit(f"compile {map_name}: {result['error']}")
    log(f"compile {map_name}: expected {result.get('expected')} cells")
    deadline = time.time() + 8 * 3600
    while time.time() < deadline:
        state = api(f"/api/compile-status?map={map_name}")
        if state.get("state") == "error":
            raise SystemExit(f"compile {map_name} failed: {state}")
        if state.get("state") == "done":
            log(f"compile {map_name}: {state.get('cells')} cells")
            return
        log(f"compile {map_name}: {state.get('phase')} cells={state.get('cells')} "
            f"fraction={state.get('fraction')}")
        time.sleep(20)
    raise SystemExit(f"compile {map_name} timed out")


def package(map_name: str, spec: dict) -> Path:
    package_root = PACKAGES / map_name
    if package_root.exists():
        shutil.rmtree(package_root)
    log(f"package {map_name}")
    subprocess.run([
        sys.executable, str(ROOT / "tools" / "make_map_mod.py"),
        str(ROOT / "output" / map_name),
        "--name", spec["name"], "--id", map_name,
        "--mods-dir", str(package_root),
    ], check=True, cwd=ROOT)
    maps = list((package_root / map_name / "common" / "media" / "maps").iterdir())
    if len(maps) != 1:
        raise SystemExit(f"package {map_name}: expected one map folder, got {maps}")
    return maps[0]


def merge(map_folder: Path, spec: dict) -> None:
    target = MERGED / "common" / "media" / "maps" / spec["name"]
    if target.exists():
        shutil.rmtree(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(map_folder, target)
    log(f"merge {spec['name']} -> {target}")


def write_mod_info() -> None:
    text = (
        "name=Omsk Expansion\n"
        "id=OmskExpansion\n"
        "description=Omsk, Isilkul, Krasnodar, Novosibirsk, Moscow and villages. "
        "Map data (c) OpenStreetMap contributors (ODbL).\n"
        "poster=poster.png\n"
        "require=Erikas_Tiles\n"
    )
    for rel in ("mod.info", "common/mod.info", "42/mod.info"):
        path = MERGED / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    for name in ("poster.png", "preview.png", "ATTRIBUTION.txt"):
        source = ROOT / "dist" / "isilkulomsk" / name
        if source.exists() and not (MERGED / name).exists():
            shutil.copy2(source, MERGED / name)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--plan", type=Path, default=PLAN)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true", help="regenerate maps that already exist")
    parser.add_argument("--only", action="append", default=[], help="map id; repeatable")
    args = parser.parse_args()

    plan = json.loads(args.plan.read_text(encoding="utf-8"))
    settings = plan["settings"]
    maps = plan["maps"]
    if args.only:
        maps = [m for m in maps if m["id"] in set(args.only)]
    if not maps:
        raise SystemExit("No maps selected")

    if args.dry_run:
        for spec in maps:
            print(f"{spec['id']}: {spec['south']},{spec['west']} .. "
                  f"{spec['north']},{spec['east']} scale={spec['scale']} cell={spec['cell']}")
        return 0

    wait_health()
    MERGED.mkdir(parents=True, exist_ok=True)
    for spec in maps:
        name = spec["id"]
        log(f"=== {name} ===")
        output = ROOT / "output" / name
        if args.force or not (output / f"{name}.pzw").exists():
            generate(name, spec, settings)
            wait_generate(name)
        else:
            log(f"generate {name}: existing pzw, skipping (use --force to redo)")
        place(name, *spec["cell"])
        build(name)
        compile_map(name)
        merged_map = package(name, spec)
        merge(merged_map, spec)

    write_mod_info()
    log(f"done: {MERGED}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
