def is_palindrome(text):

    result = ""

    for char in text:
        if char.isalnum():
            result += char.lower()


    return result == result[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
