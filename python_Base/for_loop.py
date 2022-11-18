# for varible in iterable object:
#       do something here

for x in "Alvin":
    print(x)
print("------------")

# list in for loop
myList = [2, 4, 6, 8, 10, 12, 14, 16, 18]
for i in myList:
    print(i**2)
print("------------")

# a list of tuple in for loop
for a, b in [(2, 5), (7, 9), (0, 6)]:    # tuple Unpacking
    print(a, b)
print("------------")

# dictionary in for loop
scooter = {"manufacturer": "KYMCO", "name": "RacingS", "weight": "130kg"}

# dictionary(key) in for loop
for k in scooter:
    print(k)

# dictionary(value) in for loopr
for v in scooter.values():
    print(v)

# dictionary(item) in for loopr
for key, value in scooter.items():  # like truple
    print(f"This Dictionary Key is {key}")
    print(f"This Dictionary Vaule is {value}")
print("------------")

# set in for loop
for y in {1, 3, 5, 7, 9}:
    print(y)
print("------------")

# pass 可以跳過不需要執行迴圈，在if,function,class的語法中在可以使用
for c in "How are you?":
    pass
print("------------")

# break 可以強制中斷此迴圈
for d in "123456":
    if d == "5":
        break
    else:
        print(d)
print("------------")

# continuce 會直接使迴圈跳過當次執行程式碼的敘述
for e in "ABCDE":
    if e == "c":
        continue
    print(e)
print("------------")

# ranger function在python中很常拿來和for loop一起使用
# ranger(start(0),end(requie),step(1))
for f in range(3):
    print(f)
print("------------")
for g in range(10, 15, 2):
    print(g)
print("------------")

# enumerate function(return tuple data type)
# enumerate第一個會回傳的值是整數，意即counter=int
for counter, char in enumerate("I am very hungry."):
    if counter < 10:
        print(char)
print("------------")

# zip function(tuple packing)
# 如果要packing的list長度不一樣那會依照最短的list去做packing
h = [0, 1, 2, 3]
j = ["a", "b", "c", "d"]
for k in zip(h, j):
    print(k)
print("------------")

# List comprehensions
# new_List=[operation for variable in origial_List (if condition)]
l = [1, 2, 3, 4, 5]
squared_l = [item**2 for item in l]
print(squared_l)
print("------------")

# Dictionary comprehensions
# new_Dict={key:value(operation) for varible in origial_Dict (if condition)}
squared_m = {m: m**2 for m in l if m > 2}
print(squared_m)
print("------------")

# Set comprehensions
# new_Set={operation for varible in origial_Set (if condition)}
squared_n = {n: n**2 for n in l}
print(squared_n)
print("------------")

# generator comprehensions
square_o = (o**2 for o in l)
print(square_o)  # 直接print generator object會得到其位置而非value

for p in square_o:  # 用另一個variable存放square_o的值
    print(p)
