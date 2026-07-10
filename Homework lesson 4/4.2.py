numbers = [0, 1, 7, 2, 4, 8]
summa = 0

if numbers != []:
    for x in numbers[0::2]:
        summa += x
else:
    numbers = [0]

result = summa * numbers[-1]

print(result)
