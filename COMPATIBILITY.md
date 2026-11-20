# Compatibility: Omsk Expansion + SoD2 pack

```text
Omsk Expansion  7 maps, 4999 cells, x=0..138
SoD2 pack       4 maps, 2600 cells, x=139..163
```

Combined audit over both map roots:

```text
maps: 11
duplicate cells: 0
unconnected maps: 0
road boundary pairs: 40
road pairs with matching edge roads: 40
```

Why they do not overlap:

- Omsk Expansion cells end at `x=138`;
- SoD2 cells start at `x=139`;
- separate map folders, separate `.lotheader/.lotpack` names;
- separate `mod.info` IDs: `OmskExpansion` and `SoD2Maps`.

Enable both in the same new save. Do not reuse an old save.
