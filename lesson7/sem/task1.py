# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

from random import randint, uniform


def random_numbers(num_strings: int):
    with open('task1.txt', 'a', encoding='utf-8') as f:
        for i in range(num_strings):
            f.write(f'{randint(-1000, 1000)}|{uniform(-1000, 1000):5f}\n')


if __name__ == '__main__':
    random_numbers(10)
