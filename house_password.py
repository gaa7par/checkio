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

if __name__ == '__main__':
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"

