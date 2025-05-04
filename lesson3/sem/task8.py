# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

friend_dict = {
    "Леха": ("Палатка", "Нож", "Тушёнка", "Пиво"),
    "Толян": ("Котелок", "Нож", "Удочка", "Пиво"),
    "Димон": ("Топор", "Макароны", "Тушёнка", "Пиво"),
}

all_set = set()
for friend in friend_dict:
    all_set |= set(friend_dict[friend])

thing_dict = dict.fromkeys(all_set, 0)

for thing in thing_dict:
    for friend in friend_dict:
        for item in friend_dict[friend]:
            if thing == item:
                thing_dict[thing] += 1

not_item_dict = dict.fromkeys(friend_dict, '')

for thing in thing_dict:
    if thing_dict[thing] == len(friend_dict) - 1:
        for friend in friend_dict:
            if thing not in friend_dict[friend]:
                not_item_dict[friend] += f'{thing}, '

print('Взяли вещи все друзья: ', end='')
for thing in thing_dict:
    if thing_dict[thing] == len(friend_dict):
        print(thing, end=' ')
print()

print('Уникальные вещи: ', end='')
for thing in thing_dict:
    if thing_dict[thing] == 1:
        print(thing, end=' ')
print()

for key in not_item_dict:
    if len(not_item_dict[key]) != 0:
        print(f'У всех друзей есть {not_item_dict[key]}кроме {key}')
