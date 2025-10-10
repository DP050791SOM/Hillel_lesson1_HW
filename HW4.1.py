lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
print(lst)
lst1 = []
lst2 = []
print('перебрасываем нули в конец списка')
for x in lst:
    if x == 0:
        lst1.append(x)
    else:
        lst2.append(x)

lst3 = lst2 + lst1
print(lst3)
