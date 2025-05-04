a, b = input(), input()

dict_a, dict_b = {}, {}

if len(a) != len(b):
    print("Не анаграммы")
else:
    for i in range(len(a)):
        dict_a[a[i]] = a.count(a[i])
        dict_b[b[i]] = b.count(b[i])

print("Анаграммы" if dict_a == dict_b else "Не анаграммы")
