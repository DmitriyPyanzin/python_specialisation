name = "Alex"
age = None

a = 42
print(id(a))
a = "Hello world!"
print(id(a))
a = 3.14 / 3
print(id(a))

print(name, age, a, 456, "text", sep=" (=^.^=) ", end='#')
print("Any text")

res = input("Print you text: ")
print("Ты написал ", res)

ADULT = 21
age = int(input("Сколько тебе лет: "))
how_old = ADULT - age
print(how_old, "Осталось до совершеннолетия")
