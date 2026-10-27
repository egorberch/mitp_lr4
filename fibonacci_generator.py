"""Задание №5 (средней сложности): Генератор чисел Фибоначчи."""

import itertools
from typing import Generator, Optional


def fibonacci_generator(
    count: Optional[int] = None,
) -> Generator[int, None, None]:
    """Генерирует последовательность чисел Фибоначчи.

    Если параметр count не передан, генератор работает бесконечно.
    Если count передан, генерируется ровно count чисел.

    :param count: Количество генерируемых чисел (неотрицательное).
    :return: Генератор чисел Фибоначчи.
    :raises ValueError: Если count меньше 0.
    """
    if count is not None and count < 0:
        raise ValueError("Количество чисел не может быть отрицательным")

    a, b = 0, 1
    generated = 0

    while count is None or generated < count:
        yield a
        a, b = b, a + b
        generated += 1


def main() -> None:
    """Демонстрация работы генератора чисел Фибоначчи."""
    n = 10
    print(f"Первые {n} чисел Фибоначчи (с ограничением count={n}):")
    result = list(fibonacci_generator(n))
    print(result)

    print("\nГенерация из бесконечного генератора через itertools.islice:")
    infinite_fib = fibonacci_generator()
    first_15 = list(itertools.islice(infinite_fib, 15))
    print(first_15)

    print("\nПоэлементный вывод первых 5 чисел:")
    for index, value in enumerate(fibonacci_generator(5), start=1):
        print(f"F_{index} = {value}")


if __name__ == "__main__":
    main()
