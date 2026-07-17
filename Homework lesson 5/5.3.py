import string

text = input()
result = ""

text = text.title()

for x in text:
    if x not in string.punctuation and x != " ":

        result += x

result = "#" + result

if len(result) > 140:
    result = result[:140]

print (result)



