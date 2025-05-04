# Напишите функцию группового переименования файлов. Она должна:
# 1. принимать параметр желаемое конечное имя файлов. При
# переименовании в конце имени добавляется порядковый номер.
# 2. принимать параметр количество цифр в порядковом номере.
# 3. принимать параметр расширение исходного файла. Переименование
# должно работать только для этих файлов внутри каталога.
# 4. принимать параметр расширение конечного файла.
# 5. принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик
# файлов и расширение. 3.Соберите из созданных на уроке и в рамках домашнего
# задания функций пакет для работы с файлами.
from os import chdir, listdir, rename


def sequence_number(counter, length):
    number = ''
    number += str(counter)
    if len(number) != length:
        number += '0' * (length - len(number) - 1)
    return number[::-1]


def rename_files(end_name, quantity, ext_old, ext_new, len_start, len_end):
    chdir('task1')
    lst = listdir()
    counter_num = 0
    for el in lst:
        if el[-3:] == ext_old:
            counter_num += 1
            rename(el, el[len_start:len_end] + end_name + sequence_number(counter_num, quantity) + '.' + ext_new)


if __name__ == '__main__':
    rename_files('task1', 3, 'txt', 'png', 2, 5)
