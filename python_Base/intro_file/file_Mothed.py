#encoding有2種，cp950(中文預設)和utf-8
file = open("myFile.txt",encoding="cp950")
print(file)  # <_io.TextIOWrapper name='myFile.txt' mode='r' encoding='UTF-8'>
print(file.read(10))  # 如果沒有給定任何值那會直接讀取整份文件
# 下面第一個read因為上面已經先讀取前10個字因此只會讀取剩下的部分，至於最後一個因為文件內容都已經被讀完了因此讀不到任何東西
print(file.read())
print(file.read())

print("----------------------")
# 如果文件已經被讀完還需要再重新在讀一次可以用以下method
file.seek(0)  # 裡面要放指向文件裡的方位，0=重最上面開始
print(file.read())
print(type(file.read()))  # file.read() return a string

print("----------------------")
print(file.readline())  # file.readline return a string,執行第一次會讀一行
print(file.readline())  # 執行第二次會讀第二行

# 用while loop來讀取txt內容，在需要讀取內容大量文件時用此方法可避免ram被塞滿
while True:
    x = file.readline()
    if x == "":
        break
    else:
        print(x)

# print("----------------------")
print(file.readlines())  # file.readlines return a string

# 用for loop來讀取txt內容
for i in file.readlines():
    print(i)

# 讀取完記得要把檔案給關掉
file.close()
