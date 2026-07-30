import string

alphabet = input("Please input letters: ")

result = ""
write = False

for x in string.ascii_letters:
    if x == alphabet[0]:
        write = True

    if write:
        result += x

    if x == alphabet[2]:
        break

print(result)