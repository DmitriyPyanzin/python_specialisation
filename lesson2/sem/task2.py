# Создайте в переменной data список значений разных типов перечислив их через
# запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# ✔ порядковый номер начиная с единицы
# ✔ значение
# ✔ адрес в памяти
# ✔ размер в памяти
# ✔ хэш объекта
# ✔ результат проверки на целое число только если он положительный
# ✔ результат проверки на строку только если он положительный
# добавьте в список повторяющиеся элементы и сравните на результаты.

data = [1, 2.1, True, "txt", frozenset([1, 2]), 5 + 7j, None, ...]

for i, elem in enumerate(data, 1):
    print(f"Num: {i}, value: {elem}, id: {id(elem)}, type: {type(elem)}, size: {elem.__sizeof__()}, "
          f"hash: {hash(elem)}, pos: {isinstance(elem, int)}, str: {isinstance(elem, str)}")
