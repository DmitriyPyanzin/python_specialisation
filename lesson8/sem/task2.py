# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключом для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.

import json


def writer_users():
    while True:
        user_name = input('Введите имя: ')
        user_id = input('Введите уникальный идентификатор: ')
        user_level = input('Введите уровень допуска (если ввести 0, то программа остановится): ')
        if user_name == 'q' or user_level == '0':
            break
        if user_level.isdigit() and 1 <= int(user_level) <= 7:
            with open('task2.json', 'r+', encoding='utf-8') as f:
                data = json.load(f)
                if user_id in data[user_level].keys():
                    print('Такой идентификатор уже существует\n')
                else:
                    data[user_level][user_id] = user_name
                    with open('task2.json', 'w', encoding='utf-8') as file:
                        json.dump(data, file, ensure_ascii=False)

        else:
            print('Вы ввели неверный код доступа\n')


if __name__ == '__main__':
    writer_users()
