# Spawn regions for the merged world

The compiled map is one folder, but the spawn menu should show the cities.
`Omsk_World/spawnregions.lua` defines seven regions:

```text
Isilkul
Solntsevka / Vodnoye
Omsk
Krasnodar
Novosibirsk
Moscow
Trumbull Valley
```

Each region points to its own `spawnpoints_*.lua` inside `Omsk_World`.

This keeps one continuous world without duplicate compiled cells while giving
separate city spawn entries.

After changing these files, copy the whole mod again and create a new save.
