# -*- coding: utf-8 -*-
# 数据库操作pipeline
import pymongo
from NVDSpider.settings import MONGO_HOST
from NVDSpider.settings import MONGO_PORT
from NVDSpider.settings import MONGO_DB
from NVDSpider.settings import MONGO_ID
from NVDSpider.settings import MONGO_VULN
from NVDSpider.items import IDItem
from NVDSpider.items import VulnItem


class MongoPipeline(object):

    def __init__(self):
        self.client = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
        self.db = self.client[MONGO_DB]  # 获得数据库的句柄

    def process_item(self, item, spider):
        if isinstance(item, IDItem):
            self.insert_id(item)
        elif isinstance(item, VulnItem):
            self.insert_vuln(item)
        return item

    def insert_id(self, item):
        id_coll = self.db[MONGO_ID]
        _id = item['_id']
        id_coll.update({'_id': _id}, {'$set': item}, upsert=True)

    def insert_vuln(self, item):
        id_coll = self.db[MONGO_ID]
        vlun_coll = self.db[MONGO_VULN]
        _id = item['_id']
        vlun_coll.update({'_id': _id}, {'$set': item}, upsert=True)
        # print("插入"+_id+ "成功")
        id_coll.find_one_and_delete({'_id': _id})
        # print("删除"+_id+ "成功")

    def close_spider(self, spider):
        self.client.close()
