# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона

from random import randint, choice, choices
from string import ascii_lowercase


def create_file(ext, min_name=6, max_name=30, min_byte=256, max_byte=4096, files=42):
    for _ in range(files):
        with open(f'{''.join(choices(ascii_lowercase, k=randint(min_name, max_name)))}.{ext}', 'ab') as f:
            f.write(b'x' * randint(min_byte, max_byte))


if __name__ == '__main__':
    create_file('xml', files=10)
