class Person:
    mux_up = 3


p1 = Person()
p2 = Person()
print(f'{Person.mux_up = }, {p1.mux_up = }, {p2.mux_up = }')

p1.mux_up = 12
print(f'{Person.mux_up = }, {p1.mux_up = }, {p2.mux_up = }')

Person.mux_up = 42
print(f'{Person.mux_up = }, {p1.mux_up = }, {p2.mux_up = }')