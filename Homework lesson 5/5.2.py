new_operation = True

while new_operation:
    number1 = int(input("Введіть число: "))
    number2 = int(input("Введіть число: "))
    operations = input("Введіть дію (+,-,/,*): ")

    if operations == "*":
        print(number1 * number2)
    elif operations == "+":
        print(number1 + number2)
    elif operations == "-":
        print(number1 - number2)
    elif operations == "/":
        if number2 == 0 or number1 == 0:
            print("Помилка: Дільник дорівнює 0")
        else:
            print(number1 / number2)

    question = str(input("Нова дія ? y/n "))
    while question != "y" and question != "n":
        question = str(input("Введіть y/n "))

        if question == "y":
            new_operation = True
        elif question == "n":
            new_operation = False
