import math


a, b = [int(input()) for i in range(2)]

print(math.gcd(a, b))

while b:
    a, b = b, a % b

print("НОД:", a)
