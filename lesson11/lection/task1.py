class User:
    def __init__(self, name):
        self.name = name
        print(f'Create {self.name}')

    def __new__(cls, *args, **kwargs):
        print(f'Create class {cls}')
        return super().__new__(cls)

print('Create first')
u1 = User('name1')
print('Create second')
u2 = User('name2')
print('Create third')
u3 = User(name='name3')
