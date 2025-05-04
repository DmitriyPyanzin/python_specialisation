# Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

tpl = (1, False, True, 2.4, 5, "text", "ABC", 3.45,)
mydict = {}
for el in tpl:
    mydict.setdefault(type(el), []).append(el)
    # mydict.setdefault(type(el), [])
    # mydict[type(el)] = mydict.get(type(el)) + [el]

print(mydict)
