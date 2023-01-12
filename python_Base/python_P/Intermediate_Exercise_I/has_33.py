def has33(x:list):
    if len(x)==0:
        return "false"
    for i in range(len(x)-1):
        if x[i]==3 and x[i+1]==3:
            return "true"
    return "false"


print(has33([1, 5, 7, 3, 3]))
print(has33([]))   
print(has33([4, 3, 2, 1, 0]))