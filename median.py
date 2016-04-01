# module statistics (with median()) not allowed
def checkio(data):
    median_minus = len(data) // 2 - 1
    median_plus = len(data) // 2

    data.sort()
    if len(data) % 2 != 0:
        median = data[len(data) // 2]
    else:
        median = (data[median_minus] + data[median_plus]) / 2
    return median

