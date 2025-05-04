def deco_a(func):
    def wrapper_a(*args, **kwargs):
        print('Старт декоратора А')  # 6 7
        print(f'Запускаю {func.__name__}')  # 5 8
        res = func(*args, **kwargs)  # - 9 (11)
        print(f'Завершение декоратора А')  # 8 12
        return res  # - 13

    print('Возвращаем декоратор А')  # 1
    return wrapper_a


def deco_b(func):
    def wrapper_b(*args, **kwargs):
        print('Старт декоратора B')  # 4 5
        print(f'Запускаю {func.__name__}')  # 6 6
        res = func(*args, **kwargs)  # - 7 (14)
        print(f'Завершение декоратора B')  # 9 15
        return res  # - 16

    print('Возвращаем декоратор B')  # 2
    return wrapper_b


@deco_b
@deco_a
def program():
    print('Старт основной функции')  # 7 10


if __name__ == '__main__':  # - 1
    print('>>> Запуск program')  # 3 - 2
    program()  # - 3 (17)
    print('>>> завершение program()')  # 10 18
