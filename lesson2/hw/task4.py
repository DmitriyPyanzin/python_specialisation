import fractions

a1, b1 = [int(i) for i in input().split('/')]
a2, b2 = [int(i) for i in input().split('/')]

print(f"Сумма: {a1 / b1 + a2 / b2}, проверка: {fractions.Fraction(a1, b1) + fractions.Fraction(a2, b2)}")
print(f"Произведение: {(a1 / b1) * (a2 / b2)}, проверка: {fractions.Fraction(a1, b1) * fractions.Fraction(a2, b2)}")
