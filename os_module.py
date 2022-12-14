# os module可以協助跨系統處理文件，不會因路徑格式不同而造成code無法運行的情況發生

import os
import sys
import send2trash
import shutil
from pprint import pprint

print(os.getcwd())  # cwd=currect working dirctory，指的是目前所在資料夾

# 會回傳list，裡面包含目前資料夾的所有檔案；也可以在內部用參數path=""來指定要查看的資料夾
print(os.listdir(os.curdir))

pprint(os.listdir(path="D:\\NEW_v"))

print(os.pardir)  # 會回傳..，代表parent dirctory

pprint(os.listdir(os.pardir))

os.rename("old_path", "new_path")  # 重新命名檔案名稱

os.remove("file_path")  # 移除檔案和資料夾(空的才能移除，不然會出現error)；注意:因為不被移置類圾桶，所以無法復原

send2trash.send2trash("file_name or file_path")  # 用此module可以將移除的檔案放入垃圾桶

shutil.rmtree("foider_name")  # 刪除不是空的資料夾

os.rmdir("dirctory_path")  # 重新命名資料夾名稱

# 如果沒給定路徑那就會在cwd(currect working dirctory)建立資料夾
os.mkdir("C:\\Users\\xrsen\\Downloads\\new_folder")


# os.path常用的method

print(os.path.join("html_code", "hello.html"))  # 可以將前後的字串組合成鏈結

x = "D:\\x-t2\\DSCF13008.jpg"

print(os.path.split(x))  # 會回傳tuple，(dirname,basename)

print(os.path.dirname(x))

print(os.path.basename(x))

# 此method在做檔案分類時很方便
print(os.path.splitext(x))  # 會回傳tuple，(檔案路徑,副檔名)

print(os.path.abspath("analyze_html_JS.py"))  # 會回傳檔案的絕對路徑

print(os.path.isfile("D:\\NEW_v"))  # 會判斷此路徑是否為檔案，並回傳一個boolean

print(os.path.isdir("D:\\NEW_v"))  # 會判斷此路徑是否為資料夾，並回傳一個boolean

print(os.path.exists("D:\\NEW"))  # 會判斷此路徑是否存在，並回傳一個boolean


# os constants

print(os.name)  # windows會回傳nt(New Technology)，微軟的檔案系統NTFS(New Technology File System)

print(sys.platform)  # 會回傳作業系統的詳細資訊，但如果是win64也只會回傳win32


# os.walk("folderName") 可以遍歷指定資料夾內部的所有檔案
# 是依照Depth-First(深度優先)的演算法來遍歷資料夾內的檔案


class REFILE():
    """
    可以刪除指定資料夾內的所有相同類型的副檔名
    """

    def __init__(self, folderName:str, fileExtension:str) -> None:
        self.folderName = folderName  # 檔案名稱
        self.fileExtension = fileExtension  # 副檔名

    def Walking(self):
        # os.walk會回傳Tuple，(路徑,內部資料夾名稱,內部檔案名)
        for root, dirs, file in os.walk(self.folderName):
            for f in file:
                # 將檔案的副檔名取出；os.path.splitext有會還傳Tuple
                f_Name, f_Extension = os.path.splitext(f)
                if f_Extension == self.fileExtension:
                    os.remove(os.path.join(root, f))  # os.remove內要放檔案的完整路徑
