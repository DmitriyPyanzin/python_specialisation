class User:
    def __init__(self, name):
        self.name = name
        print(f'Create {self.name = }')

    def __del__(self):
        print(f'del {self.name}')

u1 = User('u1')
u2 = User('u2')
