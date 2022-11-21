# Serialization是一種將object或者是基本資料型態(dict,list,set.....)轉換成二進位，只有socket和byte code不行；
# 如此一來就可以將這些資訊存於資料庫中或者是用於2種以上不同系統的伺服器間傳遞資料；
# 但他也有一些缺點：轉換後檔案不會變小、有安全性的問題
# Pickle module是在python中可以用來協助做Serialization和Deserialization
import pickle

# x=10
# y=[2,56,23,97]

# with open("pickle_file",mode="wb") as p_file:   #"wb"=write file
#     pickle.dump(x,p_file)  #parameter （要被轉換的varible,要放入的檔案名）
#     pickle.dump(y,p_file)


# 通常在把資料作儲存時都會使用dictionary的資料類型，方便我們可以在讀取資料時
x = 35
y = [2, 55, 12, 77]
z = "hello"


def save_file():
    global x, y, z
    with open("pickle_file", mode="wb") as p_file:  # "wb"=write file
        date = {
            "x": x,
            "y": y,
            "z": z
        }
        pickle.dump(date, p_file)


save_file()
