# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».
from math import sqrt


def gen(num):
    for i in range(2, num + 1):
        flag = True
        for j in range(2, int(sqrt(i) + 1)):
            if i % j == 0:
                flag = False
                break
        if flag:
            yield i


for item in gen(int(input())):
    print(item)

# for el in (el for el in range(2, int(input()) + 1)):
#     print(el)
