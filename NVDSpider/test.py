# -*- coding: utf-8 -*-
# 测试函数
import os
from NVDSpider.mongoSync import mongoSync
from NVDSpider.utils import unzip_file
from NVDSpider.utils import delete_zip


def zip2json(file_path):
    zip_result = unzip_file(file_path)
    if zip_result:
        delete_result = delete_zip(file_path)
        print("解压完成")
        return delete_result
    else:
        return zip_result


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


def dataCrawl():
    try:
        os.system('scrapy crawl dataSpider')
        print("下载完成")
        return True
    except:
        return False

def increDataCrawl():
    try:
        os.system('scrapy crawl increDataSpider')
        print("下载完成")
        return True
    except:
        return False

if __name__ == "__main__":
    # incre_result = increCrawl()
    # if incre_result:
    file_path = './data/incre/'
    data_result = increDataCrawl()
    if data_result:
        zip_result = zip2json(file_path)
