# Key gameplay elements audit

Checked room names inside compiled lots, not just building titles.

## Omsk_World

```text
weapons   568
food      132434
medical   9980
police    472
school    35078
religion  827
military  24135
warehouse 344814
```

Omsk keeps named gun stores, food shops, pharmacies, police rooms, schools
and churches from the OSM-derived build. Positions are the generated OSM
positions.

## Hand-authored regions

```text
map                 weapons  food  medical  police  school  church  military
Danforth               15     30      28      12      40      16       8
Harran City            16     16      14       0*     18      10      12
The Following           0      0       0       0       0      18       0
Trumbull Valley         0      3       6       0      12       8      18
Meagher Valley          0      1       6       0       0       0       6
Drucker County          0      1       0       0       0       0       4
Cascade Hills           0      0       0       0       0       6       6
Providence Ridge        0      0       0       0       0       0      10
```

`*` Harran headers contain `police` rooms, but the first audit pass reported
zero; a rescan is needed after the next rebuild.

## Positioning

- Omsk: OSM-derived, geographically positioned.
- Trumbull/SoD2/Danforth/Harran/The Following: hand-authored inspired
  layouts, not georeferenced copies of the reference maps. Landmark positions
  are plausible but not exact reference positions.

## Gaps

1. The Following needs food and weapon rooms.
2. SoD regions still lack gun/food/pharmacy/police rooms.
3. Harran police room audit needs a rescan.
4. After adding, regenerate affected maps and rerun
   `tools/audit_key_elements.py`.
