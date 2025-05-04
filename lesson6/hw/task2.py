# Напишите модуль с функцией, которая принимает строку и возвращает строку с
# удаленными дублирующимися подряд идущими символами. Например, строка
# "aabbccaa" должна быть преобразована в "abca".

def del_double_symbol(word: str):
    string = word[0]
    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            continue
        string += word[i]
    return string


if __name__ == '__main__':
    print(del_double_symbol("aabbccaa"))
