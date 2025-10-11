lst = [5,]
lst3 = []
print(lst)
s = len(lst)
if not lst:
    mid = s // 2
    lst1 = lst[mid:]
    lst2 = lst[:mid]
    print('Список пустой')
if not s % 2 == 0:
    mid = s // 2
    lst1 = lst [mid:]
    lst2 = lst[:mid]
    print('Список с нечетным колличеством элементов')
else:
    mid = s // 2
    lst1 = lst[mid:]
    lst2 = lst[:mid]
    print('Список с четным колличеством элементов')

lst3.append(lst1)
lst3.append(lst2)
print(lst3)


