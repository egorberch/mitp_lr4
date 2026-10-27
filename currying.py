"""Задание №3 (повышенной сложности): Реализация функции-карринга."""

from functools import wraps
from inspect import signature
from typing import Any, Callable


def curry(func: Callable[..., Any]) -> Callable[..., Any]:
    """Преобразует функцию нескольких аргументов в каррированную функцию.

    Позволяет вызывать функцию как по одному аргументу f(a)(b)(c),
    так и группами аргументов f(a, b)(c) или f(a)(b, c).

    :param func: Исходная функция для каррирования.
    :return: Каррированная версия функции.
    """
    sig = signature(func)
    params = [
        p for p in sig.parameters.values()
        if p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD)
        and p.default == p.empty
    ]
    arity = len(params)

    @wraps(func)
    def curried(*args: Any, **kwargs: Any) -> Any:
        if len(args) >= arity:
            return func(*args, **kwargs)

        def partial_curried(*more_args: Any, **more_kwargs: Any) -> Any:
            new_args = args + more_args
            new_kwargs = {**kwargs, **more_kwargs}
            return curried(*new_args, **new_kwargs)

        return partial_curried

    return curried


def multiply_three(a: int, b: int, c: int) -> int:
    """Перемножает три целых числа."""
    return a * b * c


def greet(greeting: str, title: str, name: str) -> str:
    """Формирует персонализированное приветствие."""
    if title:
        return f"{greeting}, {title} {name}!"
    return f"{greeting}, {name}!"


def calculate_cost(price: float, tax_rate: float, discount: float) -> float:
    """Вычисляет итоговую стоимость товара с учётом налога и скидки."""
    return (price * (1 + tax_rate)) * (1 - discount)


def main() -> None:
    """Демонстрация работы каррированных функций."""
    curried_multiply = curry(multiply_three)

    print("Каррирование функции умножения трех чисел (a * b * c):")
    print(f"Вызов f(2)(3)(4): {curried_multiply(2)(3)(4)}")
    print(f"Вызов f(2, 3)(4): {curried_multiply(2, 3)(4)}")
    print(f"Вызов f(2)(3, 4): {curried_multiply(2)(3, 4)}")
    print(f"Вызов f(2, 3, 4): {curried_multiply(2, 3, 4)}")

    double = curried_multiply(2)
    quadruple = double(2)
    print(f"\nЧастичное применение: quadruple(5) = {quadruple(5)}")

    curried_greet = curry(greet)
    formal_hello = curried_greet("Здравствуйте")("г-н")
    informal_hi = curried_greet("Привет")("")
    print(f"\nПриветствие 1: {formal_hello('Иванов')}")
    print(f"Приветствие 2: {informal_hi('Егор')}")

    curried_cost = curry(calculate_cost)
    tax_10_percent = curried_cost(100.0, 0.10)
    print(f"\nЦена 100 со скидкой 5%: {tax_10_percent(0.05):.2f}")
    print(f"Цена 100 со скидкой 20%: {tax_10_percent(0.20):.2f}")


if __name__ == "__main__":
    main()
