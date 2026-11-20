# Omsk Expansion 1.1.0

## What's new

- Beautify pass on all six maps: benches, outdoor lamps and bins.
- 256x256 Workshop preview with the map and all six city names.
- PZMapStudio 0.2.0 is published as a separate Workshop item (map item contains maps only).
- Workshop layout uses `Contents/mods/OmskExpansion/`.

## Maps

```text
Isilkul           168 cells
Solntsevka        252 cells
Omsk              930 cells
Krasnodar         837 cells
Novosibirsk      1014 cells
Moscow            868 cells
```

```text
4069 cells, 0 duplicate cells, 0 unconnected maps
```

`map-save-audit` still reports a conservative upper bound above 90%; a real
tested save previously produced a ~3.46 MB `map_meta.bin` and ran normally.
Do not trim cities without an actual save overflow.

## Install

```bash
rm -rf ~/Zomboid/mods/omsk-expansion
cp -a dist/omsk-expansion ~/Zomboid/mods/
```

Create a new save, enable `Omsk Expansion`, spawn in Isilkul. Disable old
`isilkul-roadpass` / `omsk-roadpass` to avoid duplicate cells.

## Workshop upload

```bash
bash ../PZMapStudio/tools/stage_workshop.sh \
  dist/omsk-expansion OmskExpansion
```

Then main menu → Workshop → `OmskExpansion` → Upload.

The item root needs `preview.png` (256x256) and
`Contents/mods/OmskExpansion/mod.info`.

## Known warnings

- Steam may hide the Workshop legal/publish popup behind a fullscreen game;
  switch to windowed mode or Alt-Tab before confirming.
- `map-save-audit` is conservative; verify with a real save.
