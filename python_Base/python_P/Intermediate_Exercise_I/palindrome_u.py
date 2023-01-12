# palindrom=回文
# beareab
# 0123456
# i     len(x)-1-i
import math


def palindrome(x: str):
    z = math.floor(len(x)/2)
    print(f"input string middle value is {z}.")
    for i in range(0, z):
        if x[i] != x[len(x)-1-i]:
            return False
    return True


print(palindrome("bearaeb"))
print(palindrome("Whatever revetahW"))
print(palindrome("Aloha, how are you today?"))
print()

# palindrom的第二種解法
# beareab
# left=bea
# right=eab


def palindrome2(x: str):
    left = 0
    right = len(x)-1
    while left < right:
        if x[left] != x[right]:
            return False
        left += 1
        right -= 1
    return True


print(palindrome2("alvinivla"))
