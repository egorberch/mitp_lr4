"""Задание №9 (средней сложности): Генератор случайных чисел в диапазоне."""

import itertools
import random
from typing import Generator, Optional


def random_range_generator(
    start: int,
    stop: int,
    step: int = 1,
    count: Optional[int] = None,
) -> Generator[int, None, None]:
    """Генерирует случайные целые числа в диапазоне [start, stop) с шагом step.

    Если count не указан, генератор является бесконечным.

    :param start: Начало диапазона (включительно).
    :param stop: Конец диапазона (не включительно).
    :param step: Шаг дискретизации диапазона (по умолчанию 1).
    :param count: Количество чисел (или None для бесконечной генерации).
    :return: Генератор случайных чисел.
    :raises ValueError: Если шаг <= 0, start >= stop или count < 0.
    """
    if step <= 0:
        raise ValueError("Шаг должен быть положительным числом")
    if start >= stop:
        raise ValueError("Начало диапазона должно быть меньше конца диапазона")
    if count is not None and count < 0:
        raise ValueError("Количество чисел не может быть отрицательным")

    generated = 0
    while count is None or generated < count:
        yield random.randrange(start, stop, step)
        generated += 1


def main() -> None:
    """Демонстрация работы генератора случайных чисел в диапазоне."""
    random.seed(42)

    print("Генерация 5 случайных чисел в диапазоне [10, 50):")
    limited_gen = random_range_generator(start=10, stop=50, count=5)
    print(list(limited_gen))

    print("\nГенерация 6 случайных чётных чисел [0, 100) с шагом 2:")
    even_gen = random_range_generator(start=0, stop=100, step=2, count=6)
    print(list(even_gen))

    print("\nБесконечный генератор [1, 7) (кубик d6) через itertools.islice:")
    dice_gen = random_range_generator(start=1, stop=7)
    rolls = list(itertools.islice(dice_gen, 8))
    print(f"Броски кубика: {rolls}")


if __name__ == "__main__":
    main()
