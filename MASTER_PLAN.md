# Master plan

## Current world

```text
Omsk_World   4069 cells
SoD2         5658 cells
total        9727 cells
```

Maps: Omsk world, Trumbull, Meagher, Drucker, Cascade, Providence, Danforth,
Harran City, The Following, Dread Dawn.

## Phase 1 — key locations by hand

Status: in progress.

- Danforth: evacuation center, hospital, church, school, police, depot,
  gun/food/pharmacy rooms.
- Harran: Tower, hospital, school, stadium, Old Town mosque/market, depot,
  police, gun/food/pharmacy rooms.
- The Following: chapel, farm, grain store, village market, clinic,
  constable, gun/food rooms.
- Dread Dawn: school camp, hospital, checkpoint, police, gun shop, food
  market, bus station, canal.
- Remaining: old SoD towns need gun/food/pharmacy/police rooms.

## Phase 2 — roads and spawn points

- Widen generated roads for car/NPC traffic.
- Use wider multi-lane arterials and ring roads.
- Add a spawn point for every city/location, so a new game can start in each
  map:
  - Omsk World: six existing city spawn files.
  - Trumbull, Meagher, Drucker, Cascade, Providence: multiple points each.
  - Danforth: camp, hospital, market.
  - Harran: Tower, Old Town, hospital, stadium.
  - The Following: village, farm, dam.
  - Dread Dawn: school camp, hospital, checkpoint, market.
- Add spawn points to every new village, military base and prison.

## Phase 3 — villages, military bases and prisons

Add by hand, with fences and access roads:

- 2 villages.
- 7 military bases across the map pack.
- 2 large prisons with perimeter fences.
- Road connections from the nearest main road.
- Spawn points inside each location.

### Current status

```text
2 prisons      Harran Central Prison, Danforth State Prison
2 villages     The Following village, Harran Outskirts
2 new bases    Harran Military Base, Dread Dawn Military Base
existing       Danforth evacuation base, Dread north checkpoint,
               SoD bases (need visual upgrade)
```

Roads and fences are present. Spawn points added.

Remaining: 5 more bases with the full military layout and the visual upgrade
of the old SoD bases.

### Military bases must read as bases

Every base needs:

- outer fence and controlled gate;
- vehicle checkpoint / barriers;
- barracks and command building;
- armory / supply depot;
- motor pool or helipad;
- parade ground or vehicle yard;
- watch post / tower;
- not just a generic warehouse with a `base` label.

### Prisons must read as prisons

Every prison needs:

- high perimeter wall/fence with corner watch posts;
- gatehouse with sally port;
- cell blocks with rows of cells;
- exercise yard;
- mess hall, infirmary, laundry, workshop;
- solitary/administration block;
- visitor entrance and vehicle road;
- not just a large warehouse.

## Phase 4 — manual verification

- `validate-map` for every map.
- Floor-texture audit.
- Key-element audit.
- Duplicate room/cell audit.
- Spawn-point coverage audit.
- Road continuity and drive test.
- In-game map display check (`worldmap.xml.bin` for every map).

## Phase 5 — beauty and originality

- Remove grass/bush overgrowth from roads and city edges.
- Keep fields and forests outside the built-up areas.
- Add concrete/plaza surfaces, fences, courtyards and distinctive landmark
  facades.
- Make hero buildings less generic.

## Phase 6 — optimization

- Reduce redundant decorative objects.
- Keep forest/field object density bounded.
- Check `map_meta` save size with PZBigBuffer.
- New save + drive test.
- Commit compiled cells to the local cell git.

## Phase 7 — survivor camps

Before the final optimization, add survivor camps that are easy for a player
to claim and hard for zombies to enter:

- high palisade wall around the whole camp;
- one narrow gate / choke point, with a fence maze or vehicle barrier;
- no open gaps in the perimeter;
- inside: 2–4 small cabins, garden plots, rain collectors, storage,
  campfire, workbench, watch post;
- cleared interior (no grass/bush tiles inside the palisade);
- accessible by a narrow path/road, not a wide highway;
- 2 camps visible near roads;
- 2 camps hidden in forest, away from the main road;
- spawn point inside every camp;
- no zombie-sensitive spawn right at the gate.

## Phase 8 — final defect pass

Walk every map one last time and look for:

- missing ground under props;
- grass/bush overgrowth on roads;
- floating or broken objects;
- empty buildings with no doors;
- unconnected roads;
- missing spawn points;
- bases that do not look like bases;
- prisons that do not look like prisons;
- map display missing for any map.

## Phase 9 — final optimization

After the defect pass:

- reduce object count in fields/forests;
- remove duplicate props and unused statics;
- check cell count and `map_meta`;
- rebuild `worldmap.xml.bin` where cells changed;
- run the full audit suite again;
- commit the final compiled cells to the local cell git.

