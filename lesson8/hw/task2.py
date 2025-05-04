# Напишите скрипт, который объединяет данные из нескольких JSON файлов в
# один. Каждый файл содержит список словарей, описывающих сотрудников
# компании (имя, фамилия, возраст, должность). Итоговый JSON файл должен
# содержать объединённые списки сотрудников из всех файлов

import glob
import json


def merge_json_files(input_files, output_file):
    merged_data = []
    for file in input_files:
        try:
            with open(file, 'r') as f:
                merged_data.extend(json.load(f))
        except json.JSONDecodeError:
            print(f'Ошибка чтения JSON файла: {file}')

    with open(output_file, 'w') as f:
        json.dump(merged_data, f, indent=4)


if __name__ == '__main__':
    merge_json_files(glob.glob('employees*.json'), 'all_employees.json')
