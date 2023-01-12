def findAllSmall(l:list,y:int):
    z=[]
    for i in l:
        if i<y:
            z.append(i)
    return z

print(findAllSmall([1, 2, 3], 10))
print(findAllSmall([1, 2, 3], 2))
print(findAllSmall([1, 3, 5, 4, 2], 4))