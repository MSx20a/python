# shelve適用於需要轉換並開起大量資料時所使用，
# 會類以dictionary的方式開啟資料，如此一來就可以用key去尋找對應的資料；
# 相比pickle會比較節省記憶體
import shelve

with shelve.open("shelf_file", "r") as shelf_file:
    for key in shelf_file.keys():
        print(f"{key}:{shelf_file[key]}")
