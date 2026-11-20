# In-game paper map fix

Build 42 reads `worldmap.xml.bin`, not the XML alone. Without it the M map is
blank or shows only street names.

Every shipped map folder now has:

```text
worldmap.xml
worldmap.xml.bin
```

Generated from the compiled cells as simple residential polygons. This is a
functional paper map, not the detailed OSM street rendering; the detailed XML
was too large to convert reliably.

Current maps:

```text
Omsk_World       4069 cells
Trumbull Valley   930 cells
Meagher Valley    650
Drucker County    650
Cascade Hills     650
Providence Ridge  650
```

The binary is what the game reads. XML is kept for tools that inspect it.
