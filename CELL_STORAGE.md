# Compiled cell storage

The merged base world is:

```text
Omsk_World
4999 cells
6.8 GB
```

The SoD2 pack is:

```text
2600 cells
3.9 GB
```

`CELL_MANIFEST.json` lists every cell and its `.lotheader` / `.lotpack`
sizes.

## Git limitation

Normal GitHub Git cannot store a 6.8 GB binary tree comfortably: individual
files are under 100 MB, but the repository/release limits and clone size make
it impractical. The cells are generated artifacts; the source, manifests and
build tools are committed.

Use Git LFS or split release assets for the compiled cells:

```bash
git lfs install
git lfs track "cells/**/*.lotheader" "cells/**/*.lotpack"
```

Then copy `dist/omsk-expansion/common/media/maps/Omsk_World` to `cells/` in a
dedicated cells repository and push with LFS quota enabled.

Do not commit the 6.8 GB tree with ordinary Git.
