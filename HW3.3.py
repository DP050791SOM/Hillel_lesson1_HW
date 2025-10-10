lst = []
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



print(lst1)
print(lst2)

