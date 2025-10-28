while True:
    num1 = float(input("Введите число 1: "))
    action = input("Введите символ действия (+, -, *, /): ")
    num2 = float(input("Введите число 2: "))

    print("Результат:")

    if action == "+":
        print(num1 + num2)
    elif action == "-":
        print(num1 - num2)
    elif action == "*":
        print(num1 * num2)
    elif action == "/":
        if num2 == 0:
            print("На 0 деление запрещено!")
        else:
            print(num1 / num2)
    else:
        print("Введите корректный символ")


    con = input("Повторить операцию вычисления? (y/yes для продолжения): ").lower()
    if con not in ("y", "yes"):
        print("Вычисления завершены.")
        break