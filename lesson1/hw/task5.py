num = int(input("Введите загаданное число от 1 до 100: "))
counter = 0
min_num, max_num = 1, 100

while True:
    counter += 1
    temp = int((max_num + min_num) / 2)
    print(f"Вы загадали число {temp}")
    print("1 - равно")
    print("2 - больше")
    print("3 - меньше")
    answer = int(input())
    if answer == 1:
        print(f"Ура! Я угадал с {counter} попыток!")
        break
    elif answer == 2:
        min_num = temp
    else:
        max_num = temp
