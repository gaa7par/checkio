# module statistics (with median()) not allowed
def checkio(data):
    median = len(data) // 2

    data.sort()
    if len(data) % 2 != 0:
        median = data[median]
    else:
        median = (data[median] + data[median - 1]) / 2
    return median

