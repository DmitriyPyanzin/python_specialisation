def add_one_str(a):
    text = ''

    def add_two_str(b):
        nonlocal text
        text += ', ' + b
        return a + text

    return add_two_str

hello = add_one_str('Hello')
bye = add_one_str('Good bye')

print(hello('Dima'))
print(hello('Masha'))
print(bye('Vasya'))
print(hello('Pushok'))
print(bye('Misha'))
