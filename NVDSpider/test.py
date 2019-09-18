# -*- coding: utf-8 -*-
# 主函数
import os
import pymongo
from NVDSpider.settings import MONGO_HOST
from NVDSpider.settings import MONGO_PORT
from NVDSpider.settings import MONGO_DB
from NVDSpider.settings import MONGO_ID
from scrapy import cmdline
from NVDSpider.mongoSync import mongoSync

def initMongo():
    try:
        mongo = mongoSync()
        path = "./data/"
        mongo.loadFile(path)
        return True
    except:
        return False

def increCrawl():
    try:
        os.system('scrapy crawl increSpider')
        # cmdline.execute('scrapy crawl increSpider'.split())
        return True
    except:
        return False

def detailCrawl():
    try:
        os.system('scrapy crawl detailSpider')
        # cmdline.execute('scrapy crawl detailSpider'.split())
        return True
    except:
        return False

def testCrawl():
    try:
        os.system('scrapy crawl testSpider')
        # cmdline.execute('scrapy crawl testSpider'.split())
        return True
    except:
        return False

if __name__ == "__main__":

    # try:
    #     print(a)
    # except:
    #     print("b")
    # finally:
    #     print("finally")
    # print("ok")

    # 测试爬虫
    # cmdline.execute('scrapy crawl increSpider'.split())
    # cmdline.execute('scrapy crawl detailSpider'.split())
    # cmdline.execute('scrapy crawl testSpider'.split())

    # 执行
    incre_result = increCrawl()
    print(incre_result)
    print("增量爬取ID完成")
    if incre_result:
        detail_result = detailCrawl()
        print(detail_result)
        print("增量爬取详情完成")

    # 测试初步配置
    # result = initMongo()
    # print(result)
    # if result:
    #     cmdline.execute('scrapy crawl increSpider'.split())

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