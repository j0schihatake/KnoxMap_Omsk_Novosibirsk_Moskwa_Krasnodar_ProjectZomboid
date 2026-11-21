# Local compiled-cell repository

This is a local-only git repository for the compiled Project Zomboid cells.

It intentionally is not pushed to GitHub: the Omsk and SoD2 cell trees are
several GB and the normal GitHub/LFS quota cannot hold them.

Working tree for commits:

```text
../dist
```

Contents:

```text
omsk-expansion/common/media/maps/Omsk_World/
sod2-expansion/common/media/maps/
```

Every map also ships `worldmap.xml.bin` so it appears on the in-game map.

## Read the cells

```bash
cd /home/j0schi/SteamLibrary/steamapps/common/ProjectZomboid/work/KnoxMap-dev

git --git-dir=cells-local.git --work-tree=dist status
git --git-dir=cells-local.git --work-tree=dist log --oneline
```

## Restore a checkout

```bash
git --git-dir=cells-local.git --work-tree=dist checkout -- .
```

The source generators and documentation remain in the GitHub repos; this
repository stores the compiled cells themselves.
