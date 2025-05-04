# Напишите скрипт, который удаляет файлы в указанном каталоге, которые не
# изменялись более заданного количества дней. Скрипт должен принимать путь к
# каталогу и количество дней.

import os
import time


def del_old_files(dir, days_old):
    now = time.time()
    cut_off = now - (days_old * 86400)
    for root, dirs, files in os.walk(dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_mod_time = os.path.getmtime(file_path)
            if file_mod_time < cut_off:
                os.remove(file_path)
                print(f'Удален файл: {file_path}')

if __name__ == '__main__':
    del_old_files('task1', 1)
