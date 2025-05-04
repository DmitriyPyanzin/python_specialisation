from sys import argv as a
from random import randint as r


def guess_num(args):
    num = r(args[0], args[1])
    attempts = args[2]
    while attempts != 0:
        attempts -= 1
        user_num = int(input("введите число\n"))
        if user_num < num:
            print('Больше')
        elif user_num > num:
            print('Меньше')
        else:
            return True

    else:
        return False


if __name__ == '__main__':
    arguments = [int(el) for el in a[1:]]
    print(guess_num(arguments))
