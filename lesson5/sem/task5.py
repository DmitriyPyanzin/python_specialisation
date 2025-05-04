# ✔ Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.

# def generator(n):
#     for el in range(1, n + 1):
#         yield el


# for i in generator(int(input())):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# for i in generator(int(input())):
#     print('FizzBuzz') if i % 3 == 0 and i % 5 == 0 else print('Fizz') if i % 3 == 0 else print('Buzz') if i % 5 == 0\
#         else print(i)


gen = ('FizzBuzz' if el % 3 == 0 and el % 5 == 0 else 'Fizz' if el % 3 == 0 else 'Buzz' if el % 5 == 0 else el
       for el in range(1, 101))

for el in gen:
    print(el)
