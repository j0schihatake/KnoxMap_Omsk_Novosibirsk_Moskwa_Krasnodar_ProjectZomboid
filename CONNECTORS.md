# Map connectors and rural edge strips

Status: planned after Omsk/Krasnodar compile.

Real Omsk–Isilkul road is about 140 km. At 1.75 m/tile that is ~80,000
tiles, far past the map limit, and the city bboxes are placed next to each
other in the game world anyway. The connector is therefore a stylised strip,
not a 1:1 road.

## Omsk–Isilkul link

```text
Isilkul:      x 0..11,  y 54..64
link strip:   x 12..15, y 54..83
Omsk:         x 16..43, y 54..83   (moved 4 cells right)
```

The strip carries:

- one through road from Isilkul east edge to Omsk west edge;
- shelterbelts/plantings along the road;
- fields between shelterbelts;
- forest at both outer edges;
- occasional farm buildings/tracks.

It must be generated at 1.75 m/tile so the seam matches the city maps. Better
as a drawn/design map than a real OSM bbox, because the real distance does not
fit.

## Villages

```text
Isilkul:          x 0..11,  y 54..64
IsilkulVillages:  x 0..15,  y 64..78
```

Road connects at the Isilkul south edge (`y=64`) and enters Solntsevka/Vodnoye.

## Rules

- No overlapping cells.
- A road must end exactly on both seam cells.
- Forest/fields must not leave a visible void at the seam.
- Recompile both sides after moving.

## Wide rural belt (revised)

A one-cell "кишка" is rejected. The connector is a **wide rural belt**, split
into several map rectangles that cover every playable cell between the cities
and the outer boundary:

- no empty cells between city maps and the belt;
- lakes, villages, roads, fields and forest taken from OSM;
- forest/field edges used to hide the 1.75 -> 8 m/tile detail transition;
- each rural map has no complex interiors, so it stays under the building-state
  limit and is cheap to load.

The belt is split into maps rather than one giant map, so the save limit and
memory budget stay bounded.
