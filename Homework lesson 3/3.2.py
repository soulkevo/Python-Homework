# Варіант 1 через insert & pop

numbers1 = [12, 3, 4, 10]
if len(numbers1) <= 1:
    print(numbers1)
else:
    last_number = numbers1[-1]
    numbers1.insert(0, last_number)
    numbers1.pop()
    print(numbers1)

# Варіант 2 через зрізи

numbers2 = [12, 3, 4, 10, 8]
if len(numbers2) > 1:
    numbers2 = [numbers2[-1]] + numbers2[:-1]
    print(numbers2)