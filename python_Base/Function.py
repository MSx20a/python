# x,y are local varible

def summary(x, y):  # x,y are parameters(參數（未給定值）)
    """This function is addtion for input x and y."""  # 此方法可以讓使用此function的人使用help()快速了解此function的功能
    print(x+y)


help(summary)

# argument can be variables as well
summary(25, 56)  # 25,56 are arguments(參數（已給定值）)
print("---------------")

a = 10  # gobal varible


def change(num):  # paramenters are local varible in function
    # num=a   copy by value => num=10
    num = 25  # num=25,but a value also 10


change(a)
print(a)
print("---------------")


def change_a(num):
    # change copy by value gobal varible method
    global a
    a = 25


change_a(a)
print(a)
print("---------------")

b = [1, 2, 3, 4]


def change_List(num):
    # num=b     copy by reference => num=[1,2,3,4]
    num[0] = 100  # b=num=[100,2,3,4]


change_List(b)
print(b)
print("---------------")

# return的用法


def multiplication(c, d):
    result = c*d
    return result


print(multiplication(5, 9))
print("---------------")

# return在loop和function中可以中斷在它之後的code


def sequence(g, f):
    i = 1
    j = 0
    for i in range(g):
        for j in range(f):
            if i == 3 and j == 5:
                return  # 在（3,5）時會觸發reurn來終止整個loop因此不會print(3,5)
            print(i, j)


sequence(5, 7)
# print(sequence(5, 15))  # 因為return後沒有接任何東西因此直接print sequencec會得到None
print("---------------")


def squared(h, i):
    return h**i


print(squared(2, 3))  # Postitional Arguments順序不能顛倒，會造成得到的結果不同
print(squared(i=3, h=2))  # Keyword Arguments不重視順序，即便順序不同也不影響其結果
print("---------------")

# defult arguments 必須要將有預設的參數放在後面，這是python訂下的規則
# is diferent keyword arguments


def subtraction(j, k=6):
    return j-k


print(subtraction(20))
print("---------------")

# Arbitrary Number of Arguments

# args data type is Tuple


def sum(*args):
    print(type(args))
    print(len(args))
    result = 0
    for number in range(len(args)):
        result += args[number]
    return result


print(sum(1, 5, 10, 6, 8))
print("---------------")

# kwargs data type is Dictionary


def myfun(**kwargs):
    print(type(kwargs))
    print("{} is now {} years old.".format(kwargs["name"], kwargs["age"]))
    print(f"I am {kwargs['name']}")


myfun(name="Alvin", age="28")
print("---------------")

# args和kwargs如果要一起使用那在function parameters中的順序:*args,**kwargs；也可以取＊hi,**hello，主要是用星號來決定功能

# 1.normal parameters(x)
# 2.default parameters(y)
# 3.*args parameters
# 4.**kwargs param4eters
# Ex: def fun(x,y=2,*args,**kwargs):


def both(*args, **kwargs):
    print("I like eat {} {}.".format(args[1], kwargs["food"]))


both(1, 2, 3, "hi", food="beef")
print("---------------")


# High order function的定義是會用其他function來當成他的argument
def square(num):
    # x= num**2
    # print(f"this is {x}")
    return num**2


myList = [4, 8, 2, 9]

# map function is High order function
# 第二個parameter要放iterables like string,list,truple,set,etc
c = map(square, myList)
print(c)  # return map object
print(type(c))

for d in map(square, myList):
    print(d)
    # break
print("---------------")


def even(f):
    return f % 2 == 0

    # 以上寫法和下面程式碼結果相同
    # if f%2==0:
    #    return Ture
    # else:
    #    return False
mylist = [246, 789, 444, 822, 999, 10001]
# filter function is High order function
# 和map不同的地方是iterable中的element帶入function return Ture才會被加進filter object中
print(filter(even, mylist))  # return filter object
print(type(filter(even, mylist)))

for g in filter(even, mylist):
    print(g)
print("---------------")


#Lambda Expression like JavaScript arrow function
#syntax：lambda input1,imput2,....: operation
#會自動return value
result=(lambda h:h**2)(h=5)
print(result)


myTuple=(lambda x,y:(x*y,x/y))(20,33)
print(myTuple[0])
print(myTuple[1])


#Lambda最常用在map,filter上
for h in map(lambda x:x**3,[23,55,81]):
    print(h)
for i in filter(lambda x:x%3==0,[33,48,100,117,87]):
    print(i)