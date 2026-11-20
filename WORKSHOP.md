# Steam Workshop publishing — Omsk Expansion

Current playable package:

```text
dist/omsk-expansion
```

Prepared metadata:

```text
dist/workshop/workshop_build_item.vdf
dist/workshop/README.md
```

Mod id:

```text
OmskExpansion
```

Size: about **6.2 GB**, 4069 compiled cells.

## Option A — in-game uploader (recommended)

1. Copy the mod into the game's mod folder:

   ```bash
   rm -rf ~/Zomboid/mods/OmskExpansion
   cp -a /home/j0schi/SteamLibrary/steamapps/common/ProjectZomboid/work/KnoxMap-dev/dist/omsk-expansion \
     ~/Zomboid/mods/
   ```

2. Start Project Zomboid from Steam.
3. Main menu → **Mods**.
4. Select **Omsk Expansion**.
5. Press **Upload** / **Upload to Workshop**.
6. Fill in:
   - title: `Omsk Expansion — Isilkul, Omsk, Krasnodar, Novosibirsk, Moscow`
   - description: see below;
   - preview: `poster.png`;
   - tags: `Maps`;
   - visibility: Public.
7. Publish. Steam returns a Workshop item id.
8. Start a **new save**, enable the mod, test spawn and map transitions.

If the Mods screen has no Upload button, open the main menu **Workshop** page;
on some B42 builds the uploader is there.

## Option B — SteamCMD

Install SteamCMD from Valve, then:

```bash
steamcmd +login <your_steam_login> \
  +workshop_build_item /home/j0schi/SteamLibrary/steamapps/common/ProjectZomboid/work/KnoxMap-dev/dist/workshop/workshop_build_item.vdf \
  +quit
```

The password and Steam Guard code are entered interactively; never commit them.

The VDF currently has:

```text
publishedfileid 0
```

For a new item that is correct. After the first upload Steam prints the new
`publishedfileid`; put that number into the VDF for later updates.

Only run `workshop_build_item`. Do not run `app_update` or `validate` unless you
intend to modify the game installation.

## Workshop description

```text
Six connected Project Zomboid maps from real OpenStreetMap data:
Isilkul, Solntsevka/Vodnoye, Omsk, Krasnodar, Novosibirsk and Moscow.

Forests, fields, villages, roads, furnished interiors, zombies and spawn points.
Start a NEW save. Vanilla map is at the top; new maps continue to the south and
east.

Map data © OpenStreetMap contributors, ODbL.
```

## Size warning

6.2 GB may exceed Steam Workshop's practical item limit. If publishing fails or
stalls, split the pack:

```text
OmskExpansion-Core       Isilkul + villages + Omsk
OmskExpansion-South      Krasnodar
OmskExpansion-East       Novosibirsk + Moscow
```

Each part needs its own `mod.info`, `map.info`, spawn points and Workshop item.

## Before publishing

- test in a new save;
- make sure only one copy of each map is enabled;
- keep OSM attribution and `ATTRIBUTION.txt`;
- do not include Google Street View or other unlicensed imagery;
- remove local reference photos from the published content.
