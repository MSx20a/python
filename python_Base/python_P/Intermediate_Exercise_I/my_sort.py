def mySort(x: list):
    if len(x) == 0:
        return "undefined"
    else:
        a = sorted(x)
        return a


print(mySort([17, 0, -3, 2, 1, 0.5]))
