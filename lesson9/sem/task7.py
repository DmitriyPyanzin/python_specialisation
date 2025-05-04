class Decore:
    def __init__(self, num):
        self.num = num

    def __call__(self, func):
        def wrapper():
            return func()

        return wrapper


@Decore(5)
def my_func():
    return 'Hello, world!'


if __name__ == "__main__":
    print(my_func())
