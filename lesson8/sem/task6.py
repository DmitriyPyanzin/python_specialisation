# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестирования возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.
import csv
import pickle


def convert_csv():
    with (
        open('task5_2.pkl', 'rb') as f_pickle,
        open('task6.csv', 'w', newline='', encoding='utf-8') as f_csv
    ):
        reader = pickle.load(f_pickle)
        writer = csv.DictWriter(f_csv, fieldnames=reader[0].keys())
        writer.writeheader()
        writer.writerows(reader)


if __name__ == '__main__':
    convert_csv()
