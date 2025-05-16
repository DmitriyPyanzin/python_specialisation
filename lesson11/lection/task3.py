class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name):
        self.name = name


a = Singleton('First')
print(f'{a.name = }')
b = Singleton('Second')
print(f'{b.name = }')
print(f'{a is b = }')
print(f'{a.name = }, {b.name = }')
