# Напишите генераторную функцию fibonacci(n), которая принимает на вход
# одно целое число n и возвращает последовательность первых n чисел
# Фибоначчи. Числа Фибоначчи — это последовательность, в которой каждое
# число является суммой двух предыдущих, начиная с 0 и 1.

def fibo(num):
    num -= 2
    lst = [0, 1]
    for i in range(2, num):
        lst.append(lst[i - 1] + lst[i - 2])
    return lst


print(fibo(int(input())))


def fib(num):
    a, b = 0, 1
    for _ in range(num):
        yield a
        a, b = b, a + b


for item in fib(int(input())):
    print(item, end=' ')
