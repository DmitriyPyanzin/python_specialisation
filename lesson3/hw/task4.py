import random
import string


def psw(num):
    s = ''
    for i in range(num):
        s += random.choice(string.printable)
    return s

print(psw(int(input())))
