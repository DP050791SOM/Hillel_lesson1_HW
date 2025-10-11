lst = [9, 0, 7, 31, 0, 45, 32, 45, 0, 45, 0, 0, 35,53,33]
print(lst)
list1 = lst[::2]

print('элементы с парными индексами - ',list1)
z = lst[-1]
sum1 = sum(list1)
print('сумма чисел =', sum1)
result = sum1 * z
print('финальный результат -',result)

