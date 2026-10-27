"""Задание №7 (повышенная сложность): Генератор случайных данных."""

import itertools
import random
from typing import Any, Dict, Generator

NAMES = (
    ("Алексей", "Смирнов"),
    ("Елена", "Иванова"),
    ("Дмитрий", "Кузнецов"),
    ("Ольга", "Попова"),
    ("Михаил", "Соколов"),
    ("Анна", "Новикова"),
)
CITIES = (
    "Москва",
    "Санкт-Петербург",
    "Новосибирск",
    "Казань",
    "Екатеринбург",
)
DEPARTMENTS = ("IT", "Аналитика", "Маркетинг", "Дизайн", "Продажи")


def infinite_random_data() -> Generator[Dict[str, Any], None, None]:
    """Бесконечно генерирует случайные профили сотрудников.

    Каждый профиль представляет собой словарь со структурированными
    случайными данными: идентификатором, ФИО, отделом, городом,
    рейтингом эффективности и признаком активности.

    :return: Бесконечный генератор словарей со случайными данными.
    """
    record_id = 1
    while True:
        first, last = random.choice(NAMES)
        record: Dict[str, Any] = {
            "id": record_id,
            "name": f"{first} {last}",
            "department": random.choice(DEPARTMENTS),
            "city": random.choice(CITIES),
            "performance_score": round(random.uniform(60.0, 100.0), 1),
            "is_active": random.choice([True, True, True, False]),
        }
        yield record
        record_id += 1


def main() -> None:
    """Демонстрация работы бесконечного генератора случайных данных."""
    random.seed(42)

    print("Первые 4 сгенерированных профиля (itertools.islice):")
    stream = infinite_random_data()
    sample = list(itertools.islice(stream, 4))
    for item in sample:
        print(item)

    print("\nФильтрация (filter): только активные сотрудники IT:")
    it_active = filter(
        lambda r: r["is_active"] and r["department"] == "IT",
        infinite_random_data(),
    )
    first_three_it = list(itertools.islice(it_active, 3))
    for item in first_three_it:
        print(
            f"ID {item['id']}: {item['name']} | "
            f"Отдел: {item['department']} | Баллы: {item['performance_score']}"
        )

    print("\nПреобразование (map): краткие сводки сотрудников:")
    summaries = map(
        lambda r: f"[{r['city']}] {r['name']} — {r['performance_score']} б.",
        infinite_random_data(),
    )
    first_five_summaries = list(itertools.islice(summaries, 5))
    for summary in first_five_summaries:
        print(summary)


if __name__ == "__main__":
    main()
