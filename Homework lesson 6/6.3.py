number = int(input("Please enter number: "))


while number > 9:
    result = 1

    while number > 0:
        digit = number % 10
        result *= digit
        number //= 10

    number = result

print(number)