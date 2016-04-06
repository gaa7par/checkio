def checkio(data):
    number, upper, lower = False
    if len(data) < 10:
        return False
    else:
        for char in data:
            number = number or char.isnumeric()
            upper = upper or char.isupper()
            lower = lower or char.lower()

        return number and upper and lower

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"

