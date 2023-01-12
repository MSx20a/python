result = []  #定義一個emtpy list of global varible


def flatten(x: list):
    """
    遞迴演算法
    """
    for i in x:
        if type(i) == type([]):  # 判斷x內的element是否為list的技巧
            flatten(i)
        else:
            result.append(i)
    return result


print(flatten([1, [[], 2, [0, [1]], [3]], [1, 3, [3], [4, [1]], [2]]]))
