# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

import json
import csv


def convert_to_csv():
    with (open('task2.json', 'r', encoding='utf-8') as file_json,
          open('task3.csv', 'w', encoding='utf-8', newline='') as file_csv
          ):

        reader = json.load(file_json)
        data = []
        for el in reader.items():
            for item in el[1]:
                data.append({'level': el[0], 'id': item, 'name': el[1][item]})

        field = ['level', 'id', 'name']
        csv_writer = csv.DictWriter(file_csv, fieldnames=field)
        csv_writer.writeheader()
        csv_writer.writerows(data)


if __name__ == '__main__':
    convert_to_csv()
