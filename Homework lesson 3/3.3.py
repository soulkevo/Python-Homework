numbers = [1, 2, 3, 4, 5]
middle = len(numbers) // 2

if len(numbers) % 2 != 0:
    middle += 1
first_part = numbers[:middle]
second_part = numbers[middle:]

print(first_part, second_part)




