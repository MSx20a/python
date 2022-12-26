#檔案的壓縮
# zipfile modle is lossless(無失真壓縮)
import zipfile

# 5-11行為壓縮檔案
zipped_file = zipfile.ZipFile("activate_craeler.zip", "w")  #設定壓縮檔名；w=write
# 將下此二檔案打包成zip
# compress_type用預設
zipped_file.write("geckodriver.exe", compress_type=zipfile.ZIP_DEFLATED)
zipped_file.write("analyze_html_JS.py", compress_type=zipfile.ZIP_DEFLATED)
zipped_file.close()


# 15-17行為解壓縮
zipped_obj = zipfile.ZipFile("activate_craeler.zip", "r")  #放入要解壓縮的壓縮檔；r=read
zipped_obj.extractall("result")  # extractall內要放解壓縮後的路徑或資料夾
zipped_obj.close()



