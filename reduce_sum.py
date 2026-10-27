"""Задание №3 (средней сложности): Сумма чисел с использованием reduce."""

from functools import reduce
from typing import Iterable, Union

Number = Union[int, float]


def sum_numbers(numbers: Iterable[Number], initial: Number = 0) -> Number:
    """Вычисляет сумму чисел из итерируемого объекта с помощью reduce.

    :param numbers: Итерируемый объект с числами (int или float).
    :param initial: Начальное значение аккумулятора (по умолчанию 0).
    :return: Сумма всех чисел.
    """
    return reduce(lambda acc, x: acc + x, numbers, initial)


def main() -> None:
    """Демонстрация вычисления суммы чисел через reduce."""
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result_int = sum_numbers(int_list)
    print(f"Список целых чисел: {int_list}")
    print(f"Сумма через reduce: {result_int}")

    float_list = [1.5, 2.7, 3.8, 4.0]
    result_float = sum_numbers(float_list)
    print(f"\nСписок вещественных чисел: {float_list}")
    print(f"Сумма через reduce: {result_float:.2f}")

    mixed_list = [-10, 25, -5, 40]
    result_mixed = sum_numbers(mixed_list)
    print(f"\nСписок со знаками (+/-): {mixed_list}")
    print(f"Сумма через reduce: {result_mixed}")

    empty_list: list[Number] = []
    result_empty = sum_numbers(empty_list)
    print(f"\nПустой список: {empty_list}")
    print(f"Сумма через reduce (с начальным значением): {result_empty}")


if __name__ == "__main__":
    main()
