# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

lst = [4, 2, 2, 3, 3, 3, True, True, False]
new_lst = lst.copy()

for el in lst:
    if lst.count(el) == 2:
        print(el)
        temp = new_lst.remove(el)

print(new_lst)
