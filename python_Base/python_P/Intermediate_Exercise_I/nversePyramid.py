def nverserTriangle(x):
    y=2*x-1 #星星的數量
    z=0     #空白鍵的數量
    for i in range(x):
        print(z*" "+y*"*")
        y-=2
        z+=1

nverserTriangle(4)
