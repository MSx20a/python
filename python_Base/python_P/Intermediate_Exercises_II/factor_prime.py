def factorPrime(x: int):
    """
    質因數分解
    """
    answer = str(x)+" = "  # 設定輸出的格式為 x = y * y * y * ....
    y = 2
    while y <= x:
        if x % y == 0:
            answer += str(y)+" x "
            x /= y   # 如果此質數可以整除x，那就把他除以該質數繼續round next loop
        else:
            y += 1  # 如果無法整除就往下個數去找，如果預設的2無法整除那其他偶數也無法整除x
    return answer[:len(answer)-3]  # slice method


print(factorPrime(120))
