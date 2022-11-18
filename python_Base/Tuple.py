myTuple = (5, "50", "hi")
print(len(myTuple))
print(myTuple[1])  # index rule
print(myTuple[0:2])  # slicing rule
print(myTuple.count(5))
print(myTuple.index("hi"))
print("--------------------")

x = "RCS", 19.2  # tuple Packing
print(x)
print(type(x))
name, hp = x  # tuple Unpacking
print(name)
print(hp)
print("--------------------")

a = 25
b = 35
a, b = b, a
print(a)
print(b)
# in other programming language,if you can change a,b value
#temp = a
#a = b
#b = temp
# print(a)
# print(b)
print("--------------------")

d = [0, 2, 6], "KFC"
d[0][2] = 56
print(d)
# If in an element in tuple is mutable,then we can just select the element,and then change it.
# If we want to use a tuble as a dictionary key,then all elements in the tuble has to be immutable.
print("--------------------")

# sorted method（排序後不想改變原本的tuple，而是會直接產生一個新的tuple存放到新的記憶體位置）
y = 67, 88, 23, 45, 100, 39
z = sorted(y)  # 因為會產生一個新的tuple，所以要用另一個varible存放
print(y)
print(z)
