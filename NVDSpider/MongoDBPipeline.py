from pymongo import MongoClient
from scrapy import Item
from NVDSpider.items import IDItem
from NVDSpider.items import VulnItem
from NVDSpider.settings import MONGO_HOST
from NVDSpider.settings import MONGO_PORT
from NVDSpider.settings import MONGO_DB
from NVDSpider.settings import MONGO_ID
from NVDSpider.settings import MONGO_DETAIL


class MongoDBPipeline(object):
    def __init__(self):
        # self.client.admin.authenticate(MONGO_USER, MONGO_PSW) #输入用户名密码
        self.client = MongoClient(MONGO_HOST, MONGO_PORT)      # 获取连接
        self.db = self.client[MONGO_DB]  # 获得数据库的句柄
        self.coll = self.db[MONGO_ID]  # 获得collection的句柄

    def open_spider(self,spider):
        pass

    def close_spider(self,spider):
        self.client.close()

    def process_item(self,item,spider):
        if isinstance(item, IDItem):
            self.insert_id(item)
        elif isinstance(item,VulnItem):
            self.insert_detail(item)
        return item

    def insert_id(self,item):
        self.coll = self.db[MONGO_ID]  # 获得collection的句柄
        item = dict(item)
        self.coll.insert_one(item)  # 向数据库插入一条记录
        return item

    def insert_detail(self,item):
        self.coll = self.db[MONGO_DETAIL]  # 获得collection的句柄
        item = dict(item)
        self.coll.insert_one(item)  # 向数据库插入一条记录
        return item
