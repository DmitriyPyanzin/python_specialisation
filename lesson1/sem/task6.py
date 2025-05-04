# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке

print("\t\t\t\t\tТАБЛИЦА УМНОЖЕНИЯ")


def mult1():
    for i in range(2, 11):
        for j in range(2, 6):
            print(f"{j} X {i} = {i * j}".center(14), end='')
        print()


def mult2():
    for i in range(2, 11):
        for j in range(6, 10):
            print(f"{j} X {i} = {i * j}".center(14), end='')
        print()


mult1()
print()
mult2()
