"""

寫一程式，從下列一維陣列中找出每個段落，數字連續出現的次數：
array = [3, 3, 3, 3, 3, 3, 6, 2, 7, 7, 7, 7, 7, 3, 3, 1, 1, 1, 5, 5, 5, 5, 6, 6]

"""
array = [3, 3, 3, 3, 3, 3, 6, 2, 7, 7, 7,
         7, 7, 3, 3, 1, 1, 1, 5, 5, 5, 5, 6, 6]
# i = 0
# count = 1
# for i in range(len(array)-1):
#     if array[i] == array[i+1]:
#         count += 1
#         # print(count)
#         print(f"value:{array[i]},consecutive_count:{count}")
#     else:
#         count = 1
#         # print(count)
#         print(f"value:{array[i+1]},consecutive_count:{count}")


# Recursion function


def total(x: list):
    i = 0
    count = 0
    other = []  # other list用來存放剩下的element
    if len(x) > 1:
        for i in range(len(x)):
            if x[0] == x[i]:
                count += 1
            else:
                other.append(x[i])
        # print(other)
        print(f"value:{x[0]},consecutive_count:{count}")
        total(other)
    else:
        if len(x) == 1:
            count = 1
            print(f"value:{x[0]},consecutive_count:{count}")
        else:
            pass  # 防止輸入emtpy list所造成IndexError: list index out of range


total([3, 3, 3, 3, 3, 3, 6, 2, 7, 7, 7, 7, 7, 3, 3, 1, 1, 1, 5, 5, 5, 5, 6, 6, 9])
