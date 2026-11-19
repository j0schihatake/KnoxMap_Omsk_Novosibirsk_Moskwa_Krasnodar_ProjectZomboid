# Isilkul villages (backlog)

Status: planned, not generated. Add after the Omsk compile finishes.

## Places

OpenStreetMap/Nominatim:

```text
Солнцевка, Исилькульский район
54.990009, 71.287582
bbox 54.9754..54.9996, 71.2668..71.3138

Водяное, Исилькульский район
55.007309, 71.343147
bbox 55.0023..55.0136, 71.3322..71.3486
```

Both are outside the current Isilkul bbox (`north=54.935`).

## Proposed map

```text
map id: isilkul-villages
bbox: 54.960, 71.250 .. 55.025, 71.370
scale: 1.75 m/tile
tiles: ~4,600 × 4,000
cells: ~16 × 14
placement: cell_x = 0, cell_y = 64   // directly below Isilkul (0,54..64)
```

It includes Solntsevka, Vodnoye and the fields/roads between them. A road
connector is required at the Isilkul south edge (`y=64`), because map seams do
not generate connecting roads automatically.
