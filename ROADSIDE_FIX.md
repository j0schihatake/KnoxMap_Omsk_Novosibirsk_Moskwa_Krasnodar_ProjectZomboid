# Roadside foliage cleanup

Omsk city roads had grass/bush overlays on and directly beside asphalt, which
made the city look abandoned. A one-tile radius cleanup removed vegetation
tiles but kept the base terrain and road tiles.

```text
Omsk city cells processed: 900
changed cells:             636
removed vegetation tiles:  876 507
```

Only Omsk city (`x=14..43, y=63..92`) was cleaned in this pass. The other
cities keep their existing vegetation.

Headers, rooms and buildings are preserved.
