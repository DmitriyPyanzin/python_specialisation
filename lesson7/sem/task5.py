# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

from task4 import create_file
from random import choice


def create_new_files(ext: tuple, files: int):
    for i in range(files):
        create_file(choice(ext), files=1)


if __name__ == '__main__':
    create_new_files(('img', 'txt', 'doc', 'png', 'avi', 'mp3', 'xml'), 10)
