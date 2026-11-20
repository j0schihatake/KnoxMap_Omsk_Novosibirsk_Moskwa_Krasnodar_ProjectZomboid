# Omsk Expansion + PZMapStudio

## Русский

**Omsk Expansion** — шесть связанных карт Project Zomboid по реальным данным
OpenStreetMap:

- Исилькуль;
- Солнцевка и Водяное;
- Омск;
- Краснодар;
- Новосибирск;
- Москва.

Внутри — леса, поля, деревни, дороги, интерьеры, мебель, зомби и точки спавна.
Карты продолжают стандартный мир: можно начать в обычном PZ и доехать до новых
городов.

---

## PZMapStudio — инструмент для ИИ-агента

Для работы с картой отдельно публикуется **PZMapStudio**: java-core и агентский интерфейс. Это не просто внешний скрипт — Java-ядро читает и пишет реальные клетки
PZ, умеет безопасно применять изменения с backup, а в игре работает через
Java/Lua-мод.

### Принцип работы

1. Подпишитесь на два item: **Omsk Expansion** (карты) и **PZMapStudio** (инструмент).
2. Запустите Project Zomboid и создайте **новый save**.
3. Включите `Omsk Expansion`.
4. Откройте своего ИИ-агента.
5. Скажите ему:

> Найди в папке игры или Workshop папку `PZMapStudio`. Прочитай `README.txt`,
> выполни `help` и помоги мне доработать карту: расставь лавочки в парках,
> поправь дороги, добавь крышный доступ и места историй.

Агент сам находит инструмент, читает инструкцию и работает с картой.

### Что умеет

- читать реальные `.lotheader/.lotpack`;
- импортировать terrain, дороги, здания, комнаты и мебель;
- строить дома с этажами и практичной мебелью;
- строить здания по контуру крыши;
- ставить дороги, тротуары, заборы, ворота и лавочки;
- добавлять крышные лестницы;
- размещать story-сайты;
- расставлять лавочки у парков и аллей по координатам/OSM;
- проверять карту: дубли клеток, спавны, save-state, комнаты;
- писать изменения в реальные клетки с backup и валидацией.

### Два режима

**В игре — Java/Lua-мод:**

- `F10` — панель: JSON-команды сцены, staging, Apply cell, Horde, Loot;
- `F11` — observer: игрок, время, температура;
- файловая очередь команд для агента:
  ```text
  ~/Zomboid/PZMapStudio/queue.jsonl
  ```
- live-события: зомби, лут, объекты;
- запись клетки с backup.

**Без игры — standalone Java/Python:**

- CLI и HTTP API;
- массовые road-pass/object-pass;
- аудит и подготовка карт;
- работа с будущими картами и обновлениями игры.

### Безопасность

- изменения клеток только через backup;
- проверка заголовка и комнат после записи;
- активный save не переписывается молча;
- новый мир обязателен для добавления карт.

### Требования

- Java 25 для standalone Java-инструментов;
- Python 3.11+ и Pillow — только для дополнительного Python-набора;
- Java-мод работает без Python.

### Ограничение

Это **beta**: Java-мод и live-рассказчик развиваются. Карты уже играбельны;
редактор в игре пока даёт сцену, staging, apply-cell, observer и live-события,
а полноценный RimWorld-подобный планировщик историй — следующий этап.

Данные карт: © OpenStreetMap contributors, ODbL.

---

## English

**Omsk Expansion** adds six connected Project Zomboid maps built from real
OpenStreetMap data: Isilkul, Solntsevka/Vodnoye, Omsk, Krasnodar, Novosibirsk
and Moscow.

The pack also ships **PZMapStudio**, a Java-core map tool for AI agents:
subscribe, start a new save, open your agent and ask it to find `PZMapStudio`
in the game/Workshop folder and read `README.txt`/`help`.

PZMapStudio can import real cells, build houses and furniture, place roads,
fences and park benches, add roof access and story sites, audit maps, and write
changes back to compiled cells with backup and validation.

Java mod: F10 panel/apply-cell/observer/horde/loot and a file command queue.
Standalone Java/Python: CLI, HTTP API, map audits and batch passes.

Beta: maps are playable; the in-game editor and RimWorld-style storyteller are
under active development. Map data © OpenStreetMap contributors, ODbL.
