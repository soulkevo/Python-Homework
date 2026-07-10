import random

first_list = []
second_list = []


for x in range(random.randint(3,10)):
    first_list.append(random.randint(1,100))
second_list.append(first_list[0])
second_list.append(first_list[2])
second_list.append(first_list[-2])

print(first_list)
print(second_list)