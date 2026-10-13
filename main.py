"""Программа для вычисления факториала целого неотрицательного числа."""


def factorial(n: int) -> int:
    """Возвращает n!; для отрицательных чисел и неподходящих типов вызывает ошибку."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("Аргумент должен быть целым числом")
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определён")

    result = 1
    for number in range(2, n + 1):
        result *= number
    return result


if __name__ == "__main__":
    print("Факториал 5:", factorial(5))
