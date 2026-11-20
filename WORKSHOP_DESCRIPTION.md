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

Внутри — леса, поля, деревни, дороги, мебель, интерьеры, зомби и точки спавна.
Карты продолжают стандартный мир: можно начать в обычном PZ и доехать до новых
городов.

### В комплекте — PZMapStudio для ИИ-агентов

В папке мода лежит инструмент **PZMapStudio**:

```text
PZMapStudio/
  PZMapStudio-v0.1.0.zip
  README.txt
  launch.sh
  launch.bat
```

Он умеет:

- импортировать реальные клетки PZ;
- строить дома с этажами и мебелью;
- делать контуры зданий по крыше;
- ставить дороги, тротуары, заборы и ворота;
- добавлять крышные лестницы;
- размещать места историй;
- искать адрес, фото и планировку;
- проверять карту и писать изменения обратно в клетки.

### Как начать

1. Подпишитесь на мод.
2. Запустите Project Zomboid и создайте **новый save**.
3. Включите `Omsk Expansion`.
4. Откройте своего ИИ-агента.
5. Скажите ему:

> Найди в папке игры или Workshop папку `PZMapStudio`. Прочитай
> `README.txt`, выполни `python3 -m pzmapstudio.cli help --json` и помоги
> мне доработать карту.

Или вручную:

```bash
cd .../steamapps/workshop/content/108600/<ID>/PZMapStudio/
bash launch.sh
```

Нужны Python 3.11+ и Pillow.

Steam Workshop не запускает внешние программы автоматически: он доставляет
файлы, а инструмент запускается вручную или агентом.

### Важно

- это большой мод, около 6.2 GB;
- нужен новый мир, старый save не подойдёт;
- не включайте одновременно старую отдельную копию Исилькуля;
- данные карт: © OpenStreetMap contributors, ODbL.

---

## English

**Omsk Expansion** adds six connected Project Zomboid maps built from real
OpenStreetMap data: Isilkul, Solntsevka/Vodnoye, Omsk, Krasnodar, Novosibirsk
and Moscow — with forests, fields, villages, roads, furnished interiors,
zombies and spawn points. The maps continue the vanilla world.

The mod also ships **PZMapStudio**, an agent-friendly map editor:

```text
PZMapStudio/
  PZMapStudio-v0.1.0.zip
  README.txt
  launch.sh
  launch.bat
```

After subscribing:

1. Start a **new save** and enable `Omsk Expansion`.
2. Open your AI agent.
3. Ask it:

> Find `PZMapStudio` in the game/Workshop folder, read `README.txt`, run
> `python3 -m pzmapstudio.cli help --json`, and help me edit the map.

The Workshop delivers the files; Steam cannot auto-run external Python programs.
Python 3.11+ and Pillow are required. Map data © OpenStreetMap contributors,
ODbL.
