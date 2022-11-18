# List belong copy by reference type
# Splicing rule work with list as well

lockNumbers = [2, 7, 4, 9, 1, 5, 3]
print(lockNumbers[0:4])
print(lockNumbers[::2])
print(lockNumbers[::-1])  # reverse list
print("-----------------------")

# Count method
x = [0, 0, 2, 4, 8, 9, 6, 6, 5]
print(x.count(0))
print("-----------------------")

# List can concatenation
a = [3, 8, 23]
b = [45, 12, 2]
print(a+b)
print("-----------------------")

# List can multiply
c = [3, 7, 9]
print(c*3)
print("-----------------------")
#List is mutable
e = [2, 6, 7]
e[1] = 8
print(e)
print("-----------------------")

# insert method(插入)
foods = ["beef", "fish", "pork"]
foods.insert(2, "rice")
print(foods)
print("-----------------------")

# remove method
foods.remove("fish")
print(foods)
print("-----------------------")

# clear method
foods.clear()
print(foods)
print("-----------------------")

# sort method（會直接改變在ram中原本的list）
friends = ["Josh", "Alvin", "Melo", "Tom"]
friends.sort()  # 會按照字母大小做排序
print(friends)

# sorted method（排序後不想改變原本的list，而是會直接產生一個新的list存放到新的記憶體位置）
y = [150, -20, 45, 30, 55, 89]
A = sorted(y)  # 因為會產生一個新的list，所以要用另一個varible存放
print("原來的List:", y, ",經排序後的List:", A)
print("-----------------------")

# reverse method
y.reverse()
print(y)
print("-----------------------")

# append method(附加)
friends.append("Bob")
friends.append("Boris")
print(friends)

# pop method(可以將list最後一個元素取出)
my_lost_friend = friends.pop()
print(my_lost_friend)
print(friends)
print("-----------------------")

# copy method(can really copy a list,not copy by reference)
f = [1, 2, 3, 4, 5]
g = f.copy()
g[0] = 10
print(f)
print(g)
print("-----------------------")

# list of lists
z = [1, 2, [6, 7, 8], 3, 4, [9, 0]]
print(z[2][1])  # 把陣列中的其他陣列值抓出來的方法
# print(len(z))
print(len(z)-1)  # 抓出陣列的最後一個值的方法
print("-----------------------")

# join method
x = ["1", "2", "3"]
myString = "|".join(x)  # 可以將想要的String合併進來
print(myString)
print("-----------------------")

# range function(typecasing to list)
# 這是一個比較不好的方法因為會造成電腦佔用更多的ram = 在python2中range function會return一個List
# 但在python3會return一個range object藉以節省佔用ram的空間
myList = list(range(10, 20, 3))
print(myList)
