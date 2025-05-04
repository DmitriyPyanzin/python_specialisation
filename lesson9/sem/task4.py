# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.

def run_func(num):
    def decorator(func):
        def wrapper(*args, **kwargs):
            count = 0
            for i in range(num):
                print(func(*args, **kwargs))
                count += 1
            return count

        return wrapper

    return decorator


# @run_func(5)
def example():
    return 'Hello'


if __name__ == '__main__':
    # print(example())
    print(run_func(3)(example)())
