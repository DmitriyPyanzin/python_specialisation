# Напишите скрипт, который считывает данные из CSV файла, содержащего
# информацию о продажах (название продукта, количество, цена за единицу), и
# подсчитывает общую выручку для каждого продукта. Итог должен быть сохранён в
# новом CSV файле.
# Пример: Из файла sales.csv нужно создать файл total_sales.csv, где для каждого
# продукта будет указана общая выручка.


import csv


def calculate_sales(input_file, output_file):
    sales = {}
    with open(input_file, 'r') as f:
        reader = csv.DictReader(f)

        for row in reader:
            product = row['название продукта']
            quantity = int(row['количество'])
            price = float(row['цена за единицу'])
            total_sales = quantity * price
            if product in total_sales:
                sales[product] += total_sales
            else:
                sales[product] = total_sales
    with open(output_file, 'w', newline='') as f:
        fields = ['название продукта', 'общая выручка']
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for product, total_sales in sales.items():
            writer.writerow({'название продукта': product, 'общая выручка': total_sales})


if __name__ == '__main__':
    calculate_sales('sales.csv', 'total_sales.csv')
