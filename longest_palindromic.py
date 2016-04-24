def checkio(text):
    lst = []
    # count = 0
    is_palindromic = False
    for char in text:
        lst.append(char)
        is_palindromic = lst == lst[::-1]
        # count += 1
        yield is_palindromic

# test

text = "abaccc"
print(checkio(text))
