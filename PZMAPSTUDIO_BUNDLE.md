# Bundling PZMapStudio with the Workshop mod

The map mod can ship the PZMapStudio source release in a normal folder:

```text
dist/omsk-expansion/PZMapStudio/
  PZMapStudio-v0.1.0.zip
  README.txt
  launch.sh
  launch.bat
```

After subscribing, the user finds it under the Workshop content folder:

```text
.../steamapps/workshop/content/108600/<publishedfileid>/PZMapStudio/
```

They can extract the zip and run:

```bash
bash launch.sh
python3 -m pzmapstudio.cli help
```

or on Windows double-click `launch.bat`.

## Important limitation

Steam Workshop cannot execute an external Python program automatically. A
subscription can deliver the files but cannot install Python, unpack them or
launch a process. That is a Steam/Workshop constraint, not a missing button.

If the tool must run with no manual step, it has to become an in-game Java/Lua
mod, which is a separate project and a large rewrite.

## Recommended distribution

- Publish the map pack in Workshop.
- Bundle the toolkit folder as above.
- Keep the canonical PZMapStudio release on GitHub Releases.
- In the Workshop description, link the GitHub release and the command
  `python3 -m pzmapstudio.cli help`.
