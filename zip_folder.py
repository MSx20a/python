# 資料夾的壓縮
import shutil

# 5-8行為壓縮資料夾
folder_zip = "D:\\VScode program\\python\\parectic\\collection_module"
output_name = "D:\\VScode program\\python\\parectic\\collection"

shutil.make_archive(output_name, "zip", folder_zip) 


# 12-15行為解壓縮資料夾
folder_unzip = "D:\\VScode program\\python\\parectic\\collection.zip"
unzip_name = "D:\\VScode program\\python\\parectic\\collection_md"

shutil.unpack_archive(folder_unzip, unzip_name, "zip")
