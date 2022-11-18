# 移除檔案和資料夾的語法（會直接從電腦刪除，不會留在垃圾桶）
import os

os.remove("test.html")  # 移除檔案

os.rmdir("floder")  # 移除資料夾(只能刪除空資料夾)
