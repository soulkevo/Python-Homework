numbers = int(input("Введіть 4-х значне ціле число: "))

num1 = numbers // 1000
num2 = numbers // 100 % 10
num3 = numbers // 10 % 10
num4 = numbers % 10

print(num1, num2, num3, num4, sep='\n')
