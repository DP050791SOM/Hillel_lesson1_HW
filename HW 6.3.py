numb = int(input("Введите число: "))

while numb > 9:
    numb1 = 1
    for digit in str(numb):
        numb1 *= int(digit)
    numb = numb1

print("Результат:", numb)