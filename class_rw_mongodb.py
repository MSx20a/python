#要新增2個時間第一新增時間,第二編輯時間
from pymongo import MongoClient
from datetime import datetime

class RW_database():
    """
    定義連線資料庫
    """

    def __init__(self, data: dict, db_host: str, db_name: str, db_cltn: str) -> None:
        self.i_data = data
        self.host = db_host
        self.i_dbname = db_name
        self.i_cltn = db_cltn
        self.db_connect = self.connect_Mongodb()

    def connect_Mongodb(self):
        client = MongoClient(self.host)
        try:
            db = client[self.i_dbname]
            print(f"{self.i_dbname} connect success")
        except Exception as e:
            print("Error Massange:"+str(e))
        # self.db_connect = db
        return db

    def insert_doc(self):
        """
        此函式是將爬到的資料更新至MongoDB
        data: 要新增的資料 {"欄位名稱":值} ,data type dictionary
        collection:要帶入要存取資料的資料夾名稱
        """
        doc=self.db_connect[self.i_cltn].insert_one(self.i_data)
        if doc:
            print("Data insert success.")
        else:
            print("Data insert fail.")    

    def update_doc(self, n_data: dict, filer_o: dict):
        """
        將新資料更新至DB
        n_data要放入更新的data
        filer要帶需被更新的data
        """
        n_value = {"$set": n_data}
        self.db_connect[self.i_cltn].update_one(filer_o, n_value)
        #print(f"filer value is {filer_o}")
        #print(f"n_value value is {n_value}")

    def edit_ptt(self, n_data, f_name):
        db_find = self.db_connect[self.i_cltn].find_one({f_name: self.i_data[f_name]})
        #print(f"{f_name}:{self.i_data[f_name]}")
        #print(f"db_find value is {db_find}")
        if db_find:
            for key in n_data.keys():
                if n_data[key] != db_find[key]:
                    self.update_doc(n_data, {f_name: self.i_data[f_name]})
                    print(key)  #查看有哪個key被break
                    break
            else:
                print("Not update.")
        else:
            self.db_connect[self.i_cltn].insert_one(n_data)          
            print("Database haven't this data,it insert success.")

test_Data1 = {
    'url': 'https://ptt.cc/bbs/cat/index.html',
    'name': 'Cat',
    'nuser': '345555',
    'class': '寵物',
    'title': '◎喵板～',
    'new_time': datetime.now()
}

test_Data2 = {
    'url': 'https://ptt.cc/bbs/cat/index.html',
    'name': 'C',
    'nuser': '34',
    'class': '寵物',
    'title': '◎喵板～',
    'new_time': datetime.now()
}


mongo_rw = RW_database(test_Data2, "localhost:27017",
                       "pptHtml_database", "ptt")
#mongo_rw.insert_doc()
mongo_rw.edit_ptt(test_Data2, "nuser")
