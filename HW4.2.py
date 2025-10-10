lst = [9, 0, 7, 31, 0, 45, 32, 45, 0, 45, 0, 0, 35]
print(lst)
elements = len(lst)
list1 = []
y= 0
while y >= 0:
    x = lst[y]
    y=y+2
    list1.append(x)
    if y >= elements - 1:
        break

print('элементы с парными индексами - ',list1)
z = lst[-1]
sum1 = sum(list1)
print('сумма чисел =', sum1)
result = sum1 * z
print('финальный результат -',result)

