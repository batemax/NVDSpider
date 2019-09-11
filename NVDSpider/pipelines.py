# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# import pymongo
# from NVDSpider.settings import MONGO_HOST
# from NVDSpider.settings import MONGO_PORT
# from NVDSpider.settings import MONGO_USER
# from NVDSpider.settings import MONGO_PSW
# from NVDSpider.settings import MONGO_DB
# from NVDSpider.settings import MONGO_ID
# from NVDSpider.settings import MONGO_DETAIL

# class NvdspiderPipeline(object):
#     def __init__(self):
#         self.client = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
#         # self.client.admin.authenticate(MONGO_USER, MONGO_PSW)
#         self.db = self.client[MONGO_DB]  # 获得数据库的句柄
#         self.coll = self.db[MONGO_COLL]  # 获得collection的句柄
#
#     def process_item(self, item, spider):
#         postItem = dict(item)  # 把item转化成字典形式
#         self.coll.insert(postItem)  # 向数据库插入一条记录
#         return item
