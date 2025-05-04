# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

from math import prod


def compare_lens(lst_nums, lst_names):
    if len(lst_nums) < len(lst_names):
        temp = lst_nums
    else:
        temp = lst_names

    while True:
        for i in range(len(temp)):
            temp.append(temp[i])
            if len(lst_nums) == len(lst_names):
                return


def func():
    with (
        open('task1.txt', 'r', encoding='utf-8') as f_nums,
        open('task2.txt', 'r', encoding='utf-8') as f_names,
        open('task3.txt', 'a', encoding='utf-8') as f_res
    ):
        lst_nums = [el for el in f_nums.read().split()]
        lst_names = [el for el in f_names.read().split()]

        if len(lst_names) != len(lst_nums):
            compare_lens(lst_nums, lst_names)

        for i in range(len(lst_nums)):
            temp_lst_nums = lst_nums[i].split('|')
            temp_prod = prod([int(temp_lst_nums[0]), float(temp_lst_nums[1])])
            if temp_prod < 0:
                f_res.write(f'{lst_names[i].lower()} - {round(abs(temp_prod), 3)}\n')
            else:
                f_res.write(f'{lst_names[i].upper()} - {round(temp_prod)}\n')


if __name__ == '__main__':
    func()
