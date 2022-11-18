# String belong copy by value type
# keep in mind in python build-in method don't modify the string itself
# string is immutable!（不可改變，即使使用method也不會將原先設定的string做更改而是會喘聲一個新的string存放在其他的記憶體位置上）
# strung可以和number做相乘，但float不行
print("Futile!"*10)
print("--------------")

# 在python中在字串後加上[]可以查看該string的index值（從0開始計算）
print("Hello"[0])
print("Hello"[1])
print("Hello"[2])
print("Hello"[3])
print("Hello"[4])
print("--------------")

# reverse output
print("Hello"[0])
print("Hello"[-1])
print("Hello"[-2])
print("Hello"[-3])
print("Hello"[-4])
print("Hello"[-5])  # not happen [out of ranger error]
print("--------------")

# string slice method
x = "python is good."
# [start(inclusive):end(exclusive):stepsize(optional)]
print(x[:5])
print(x[3:])
print(x[2:10])
print(x[1:9:2])
print(x[::-1])  # reverse output
print("--------------")

# 在python中string可以用““和‘’來表示
print('"python" is good.')
print("--------------")

# "\n"代表換行
print("I am\n Alvin.")
print("--------------")

# string can concatenation
string1 = "Freedom "
string2 = "and Justice."
result = string1+string2
print(result)

# in python,string can't concatenation with number
string3 = "orange"
number1 = "2"
print(string3+str(number1))
# format() method can help string conatenation number,array,float
print("I am eat {} Beef.".format(3))
print("I like some drink,Ex:{}".format(["black tea", "juice", "cola"]))
print("{},{},{}".format(3.65, "come here", 69))
# can use index number
print("{1},{2},{3}".format(3.65, "come here", 69, 6.68))
print("{name},{age},{weight}".format(name="Alvin", age=27, weight=67))
# fstring method after python3.6
myName = "Alvin"
myAge = 27
print(f"My name is {myName},i am {myAge} years old.")
print("--------------")

print(len("Alvin"))  # string lenght method
print(len(""))
print("--------------")

# 大小寫轉換
string4 = "Japan"
print(string4.upper())
print(string4.lower())

# 檢查string是否都為大小寫
print(string4.upper().isupper())  # method chaining
print(string4.lower().islower())
print("--------------")

# 查看string index value
name2 = "kira"
print(name2.index("r"))
print(name2.index("ki"))
print("--------------")

# find() 和 index()最大的差別就是當找不到所要的字串時，find()會回傳-1，而index()會回傳error
print(string4.find("b"))
print(string4.find("a"))  # 如果查找的字在字串中有多個，那只會回傳第一個找到的index value
print("--------------")

# string替換函式
string5 = "Forza Horizon is a very reality game."
print(string5.replace("Forza Horizon", "Gran Turismo"))
print("--------------")
print(string5.split(" "))  # 會從目前的sub string中藉由空白鍵將每個string分開並存入一個new array
print(list(string5))  # 和split()雷同，只不過是會分開每個字母，也屬於typecasting
print("--------------")

# count() method 可以協助數sub string內有出現多少個指定的string，但會區分大小寫所以可以先把字串都換成小寫以免漏找
string6 = "In 2022,Iphone 14 Pro Max is best iphone by Apple."
print(string6.count("iphone"))
print(string6.lower().count("iphone"))
print("--------------")

# startswith(),endswith()此2個method分別可以找string的開頭及結尾分別是哪個string,substring
print(name2.startswith("K"))
print(name2.startswith("ki"))
print(name2.endswith("a"))
print(name2.endswith("ka"))
print("--------------")

# sorted method（可以將string內由字母順序做排列）
y = sorted(string6)
print(y)
print("--------------")

# Membership Operator
if "is" in string6:
    print("'is' has in", string6)
