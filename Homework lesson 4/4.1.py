numbers = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

for x in numbers:
    if x == 0:
        numbers.append(x)
        numbers.remove(x)
print(numbers)