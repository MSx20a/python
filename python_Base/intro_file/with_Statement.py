# 可以讓code的可閱讀性變高，在開啟檔案後也會幫我們做自動關閉動作
# open function mode:
# r = read (讀取文件，也是預設)
# a = append （新增字串到文件）
# w = write（覆寫文件）
# x = create（新增文件）

#預設mode="r"
with open("myFile.txt") as x:
    all_content = x.read()
    print(all_content)

#mode="a"
with open("myFile.txt",mode="a") as x:
    x.write("I will come back,too!!")

#mode="w"
with open("myFile.txt",mode="w") as x:
    x.write("go home and sleep.\nbody is very well.\n")

#mode="x"
try:
    with open("myFile.txt",mode="x") as x:
        pass
except Exception as e:
    print("Error Messange:" + str(e))


