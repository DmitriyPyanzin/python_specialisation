# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

from os import chdir, mkdir
from task5 import create_new_files


def create_dir(directory):
    try:
        mkdir(directory)
        chdir(directory)
        create_new_files(('img', 'txt', 'doc', 'png', 'avi', 'mp3', 'xml'), 1)
    except FileExistsError:
        chdir('..')


if __name__ == '__main__':
    create_dir('dir')
