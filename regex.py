import re

st1 = "My name is Alivn,is very strong."

mh = "is"

# re method
r = re.search(mh, st1)  # 只會找到第一個符合的，如果找不到會回傳None

print(r)
print(r.group())  # 會回傳找到的結果
print(r.span())  # 會回傳是在哪個位置找到的
print(r.start())  # 8
print(r.end())  # 10

f = re.findall(mh, st1)  # 會找到所有符合的，並用list回傳
print(f)

print("-----------------")

# re syntax
print(r"\n")  # raw String


text1 = "hello,hodeo,hcdeo,h39io"

print(re.findall(r"h[a-f][rds][use]o", text1))  # 可以用中括號來設定要尋找的內容

print(re.findall(r"he..o", text1))  # ..代表2個任意字，所以只要開頭he結尾o都會符合，因此得到結果['hello']

text2 = "a,ab,abbb,abbbbbbc,abbbbd"

print(re.findall(r"ab*", text2))  # 會找到有b(一個或以上)或沒有b的對象

print(re.findall(r"ab+", text2))  # 會找到有b(一個或以上)的對象

print(re.findall(r"h[a-z]*o", text1))  # *,+也可以和[]混著用

text3 = "h1,h56,h249,h39482"

print(re.findall(r"h\d{3}", text3))  # 會尋找符合十進位的3位數，結果['h249', 'h394']

# 會尋找符合十進位且1位以上的數，結果['h1', 'h56', 'h249', 'h39482']
print(re.findall(r"h\d{1,}", text3))

# 會尋找符合十進位1-2位的數，結果['h1', 'h56', 'h24', 'h39']
print(re.findall(r"h\d{1,2}", text3))

text4 = "My phone number is 0800-560731,and home number is 02-6239011."

print(re.findall(r"p\D{4}", text4))  # 會尋找符合非十進位數

print(re.findall(r"0\w+-\w+", text4))  # 會尋找符合的數字或英文字

print(re.findall(r"\W", text4))  # 會尋找符合非數字或英文字

print(re.findall(r"\s", text4))  # 會尋找符合有空白鍵

print(re.findall(r"\S", text4))  # 會尋找符合沒有空白鍵

print(re.findall(r"\.", text4))  # 會尋找.

print(re.findall(r"\bnum", text4))  # 會找到符合num而且前面要有empty string的

print(re.findall(r"[a-zA-Z]*\S|[0-9]*\S", text4))  # | == or

# 判斷e-mail
# reg1=reg2
reg1 = r"\b[A-Za-z0-9.&#$%-]+@[A-Za-z]+\.[A-Za-z.]{2,}\b"
# 有2種意思,第一種^[@A-Z0-9]是指只要@,A-Z,0-9；第二種[^@]是指排除@以外的都可以
reg2 = r"\b[^@]+@[^[@0-9]]+\.[^@]{2,}\b"


def check_email(x: str):
    if re.match(reg2, x):
        print(f"{x} is a e-mail.")
    else:
        print(f"{x} is not a e-mail.")


e1 = "rg#h$j7%y@gmail.com"
e2 = "grokhtr.google.tw"
e3 = "67gt.ht@yahoo.com.tw"

check_email(e1)
check_email(e2)
check_email(e3)
print("-----------------------")

text5 = "My phone number is 808-733-0277 and 71-439-5112"

r = re.findall(r"(\d{2,3})-(\d{3})-(\d{3})", text5)  # 將搜尋條件都加上()就會以tuple的方式輸出

print(type(r[1]))

for area, m, e in r:
    if area == "808":
        print(f"{area}-{m}-{e} is from Hawaii.")
    else:
        print(f"{area}-{m}-{e} is from other area.")
