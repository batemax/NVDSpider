# -*- coding: utf-8 -*-
# 首次配置系统运行函数
import os

from mongoSync import mongoSync
from utils import unzip_file, delete_zip


def zip2json(file_path):
    zip_result = unzip_file(file_path)
    if zip_result:
        delete_result = delete_zip(file_path)
        print("解压完成")
        return delete_result
    else:
        return zip_result


def data_crawl():
    try:
        os.system('scrapy crawl dataSpider')
        print("下载完成")
        return True
    except:
        return False


def init_mongo(file_path):
    try:
        mongo = mongoSync()
        mongo.load_file(file_path)
        return True
    except:
        return False


if __name__ == "__main__":
    file_path = './data/full/'
    # init_result = init_mongo(file_path)



    data_result = data_crawl()
    if data_result:
        zip_result = zip2json(file_path)
        if zip_result:
            init_result = init_mongo(file_path)
