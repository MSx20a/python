# Counter也是class object，會將結果以dict的形式回傳
from collections import Counter

myList = [2, 3, 3, 5, 5, 5, 9, 9, 9, 9, 4, 4, 4, 4, 4]

result = Counter(myList)

print(type(result))
print(result)

print("-----------------------------------")

letter = "aaaaaaaaaaaaagggggggggggghhhhhhhhhhhhhhhhhhhhhhrrrrrrrvvvvZZZZZZZZZZZZ"

# most_commom()可以依照出現次數將元素由多到少排列，也可以帶入參數來指定要第幾多的元素；會以tuple的方式回傳
f = Counter(letter).most_common()
print(f)
c = Counter(letter).most_common(3)
print(c)
