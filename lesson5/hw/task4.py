# Напишите генераторную функцию substrings(s), которая принимает строку
# s и возвращает генератор всех возможных подстрок этой строки.
# На вход подается строка abc

s = input()

for el in (s[start:end] for start in range(len(s)) for end in range(start + 1, len(s) + 1)):
    print(el)
