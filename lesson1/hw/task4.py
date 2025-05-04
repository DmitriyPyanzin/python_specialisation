num = int(input("Введите число: "))
s = ""

for i in range(num, 0, -1):
    for j in range(num, i - 1, -1):
        s += str(j)
    s += '.' * (i - 1)
    print(s + s[::-1])
    s = ""
