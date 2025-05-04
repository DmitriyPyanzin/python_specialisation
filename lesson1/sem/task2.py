# Работа в консоли в режиме интерпретатора Python.
# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# Используйте while и if.
# Попробуйте разные значения e и n.

n, e = map(int, input().split())
mysum, elem = 0, 0

while elem <= n:
    elem += 2
    if elem % e == 0:
        continue
    mysum += elem

print(mysum)
