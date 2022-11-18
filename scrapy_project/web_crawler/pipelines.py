# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from web_crawler import settings


class WebCrawlerPipeline:
    def __init__(self) -> None:
        self.db_connect = self.connect_Mongodb()

    def connect_Mongodb(self):
        client = pymongo.MongoClient(settings.DB_HOST)
        try:
            db = client[settings.DB_NAME]
            print(f"{settings.DB_NAME} connect success")
        except Exception as e:
            print("Error Massange:"+str(e))
        return db

    def process_item(self, item, spider):
        db_find = self.db_connect[settings.DB_COLLECTION].find_one(
            {"url": item["url"]})
        if db_find:
            if item != db_find:
                o_data = db_find
                n_date = {"$set": item}
                update_doc = self.db_connect[settings.DB_COLLECTION].update_one(
                    o_data, n_date)
            else:
                print("Don't update.")
        else:
            doc = self.db_connect[settings.DB_COLLECTION].insert_one(
                ItemAdapter(item).asdict())
        return item
