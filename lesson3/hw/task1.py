lst = [1, 1, 2, 3, 3, 4, 5, 5, 6]
new_lst = []
for el in lst:
    if lst.count(el) != 1:
        new_lst.append(el)

for el in new_lst:
    lst.remove(el)

print(new_lst)
print(lst)
