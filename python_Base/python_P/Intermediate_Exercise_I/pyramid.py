#    *
#   ***
#  *****
# *******
#最底層的星星數量=2x-1


def triangle(x):
   y=x-1  #空白鍵的數量
   z=1    #星星的數量
   for i in range(x):
    print(y*" "+z*"*")
    z+=2
    y-=1

triangle(4)


    
        
