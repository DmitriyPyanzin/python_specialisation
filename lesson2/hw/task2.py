def reform(num: int, div: int) -> str:
    new_num: str = ""
    while num != 0:
        temp = num % div
        if temp > 9:
            temp = chr(87 + temp)
        new_num += str(temp)
        num //= div
    return new_num[::-1]


number = int(input("Введите целое число: "))

print(reform(number, 2) == bin(number)[2:], reform(number, 2))
print(reform(number, 8) == oct(number)[2:], reform(number, 8))
print(reform(number, 16) == hex(number)[2:], reform(number, 16))
