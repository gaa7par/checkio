def checkio(data):
    new_data = []
    for number in data:
        if data.count(number) != 1:
            new_data.append(number)
    return new_data

