# Steam Workshop publishing

Prepared files:

```text
dist/workshop/workshop_build_item.vdf
dist/workshop/README.md
```

The content folder is:

```text
dist/omsk-expansion
```

First upload uses `publishedfileid=0`; after publishing put the returned id into
the VDF. SteamCMD command:

```bash
steamcmd +login <steam_login> +workshop_build_item /home/j0schi/SteamLibrary/steamapps/common/ProjectZomboid/work/KnoxMap-dev/dist/workshop/workshop_build_item.vdf +quit
```

The mod is about 6.2 GB. If Steam rejects a single item, split the maps into a
core plus optional regional Workshop items.
