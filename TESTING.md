# Testing Omsk Expansion

## Install

```bash
rm -rf ~/Zomboid/mods/omsk-expansion
cp -a /home/j0schi/SteamLibrary/steamapps/common/ProjectZomboid/work/KnoxMap-dev/dist/omsk-expansion \
  ~/Zomboid/mods/
```

Do not keep an old separate `isilkul-roadpass`/`omsk-roadpass` mod enabled at
the same time; it would duplicate cells.

## Start

1. Project Zomboid → **new save**.
2. Enable **Omsk Expansion**.
3. Spawn in Isilkul or the standard map.
4. Check:
   - roads are asphalt/gravel, not grass;
   - no hard cell seams or split roads;
   - buildings and interiors load;
   - spawn points work;
   - map reaches Omsk, Krasnodar, Novosibirsk, Moscow.

## What to report

If something is wrong, send:

- map + approximate tile coordinates;
- screenshot;
- `~/Zomboid/console.txt` tail;
- whether the save was created after installing this mod version.

## Useful commands

Validate the pack:

```bash
python3 -m pzmapstudio.cli layout-audit \
  --map-root /path/to/omsk-expansion/common/media/maps
python3 -m pzmapstudio.cli validate-map --map /path/to/one/map
python3 -m pzmapstudio.cli map-save-audit \
  --map-root /path/to/omsk-expansion/common/media/maps
```

The last audit is conservative; a real save `map_meta.bin` around 3–4 MB has
been observed and ran normally.
