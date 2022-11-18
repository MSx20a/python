x = set({1, 5, 9, 3})
print(x)  # set在print後會自動由小到大排序
print("--------------")

myList = [0, 5, 5, 5, 9, 6, 6]
y = set(myList)
print(y)
print("--------------")

# add method
s = set()
s.add(1)
s.add(3)
s.add(3)
print(s)

# discard method
s.discard(1)
print(s)

# clear method
s.clear()
print(s)
print("--------------")

a = {1, 2, 3, 4, 5}
b = {3, 4, 6, 7, 8}
# difference method
print(a.difference(b))  # a-b
print(b.difference(a))  # b-a

# intersection method(交集)
print(a.intersection(b))
print(b.intersection(a))

# union method(聯集)
print(a.union(b))
print(b.union(a))
print("--------------")

# isdisjoint method(確認是否無交集)
c = {1, 2, 3}
d = {4, 5, 6}
print(c.isdisjoint(d))
print("--------------")

e = {35, 79}
f = {35, 23, 79, 56, 12, 84}
# issubset method(確認是否為子集合)
print(e.issubset(f))
# issuperset method(確認是否為母集合)
print(f.issuperset(e))
print("--------------")
