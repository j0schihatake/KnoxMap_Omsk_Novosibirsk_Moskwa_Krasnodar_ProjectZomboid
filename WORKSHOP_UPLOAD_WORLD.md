# Upload Omsk Expansion World

## What gets uploaded

The Workshop item contains the full compiled world, not just metadata:

```text
Contents/mods/OmskExpansion/common/media/maps/Omsk_World/
  *.lotheader       4999 files
  world_*.lotpack
  spawnregions.lua
  spawnpoints_isilkul.lua
  spawnpoints_solntsevka.lua
  spawnpoints_omsk.lua
  spawnpoints_krasnodar.lua
  spawnpoints_novosibirsk.lua
  spawnpoints_moscow.lua
  spawnpoints_trumbull.lua
  map.info
```

## Prepare staging

```bash
cd /home/j0schi/SteamLibrary/steamapps/common/ProjectZomboid/work/PZMapStudio

bash tools/stage_workshop.sh \
  /home/j0schi/SteamLibrary/steamapps/common/ProjectZomboid/work/KnoxMap-dev/dist/omsk-expansion \
  OmskExpansion
```

## Verify

```bash
cat ~/Zomboid/Workshop/OmskExpansion/workshop.txt

find ~/Zomboid/Workshop/OmskExpansion/Contents \
  -name '*.lotheader' | wc -l

ls -l ~/Zomboid/Workshop/OmskExpansion/Contents/mods/OmskExpansion/common/media/maps/Omsk_World/spawnregions.lua
ls -l ~/Zomboid/Workshop/OmskExpansion/preview.png
```

Expected:

```text
id=3842859537
title=KnoxMap OMSK EXPANSION
4999
spawnregions.lua exists
preview.png 256x256
```

## City list for the description

```text
Omsk Expansion World

Один непрерывный мир. Спавн по городам:
- Исилькуль
- Солнцевка / Водяное
- Омск
- Краснодар
- Новосибирск
- Москва
- Trumbull Valley

4999 клеток.
Карты: Omsk_World.
Данные: © OpenStreetMap contributors, ODbL.
```

## Upload

```text
Project Zomboid → Workshop
→ KnoxMap OMSK EXPANSION
→ Upload/Update
```

The item keeps ID `3842859537`.

Cells are uploaded as part of `Contents/mods/OmskExpansion`.
