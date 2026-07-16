import keyword, string

name_def =input("Variable name: ")
is_valid = True


for test_case in name_def:
    if test_case == "_":
        continue
    elif test_case in string.punctuation:
        is_valid = False


if name_def in keyword.kwlist:
    is_valid = False
elif name_def.islower() == False:
    is_valid = False
elif name_def[0].isdigit():
    is_valid = False
elif "__" in name_def:
    is_valid = False
elif "___" in name_def:
    is_valid = False
elif " " in name_def:
    is_valid = False
print(f"{is_valid}")