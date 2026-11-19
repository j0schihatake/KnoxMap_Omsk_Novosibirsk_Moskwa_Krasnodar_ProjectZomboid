# Russian multi-entrance apartment layout (backlog)

Status: not implemented. Apply after the Omsk/Krasnodar/filler maps are built.

## Goal

For `building=apartments` in Russian cities, generate the classic layout:

```text
long panel/brick block
├─ podyezd 1: entrance + stair core + landing + 4 flats
├─ podyezd 2: entrance + stair core + landing + 4 flats
├─ ...
└─ shared facade, roof, basement
```

Floors: 2–5–9 (optionally 12+ with lift).

## Requirements

- Split a long footprint into entrance sections, not one stair core for the whole building.
- One stair core per section, aligned on every storey.
- Stair landing opens onto 4 flats in the classic pattern:
  - 1-room, 2-room, 3-room variants;
  - kitchen, bathroom, hallway, living/bedrooms;
  - no doors between flats.
- Street entrance per section, with a small entrance lobby on the ground floor.
- Lift for 9+ storeys.
- Basement/storage optional.
- Furniture must never block stairs or the landing.
- Every flat has exactly one front door onto the landing.
- Every room reachable from the flat's front door.
- Audit must report zero furniture-on-stairs and zero flats without a door.

## Integration

Add a generator setting, e.g.:

```text
apartment_layout = auto | generic | russian
```

`russian` applies only to `apartment` kind; fall back to generic if the footprint is too small for a section.
