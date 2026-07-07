# Версія 1

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



# Версія 2
'''
number1 = int(input("Введіть число: "))
number2 = int(input("Введіть число: "))
user_select = int(input("Виберіть дію (+,-,/,*): \n1.*\n2.+\n3.-\n4./\nВведіть ваш вибір: "))

if user_select > 4:
    print("Вибір не вірний")
match user_select:
    case 1:
        print("Відповідь: ",int(number1 * number2))
    case 2:
        print("Відповідь: ",int(number1 + number2))
    case 3:
        print("Відповідь: ",int(number1 - number2))
    case 4:
        if number2 == 0 or number1 == 0:
            print("Помилка: Дільник дорівнює 0")
        else:
            print("Відповідь: ",int(number1 / number2))
'''