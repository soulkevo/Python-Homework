def generate_cube_numbers(end):
    number = 2

    while number ** 3 < end:
        yield number ** 3
        number += 1


from inspect import isgenerator

gen = generate_cube_numbers(1)

assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'Test1'
assert list(generate_cube_numbers(100)) == [8, 27, 64], 'Test2'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729], 'Test3'

print('OK')