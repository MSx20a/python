def findSmallTotal(l:list,x:int):
    y=0
    for i in l:
        if i < x:
            y+=i
    return y        

print(findSmallTotal([1, 2, 3], 3)) # returns 3
print(findSmallTotal([1, 2, 3], 1)) # returns 0
print(findSmallTotal([3, 2, 5, 8, 7], 999)) # returns 25
print(findSmallTotal([3, 2, 5, 8, 7], 0)) # returns 0