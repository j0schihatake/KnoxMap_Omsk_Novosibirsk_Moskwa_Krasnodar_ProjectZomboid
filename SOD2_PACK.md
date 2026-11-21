# State of Decay + Dying Light map pack

Status:

```text
Trumbull Valley    930 cells
Meagher Valley     650 cells
Drucker County     650 cells
Cascade Hills      650 cells
Providence Ridge   650 cells
Danforth           400 cells
Harran City        576 cells
The Following      576 cells
Dread Dawn         576 cells
total             5658 cells
```

Each region has hand-authored bases and landmarks:

```text
Trumbull Valley    Marshall, Spencer's Mill, fairgrounds, church
Meagher Valley     Whitney Field, Camp Kelenqua, Mazzara Farm,
                   Squelones Brewing, Sasser Regional Hospital
Drucker County     Mike's Concrete, Barricaded Strip Mall,
                   Knights Drive-In, Wheelhouse Truck Stop,
                   Lundegaard Mansion
Cascade Hills      Container Fort, Bridge Fort, Church on the Hill,
                   Corner Office, Cash Beaumont's
Providence Ridge   Firewatch Fortress, Rusty Rosie's, Lumber Mill,
                   Red Talon FOB, Tranquility Factory
Danforth           Evacuation Center, Memorial Hospital, St. Michael,
                   High School, Police Office, Supply Depot
Harran City        The Tower, St. Joseph's Hospital, Harran High School,
                   Harran Stadium, Old Town Mosque, Old Town Market,
                   Harran Depot, Police Station
The Following      Countryside Chapel, Bilal Farm, Grain Store,
                   Village Market, farmhouses, fields, river and forest
Dread Dawn         School Camp, Hospital, North Checkpoint, Police Station,
                   Quarantine Gun Shop, Food Market, Bus Station, canal
```

Placement:

```text
x = 109..138  Trumbull Valley
x = 139..163  Meagher, Drucker, Cascade, Providence
x = 164..183  Danforth
x = 184..207  Harran City (y=0..23), The Following (y=24..47)
x = 208..231  Dread Dawn
```

Danforth connects to Meagher/east edge. Harran connects to Danforth and to
The Following. The remaining border is countryside: fields, forest and ring
roads.

The pack requires the Omsk Expansion map pack and PZBigBuffer:

```text
require=PZBigBuffer,OmskExpansion
```

Known limitation: road continuity and the final drive test still need an
in-game check.
