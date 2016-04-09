def checkio(data):
    numeric = False
    upper = False
    lower = False

    if len(data) < 10:
        return False
    else:
        data = data[::1]
        for char in data:
            if char.isnumeric():
                numeric = True
            if char.isupper():
                upper = True
            if char.islower():
                lower = True
    if numeric and upper and lower:
        return True
