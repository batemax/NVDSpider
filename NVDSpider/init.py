# -*- coding: utf-8 -*-
# 首次配置系统运行函数
import os

from mongoSync import mongoSync
from utils import unzip_file, delete_zip
from NVDSpider.settings import MONGO_VULN
from NVDSpider.settings import MONGO_RECENT


def zip2json(file_path):
    zip_result = unzip_file(file_path)
    if zip_result:
        delete_result = delete_zip(file_path)
        print("解压完成")
        return delete_result
    else:
        return zip_result


# 增量爬取执行命令
def recent_mongo(file_path):
    try:
        mongo = mongoSync(MONGO_RECENT)
        mongo.load_file(file_path)
        return True
    except:
        return False


# 第一次爬取执行命令
def init_mongo(file_path):
    try:
        mongo = mongoSync(MONGO_VULN)
        mongo.load_file(file_path)
        return True
    except:
        return False


def init_crawl():
    file_path = './data/full/'
    with os.popen('scrapy crawl dataSpider') as p:
        r = p.read()
        print(r)
    zip_result = zip2json(file_path)
        # if zip_result:
        #     init_result = init_mongo(file_path)


def recent_crawl():
    file_path = './data/recent/'
    with os.popen('scrapy crawl dataRecentSpider') as p:
        r = p.read()
        print(r)
    zip_result = zip2json(file_path)
    if zip_result:
        init_result = recent_mongo(file_path)


if __name__ == "__main__":
    recent_crawl()
    # file_path = './data/'
    # init_result = recent_mongo(file_path)
    # zip_result = zip2json(file_path)
    # if zip_result:
    #     init_result = recent_mongo(file_path)
    # data_result = data_crawl()
    # if data_result:
    #     zip_result = zip2json(file_path)
    #     if zip_result:
    #         init_result = init_mongo(file_path)
