number_str = input("введите 4-х значное число: ")

number = int(number_str)


number1 = number // 1000
number2 = (number % 1000) // 100
number3 = (number % 100) // 10
number4 = number % 10

print(number1)
print(number2)
print(number3)
print(number4)