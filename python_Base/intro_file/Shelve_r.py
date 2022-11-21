# shelve適用於純存大量資料時所使用，
# 和pickle一樣會轉換成二進位儲存
# 缺點也是安全性不足
import shelve

x = (2, 6, 9, 1)
y = [0, "o", "eeg", 45, 11]
z = {"food": "prok", "fruit": "orange"}

with shelve.open("shelf_file", "c") as s_file:
    s_file["x"] = x
    s_file["y"] = y
    s_file["z"] = z
