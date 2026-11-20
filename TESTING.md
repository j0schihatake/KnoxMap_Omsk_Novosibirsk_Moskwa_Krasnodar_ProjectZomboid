# Testing checklist

## 1. Install

```bash
rm -rf ~/Zomboid/mods/omsk-expansion
cp -a dist/omsk-expansion ~/Zomboid/mods/
```

Close the game first. Disable old `isilkul-roadpass` / `omsk-roadpass`.

## 2. New save

- enable `Omsk Expansion`;
- spawn in Isilkul;
- do not reuse an old save.

## 3. World checks

- roads connect to the vanilla map;
- no missing cells around city edges;
- no duplicate cells at map borders;
- interiors have rooms and doors;
- benches/lamps/bins appear along streets.

## 4. Java tool

Install PZMapStudio separately:

```bash
rm -rf ~/Zomboid/mods/PZMapStudio
cp -a ../PZMapStudio/dist/PZMapStudioMod ~/Zomboid/mods/PZMapStudio
```

Enable it in the same new save.

- `F10` opens the panel;
- `F11` prints observer JSON;
- `Horde x5` spawns zombies;
- `Loot bandage x3` spawns loot;
- `Story camp` adds camp loot;
- `Weather storm` changes weather;
- `Door` toggles a door at the player.

## 5. Agent queue

```bash
python3 tools/live_queue.py --op observe --wait 3
```

Then:

```bash
python3 tools/live_queue.py --op story --kind camp --x 100 --y 100 --wait 3
python3 tools/live_queue.py --op weather --kind storm --seconds 60
```

Responses go to `~/Zomboid/PZMapStudio/responses.jsonl` and `console.txt`.

## 6. Map write

Use `Stage cell` / `Apply cell` on a test cell and verify:

- backup appears under `PZMapStudioBackup/<timestamp>/`;
- rooms/buildings remain;
- game reloads the cell without errors.

Report `console.txt` lines starting with `[PZMapStudio]`.
