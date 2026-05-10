#!/usr/bin/env python3
"""
build_zones.py — генерация data/zones.json (9 Васту-зон)

Источник: канон Вастушастра, agents.json (vastu_zone поля),
лорбук Pavel_voice_note_vastu_innovations.txt

Запуск: python3 tools/build_zones.py
Результат: data/zones.json
"""

import json
import os

ZONES = [
    {
        "id": 1,
        "slug": "east",
        "name": "Восток",
        "direction": "Восток",
        "element": "Огонь",
        "planet": "Солнце",
        "quality": "Пробуждение, чистота, новое начало"
    },
    {
        "id": 2,
        "slug": "northeast",
        "name": "Северо-Восток (Ишана)",
        "direction": "Северо-Восток",
        "element": "Вода",
        "planet": "Юпитер",
        "quality": "Божественность, мудрость, священное знание"
    },
    {
        "id": 3,
        "slug": "north",
        "name": "Север (Кубера)",
        "direction": "Север",
        "element": "Воздух",
        "planet": "Меркурий",
        "quality": "Богатство, возможность, ясность ума"
    },
    {
        "id": 4,
        "slug": "northwest",
        "name": "Северо-Запад (Ваю)",
        "direction": "Северо-Запад",
        "element": "Воздух",
        "planet": "Луна",
        "quality": "Движение, перемена, непостоянство"
    },
    {
        "id": 5,
        "slug": "west",
        "name": "Запад (Варуна)",
        "direction": "Запад",
        "element": "Вода",
        "planet": "Сатурн",
        "quality": "Завершение, стабильность, созерцание"
    },
    {
        "id": 6,
        "slug": "southwest",
        "name": "Юго-Запад (Найрити)",
        "direction": "Юго-Запад",
        "element": "Земля",
        "planet": "Раху",
        "quality": "Укоренение, сила, защита"
    },
    {
        "id": 7,
        "slug": "south",
        "name": "Юг (Яма)",
        "direction": "Юг",
        "element": "Огонь",
        "planet": "Марс",
        "quality": "Энергия, трансформация, дхарма"
    },
    {
        "id": 8,
        "slug": "southeast",
        "name": "Юго-Восток (Агни)",
        "direction": "Юго-Восток",
        "element": "Огонь",
        "planet": "Венера",
        "quality": "Творчество, изобилие, жизненная сила"
    },
    {
        "id": 9,
        "slug": "center",
        "name": "Центр (Брахмастан)",
        "direction": "Центр",
        "element": "Эфир",
        "planet": "Брахмастан",
        "quality": "Священное пространство, равновесие, источник"
    }
]

def main():
    out_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'zones.json')
    out_path = os.path.normpath(out_path)
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(ZONES, f, ensure_ascii=False, indent=2)
    print(f"zones.json: {len(ZONES)} zones -> {out_path}")

if __name__ == '__main__':
    main()
