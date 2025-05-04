# Создайте функцию-замыкание, которая запрашивает два целых числа:
# от 1 до 100 для загадывания, от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

def secret_num(num):
    if 0 < num < 101:
        def attempt(quantity):
            if 0 < quantity < 11:
                while quantity != 0:
                    answer = int(input('Введите число: '))
                    quantity -= 1
                    if answer == num:
                        return 'Вы угадали! Ура!'
                    else:
                        print(f'Не угадали, у вас {quantity} попыток!\n')
                else:
                    return 'Попытки кончились!'
            else:
                return 'Неправильное количество попыток'

        return attempt
    else:
        return 'Предано неправильное число'


if __name__ == '__main__':
    print(secret_num(50)(10))

