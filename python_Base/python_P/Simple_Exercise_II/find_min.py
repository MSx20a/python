def findMin(x:list):
    z=10000000000000000000
    if len(x)==0:
        return "undefined"
    for i in x:
        if i<z:
            z=i
    return z

print(findMin([1, 2, 5, 6, 99, 4, 5]))
print(findMin([1, 6, 0, 33, 44, 88, -10]))
print(findMin([]))