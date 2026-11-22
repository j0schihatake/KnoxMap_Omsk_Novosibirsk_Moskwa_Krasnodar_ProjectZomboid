# Final audit — round 12

## Maps

```text
Omsk_World        4069 cells   47 spawns   validate ok
Cascade Hills      650 cells    3 spawns   validate ok
Danforth           400 cells    5 spawns   validate ok
Dread Dawn         576 cells    6 spawns   validate ok
Drucker County     650 cells    3 spawns   validate ok
Harran City        576 cells    8 spawns   validate ok
Meagher Valley     650 cells    3 spawns   validate ok
Providence Ridge   650 cells    3 spawns   validate ok
The Following      576 cells    6 spawns   validate ok
Trumbull Valley    930 cells    6 spawns   validate ok
```

All ten maps have `worldmap.xml.bin`.

## Floor audit

```text
0 missing floor textures on every map
```

## Save-state audit

```text
Omsk_World       fraction 3.3228  (conservative estimate; tested save was 3.46 MB)
all SoD2 maps    fraction ~0.303
```

PZBigBuffer raises the fixed save buffer to 64 MB.

## Roads

- 3-tile shoulders/trotuars on rebuilt maps;
- road markings on all SoD maps;
- wider roads on all SoD maps;
- connected canals and bridges between Dread Dawn and The Following.

## Props

- street benches, tables, chairs and lamps added;
- decorative props thinned by `170 578` for optimization.

## Local cell git

```text
f1fa74f cells: final validation pass
```

## Remaining in-game check

New save + drive test is still recommended before public Workshop upload.
