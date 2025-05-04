# Создайте модуль с функцией, которая получает список слов и возвращает
# словарь, в котором ключи — это слова, а значения — количество их повторений
# в списке.

def create_dict(lst: list):
    dct = {}
    for el in lst:
        dct[el] = lst.count(el)
    return dct


if __name__ == '__main__':
    print(create_dict(["proger", "tester", "proger", "prodact", "tester", "proger"]))
    