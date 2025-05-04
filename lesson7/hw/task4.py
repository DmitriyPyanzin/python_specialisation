# Напишите функцию, которая находит и перечисляет все файлы с заданным
# расширением в указанном каталоге и всех его подкаталогах. Функция должна
# принимать путь к каталогу и расширение файла.

import os


def count_files(dir, ext):
    for root, files, dirs in os.walk(dir):
        for file in files:
            if file.endwith(ext):
                print(os.path.join(root, file))


if __name__ == '__main__':
    count_files('lesson7/hw/task1', '.py')
