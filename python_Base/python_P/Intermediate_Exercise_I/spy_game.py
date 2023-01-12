def spyGame(x: list):
    """
    查看list內有無0,0,7這三個值(非連貫)
    """
    y = [0, 0, 7]
    pointer_for_list1 = 0
    pointer_for_list2 = 0
    while pointer_for_list1 < len(x):
        if x[pointer_for_list1] == y[pointer_for_list2]:
            pointer_for_list2 += 1
            print(pointer_for_list2)
            if pointer_for_list2 == len(y):  # 防止超出y list的index value
                return "true"
        pointer_for_list1 += 1
    return "false"


print(spyGame([1, 2, 4, 0, 3, 0, 7]))
print(spyGame([1, 2, 5, 0, 3, 1, 7]))
