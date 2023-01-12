def position(x):
    # enumerate會回傳Tuple且第一個會回傳的值是整數，意即num=int
    for num, s in enumerate(x):  # 因為會回傳Tuple所以使用Tuple Onpacking
        if s == s.upper():
            return s, num
    return -1  # 如果遇到輸入的str都是小寫的情況會導致for loop執行完沒有回傳任何值會出現None，因此設定此情形會回傳-1


print(position("abcd"))
print(position("AbCd"))
print(position("abcD"))
