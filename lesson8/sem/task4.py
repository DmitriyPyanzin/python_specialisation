# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.

import csv
import json


def convert_json(file_csv, file_json):
    with (
        open(file_csv, 'r', encoding='utf-8', newline='') as f_csv,
        open(file_json, 'w', encoding='utf-8') as f_json
    ):
        reader = list(csv.reader(f_csv))
        reader[0].append('hash')
        temp_lst = []
        for el in reader[1:]:
            el[1] = el[1].zfill(10)
            el[2] = el[2].title()
            el.append(hash(el[1] + el[2]))
            temp_lst.append({reader[0][0]: el[0], reader[0][1]: el[1], reader[0][2]: el[2], reader[0][3]: el[3]})
        json.dump(temp_lst, f_json, ensure_ascii=False)


if __name__ == "__main__":
    convert_json('task3.csv', 'task4.json')
