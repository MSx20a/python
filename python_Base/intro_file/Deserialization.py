# dsserialization是一種將二進位轉換成object或者是python dataType，如此一來就可以判讀這些資料
# Pickle module是在python中可以用來協助做Serialization和Deserialization
import pickle

# with open("pickle_file",mode="rb") as p_file:  #"rb"=read file
#     print(pickle.load(p_file))   #第一筆資料
#     print(pickle.load(p_file))   #第二筆資料

x = None
y = None
z = None


def restore_date():
    global x, y, z
    with open("pickle_file", mode="rb") as p_file:  # "rb"=read file
        date = pickle.load(p_file)
        x = date["x"]
        y = date["y"]
        z = date["z"]


restore_date()
print(x, y, z)
