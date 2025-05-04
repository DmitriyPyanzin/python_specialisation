counter = 0
n = int(input("Введите количество чисел: "))

for i in range(n):
    num = int(input("Введите число: "))
    if num == 0:
        break
    else:
        for i in range(2, num + 1):
            if num % i == 0 and i != num:
                break
            elif num % i == 0 and i == num:
                counter += 1

print(f"Количество простых чисел равно {counter}")
