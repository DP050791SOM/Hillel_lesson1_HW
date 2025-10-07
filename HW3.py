num1 = float(input("введите первое число: "))
num2 = float(input("введите второе число: "))
operation = input("ввыедите операцию (+, -, *, /): ")
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("Делить на ноль нельзя")
else:
    print("Введите правильную операцию")

print("Результат: ")
print(result)
