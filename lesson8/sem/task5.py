# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

import os
import pickle
import json


def convert_pickle():
    lst_files = os.listdir()
    counter = 0
    for el in lst_files:
        if el.split('.')[1] == 'json':
            with (
                open(f'task5_{counter}.pkl', 'wb') as f_pickle,
                open(el, 'r', encoding='utf-8') as f_json
            ):
                pickle.dump(json.load(f_json), f_pickle)
            counter += 1


if __name__ == "__main__":
    convert_pickle()
