# Active Omsk Expansion mod layout

Generated maps were built on 300-tile world cells and compiled on 256-tile
cells, so neighbouring maps shared some compiled cells. The final mod keeps one
owner per 256-tile cell and moves the losing files to:

```text
dist/overlap-trim-backup/
```

Final map folders (no duplicate cell coordinate):

```text
common/media/maps/Isilkul, Omsk Oblast                        168 cells
common/media/maps/Солнцевка и Водяное, Омская область         252
common/media/maps/Омск, Омская область                        930
common/media/maps/Краснодар, Краснодарский край                837
common/media/maps/Новосибирск, Новосибирская область          1014
common/media/maps/Москва                                      868
```

Total: 4069 unique cells.

`plans/omsk_expansion.json` is the **generation** plan and still contains the
original origins. Re-running it with `--force` would recreate overlapping
128-cell boundaries. To rebuild or move a map, use the corrected cell origins
in `plans/omsk_expansion.json` only after recompiling it; do not treat the
current trimmed folders as a fresh generation plan.

One invalid Novosibirsk spawn that fell inside a cell now owned by Moscow was
removed; seven Novosibirsk spawn points remain.
