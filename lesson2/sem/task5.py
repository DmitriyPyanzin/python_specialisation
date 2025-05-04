# ✔ Напишите программу, которая решает квадратные уравнения даже если
# дискриминант отрицательный.
# ✔ Используйте комплексные числа для извлечения квадратного корня.

from math import sqrt


a, b, c = 10, -50, 100

D = b ** 2 - 4 * a * c

if D > 0:
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    print(f"Корни уравнения: х1 = {x1:.3f}; x2 = {x2:.3f}")
elif D == 0:
    x = (-b) / (2 * a)
    print(f"Корень уравнения: x = {x:.3f}")
else:
    real = round(-b / (2 * a), 4)
    imaginary = round(sqrt(abs(D)) / (2 * a), 4)
    x1 = complex(real, imaginary)
    x2 = complex(real, -imaginary)
    print(f"Корни уравнения: х1 = {x1:.3f}; x2 = {x2:.3f}")
