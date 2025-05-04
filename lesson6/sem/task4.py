import random as r


def func(start, end, attempt):
    num = r.randint(start, end)

    while attempt != 0:
        print(f"Попыток для угадывания {attempt}")
        attempt -= 1
        user_num = int(input("введите число\n"))
        if user_num < num:
            print('Больше')
        elif user_num > num:
            print('Меньше')
        else:
            print(f'Угадали с попытки № {attempt}')
            return True

    else:
        print(f'У вас {attempt} попыток')
        return False


if __name__ == '__main__':
    print(func(1, 100, 7))
