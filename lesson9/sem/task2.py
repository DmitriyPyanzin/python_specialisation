# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.

import random
import functools


def check_secret(func):
    @functools.wraps(func)
    def wrapper(num):
        """Wrapper"""
        if 1 <= num <= 100:
            return func(num)
        print('Введено неверное загаданное число')
        return func(random.randint(1, 100))

    return wrapper


def check_tries(func):
    def wrapper(num):
        if 0 < num < 11:
            return func(num)
        print('Введено неверное количество попыток')
        return func(random.randint(1, 10))
    return wrapper


@check_secret
def secret_num(num):
    """Source"""
    if 0 < num < 101:
        @check_tries
        def attempt(tries):
            if 0 < tries < 11:
                while tries != 0:
                    answer = int(input('Введите число: '))
                    tries -= 1
                    if answer == num:
                        return 'Вы угадали! Ура!'
                    else:
                        print(f'Не угадали, у вас {tries} попыток!\n')
                else:
                    return 'Попытки кончились!'
            else:
                return 'Неправильное количество попыток'

        return attempt
    else:
        return 'Предано неправильное число'


if __name__ == '__main__':
    # print(secret_num(50)(10))
    print(secret_num.__name__)
    print(secret_num.__doc__)
