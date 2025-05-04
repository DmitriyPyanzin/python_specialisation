# Создайте модуль с функцией, которая принимает два списка и возвращает
# список, содержащий только элементы, которые уникальны для обоих списков.

def unique_el(lst1: list, lst2: list) -> list:
    res = []
    new_lst1 = [el for el in lst1 if lst1.count(el) == 1]
    new_lst2 = [el for el in lst2 if lst2.count(el) == 1]
    for el in new_lst1:
        if el not in new_lst2:
            res.append(el)
        else:
            new_lst2.remove(el)
    res += new_lst2
    return res


if __name__ == '__main__':
    print(unique_el(['a', 'b', 'c', 'a', 'd'], ['q', 'b', 'd', 'e', 'z', 'j', 'g', 'f']))
