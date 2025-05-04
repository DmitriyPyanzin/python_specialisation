# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.

lst = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]
new_list = []

for i in range(len(lst)):
    if lst[i] % 2:
        new_list.append(i + 1)

print(new_list)

new_list1 = [i + 1 for i in range(len(lst)) if lst[i] % 2]

print(new_list1)

new_list2 = [i for i, el in enumerate(lst, start=1) if el % 2]

print(new_list2)
