from collections import namedtuple
from math import sqrt

# namedyuple會創造一個class，名稱是我設定的"Point"
z = namedtuple("Point", ["x", "y"])

a = z(4.3, 5.9)
b = z(7.1, 9.6)

line_len = sqrt((a.x-b.x)**2+(a.y-b.y)**2)
print(type(a))
print(line_len)


print("-------------------")


worker = namedtuple("Worker", ["job", "salary", "workplace"])

alvin = worker("Engineer", 60000, "TW")

print(type(alvin))
print(alvin)
print(alvin.salary)
