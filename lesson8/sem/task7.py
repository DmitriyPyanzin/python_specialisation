# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Распечатайте его как pickle строку.

import csv
import pickle


def print_pickle():
    with open('task6.csv', 'r', newline='') as f_csv:
        return pickle.dumps([el for el in csv.reader(f_csv)])


if __name__ == '__main__':
    print(print_pickle())
