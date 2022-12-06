# generator語法介紹
# 優點是比comprehension（list,dict,set）的語法還要節省記憶體

# yield
def ten(x):
    for i in range(x):
        yield i ** 10


print(ten(5))  # 會回傳<generator object third at 0x7f7aa433dba0>

# generator object屬於iterable object(可迭代物件)
for i in ten(5):
    print(i)


print("------------")

# yield from
# 優點是可以重新架構程式碼，讓程式碼能更好維護


def second(x):
    if x > 2:
        for i in range(2, x, 2):
            yield i ** 2
    else:
        return "x is too small."


def gen(y):
    yield from second(y)


for i in gen(20):
    print(i)


print("------------")


# 第一種製做可用於for loop的object，意即製作一個iterable
# 需使用__iter__() method會回傳iterator
# 在python中任何的generator都是iterator
class Something():
    def __init__(self, x) -> None:
        self.x = x

    def __iter__(self):
        for i in range(self.x):
            yield i


s = Something(5)
print(s)
# iter(iterable)，如果在iter內放入iterable那就會回傳iterator；如果放入的不是iterable會擲出"TypeError"
print(iter(s))
for i in s:
    print(i)


print("------------")


# 第二種製做可用於for loop的object，意即製作一個iterable
# 使用__getitem__ method
class Food():
    def __init__(self, y) -> None:
        self.y = [" "]*y

    def __setitem__(self, y_number, data):
        self.y[y_number] = data

    def __getitem__(self, y_number):
        return self.y[y_number]


f = Food(4)
print(iter(f))  # <iterator object at 0x7fea41449b20>
f[0] = "fish"
f[1] = "beef"
f[2] = "pork"
f[3] = "chicken"

for i in f:
    print(i)

print(f[1])


print("------------")


# 在python中，如果某個東西屬於iterator那它一定是iterable；反之如果它是iterable，那不見得是iterator
# Iterator必須要有__iter__ and __next__，這2個method
# 用上述邏輯來檢查list是否為iterable
x = [1, 2, 3]
print(dir(x))  # dir會回傳放入物件所有的attributes；經查看lsit只有__iter__，因此只屬於iterable
print(dir(iter(x)))  # 經查看有__iter__和__next__，因此屬於iterator

# 從98、99行得到結論：iterator＝iter(iterable)

# 從這可以延伸出for i in x:內部的運作流程
list_iterator = iter(x)
print(next(list_iterator))
print(next(list_iterator))
print(next(list_iterator))


print("------------")

# 製作自己的iteration
class MyIterator():
    def __init__(self, max) -> None:
        self.max = max
        self.index = 0

    def __iter__(self):
        return self  #此部份要回傳自己，因為在for loop運作時，會先執行 __iter__()，後再依序執行__next__()

    def __next__(self):
        if self.index < self.max:
            value=self.index
            self.index += 1
            return value
        else:
            self.index = 0
            raise StopIteration #for loop遇到StopIteration就會被停止


c = MyIterator(7)
for i in c:
    print(i)
