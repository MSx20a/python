def intersection1(x: list, y: list):
    """
    2 list的交集
    但會有個小bug，如果list內有重複的element那也會一併輸出到新的list內
    """
    result = []
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                result.append(x[i])

    return result


print(intersection1([1, 3, 4, 4, 6, 10], [5, 11, 4, 4, 3, 100, 144, 0, 3]))


def intersection2(x: list, y: list):
    """
    2 list的交集(使用Set的intersection method)
    """
    return list(set(x).intersection(set(y)))


print(intersection2([1, 3, 4, 4, 6, 10], [5, 11, 4, 4, 3, 100, 144, 0, 3]))
