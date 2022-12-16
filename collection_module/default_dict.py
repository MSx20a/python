# defaultdict 也是class object
from collections import defaultdict


#default dictionary是不能用一般的字典表達方式去設定b={"name":"Harry","age":34}；
#如果使用一般的方式的話，會出現reassignment的效果，讓你的變數a變成一般的字典，而不是default dictionary


b=defaultdict(lambda:"Not the key.")

b["name"]="Web"
b["age"]=30

print(b["weihgt"])