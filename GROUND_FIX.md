# Ground under props

The first beautify pass replaced ground tiles under benches/lamps/bins/fences.
A second pass restored a terrain/road tile from the nearest neighbour.

Result:

```text
repaired cells: 2991
prop-only squares fixed: 1,051,628
```

Samples now report `prop_only=0`.

This only changes `.lotpack` tile records; room/building headers are preserved.
