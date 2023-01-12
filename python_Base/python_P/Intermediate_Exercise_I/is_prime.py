def isPrime(x):
    if x == 1:
        return "false"
    for i in range(2, x):
        if x % i == 0:
            return "false"
    return "ture"

    # #other answer
    # s=2
    # while x>s:
    #     if x%s==0:
    #         return "false"
    #     s+=1
    # return "ture"


print(isPrime(1))
print(isPrime(5))
print(isPrime(13))
print(isPrime(91))
