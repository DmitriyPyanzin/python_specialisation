# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл

from random import randint, choice


def pseudo_names(num):
    vowels = ('a', 'e', 'i', 'o', 'u', 'y')
    with open('task2.txt', 'a', encoding='utf-8') as f:
        for i in range(num):
            temp_str = ''
            for j in range(randint(3, 6)):
                temp_str += chr(randint(97, 122))
                if j == 0:
                    temp_str = temp_str.upper()
            if any([el for el in temp_str if el in vowels]):
                temp_str += f'{choice(vowels)}'
            f.write(temp_str + '\n')


if __name__ == '__main__':
    pseudo_names(5)
