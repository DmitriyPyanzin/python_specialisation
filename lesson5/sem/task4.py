# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
# числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.

generator = range(0, 101, 2)
gen = (i for i in range(0, 101, 2) if sum([int(el) for el in str(i)]) != 8)

print([el for el in generator if el % 10 + el // 10 != 8])
print([el for el in gen])
