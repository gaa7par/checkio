def checkio(data):
    numeric = False
    upper = False
    lower = False

    if len(data) < 10:
        return False
    else:
        data = data[::1]
        for char in data:
            numeric = numeric or char.isnumeric()
            upper = upper or char.isupper()
            lower = lower or char.islower()
    return numeric and upper and lower
