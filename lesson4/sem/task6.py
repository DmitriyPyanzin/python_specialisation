# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.
import random


def my_sum(lst, index1, index2):
    list_index = sorted([index1, index2])
    return sum(el for el in lst if lst.index(el) in range(list_index[0] + 1, list_index[1]))

random_list = [random.randint(0, 100) for i in range(int(input()))]
print(random_list)
print(my_sum(random_list, -5, -2))
