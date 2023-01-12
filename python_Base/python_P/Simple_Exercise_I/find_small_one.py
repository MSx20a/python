
def smallCount(x:list,y:int):
    z=0 #計數值的預設要再loop外否則每當執行新一輪loop，計數值都會被歸0
    for i in x:
        if i<y:
           z+=1
    return z

print(smallCount([1, 2, 3], 5))
print(smallCount([1, 2, 3, 4, 5], 0))
