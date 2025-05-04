# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.
import decimal
import math


def circle(num: int) -> str:
    decimal.getcontext().prec = 28
    return (f"Площадь круга: {decimal.Decimal(math.pi) * decimal.Decimal(num) ** 2}\n"
            f"Длина окружности: {2 * decimal.Decimal(math.pi) * decimal.Decimal(num)}")


print(circle(int(input("Введите диаметр: "))))
