# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json


def txt_to_json(file_txt, file_json):
    with (open(file_txt, 'r', encoding='utf-8') as f_txt,
          open(file_json, 'w', encoding='utf-8') as file_json
          ):
        data = {}
        for line in f_txt:
            data[line.split(' - ')[0].capitalize()] = line.split(' - ')[1][:-1]

        json.dump(data, file_json, indent=2)


if __name__ == "__main__":
    txt_to_json('task1.txt', 'task1.json')
