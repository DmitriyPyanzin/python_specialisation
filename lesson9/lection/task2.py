def add_one_str(a):
    names = []

    def add_two_str(b):
        names.append(b)
        return a + ', ' + ', '.join(names)

    return add_two_str

hello = add_one_str('Hello')
bye = add_one_str('Good bye')

print(hello('Dima'))
print(hello('Masha'))
print(bye('Vasya'))
print(hello('Pushok'))
print(bye('Misha'))
