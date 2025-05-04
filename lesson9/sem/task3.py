# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой
# функции.


import json
import os


def save_to_json(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)

            data = {
                'name': func.__name__,
                'args': args,
                'kwargs': kwargs,
                'res': res
            }

            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    exist = json.load(file)
                exist.append(data)

                with open(filename, 'w') as file:
                    json.dump(exist, file, indent=2)
            else:
                with open(filename, 'w') as file:
                    json.dump([data], file, indent=2)

        return wrapper

    return decorator


@save_to_json('function_data.json')
def example(a, b, c=3):
    return a + b + c

if __name__ == '__main__':
    example(1, 2, c=3)
    example(4, 5, c=6)
