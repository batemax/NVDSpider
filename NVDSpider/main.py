# -*- coding: utf-8 -*-
# 主函数
from scrapy import cmdline
if __name__ == "__main__":
    # cmdline.execute('scrapy crawl increSpider'.split())
    cmdline.execute('scrapy crawl detailSpider'.split())
    # cmdline.execute('scrapy crawl testSpider'.split())