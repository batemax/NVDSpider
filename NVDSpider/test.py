# -*- coding: utf-8 -*-
# 主函数
import pymongo
from NVDSpider.settings import MONGO_HOST
from NVDSpider.settings import MONGO_PORT
from NVDSpider.settings import MONGO_DB
from NVDSpider.settings import MONGO_ID
from scrapy import cmdline
from NVDSpider.mongoSync import mongoSync

if __name__ == "__main__":

    # 测试爬虫
    # cmdline.execute('scrapy crawl increSpider'.split())
    cmdline.execute('scrapy crawl detailSpider'.split())
    # cmdline.execute('scrapy crawl testSpider'.split())

    # 测试初步配置
    mongo = mongoSync()
    path = "../data/"
    mongo.loadFile(path)


    # 测试数据库
    # start_urls = []
    # client = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
    # db = client[MONGO_DB]
    # coll = db[MONGO_ID]
    # results = coll.find()
    # for item in results:
    #     url = item['vuln_url']
    #     start_urls.append(url)
    # client.close()
    # print(start_urls)