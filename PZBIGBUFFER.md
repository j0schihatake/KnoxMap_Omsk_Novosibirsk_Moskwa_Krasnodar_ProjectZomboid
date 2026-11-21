# PZBigBuffer

A tiny ZombieBuddy Java mod that replaces the fixed 10 MB
`zombie.iso.SliceY.SliceBuffer` with a 64 MB heap buffer.

It is a normal Java mod, not a Java agent and not a preload mod:

```text
mod.info
42/media/java/PZBigBuffer.jar
javaPkgName=pzbigbuffer.mod
require=ZombieBuddy
```

Users subscribe, approve the JAR once in ZombieBuddy, and restart. No scripts,
no `-javaagent`, no `ProjectZomboid64.json` edits.

Maps declare:

```text
require=PZBigBuffer
```

Build output:

```text
work/PZBigBufferMod/dist/PZBigBuffer
```

Tested headlessly: the replacement reports `capacity=67108864`.
