width = int(input("Введите ширину рамки: "))
height = int(input("Введите высоту рамки: "))

for i in range(height):
    print(f'|{'-' * (width - 2)}|' if i == 0 or i == height - 1 else f'|{' ' * (width - 2)}|')
