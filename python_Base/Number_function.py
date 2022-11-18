# Integer belong copy by value type
import math

print(10 + 5)
print(10 * 2)
print(3 ** 3)
print(5 / 2)
print(5 % 2)
print("--------------")

# python methods of numbers

print(abs(-10))  # absolute value
print(pow(2, 10))  # 2 power 10
print(min(4, 7, 2, -13, 100))
print(max(4, 7, 2, -13, 100))
print("--------------")

# 四捨五入，但round函式有一個很特別的規則，只要input number = x.5那就要看他進位後的value是否為偶數，如果是則不會進位，反之則進位；以下有4個例子
print(round(2.5))
print(round(3.5))
print(round(6.2))
print(round(9.7))
print("--------------")

# str(),int(),float() are for typecasting(型態轉換)
print(str(5))
print(int(7.6))
print(float(6))
print("--------------")

# math moddule
print(math.e)
print(math.pi)
print(math.floor(4.9999))  # 無條件捨去
print(math.ceil(4.0001))  # 無條件進位
print(math.sqrt(36))  # square root(開根號)
print("--------------")

# python也有支援數學的“複數（i＝根號-1）”運算用j表示
x = 4+3j
y = 9-2j
print(x+y)
