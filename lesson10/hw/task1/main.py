# Вася совсем заскучал на работе и решил побаловаться с кодом проекта. Он
# Реализуйте два класса: «Родитель» и «Ребёнок». У родителя есть:
# ● имя,
# ● возраст,
# ● список детей.
# И он может:
# ● сообщить информацию о себе,
# ● успокоить ребёнка,
# ● покормить ребёнка.
# У ребёнка есть:
# ● имя,
# ● возраст (должен быть меньше возраста родителя хотя бы на 16 лет),
# ● состояние спокойствия,
# ● состояние голода.
# Реализация состояний — на ваше усмотрение. Это может быть и простой «флаг»,
# и словарь состояний, и что-то поинтереснее.

from lesson10.hw.task1.Child import Child
from lesson10.hw.task1.Parent import Parent

parent = Parent('Дима', 37)
child1 = Child('Василиса', 13)
child2 = Child('Мишаня', 10)

for child in [child1, child2]:
    parent.add_children(child)

parent.info()
parent.list_children()

for child in parent.children:
    parent.feed(child)
    parent.calm(child)
    child.get_status()
