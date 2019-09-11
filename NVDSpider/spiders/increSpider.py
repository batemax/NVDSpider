# -*- coding: utf-8 -*-
# 增量爬取，爬取每天增量
import scrapy
from NVDSpider.items import IDItem

class increSpider(scrapy.Spider):
    name = 'increSpider'
    allowed_domains = ['https://cassandra.cerias.purdue.edu/']
    start_urls = ['https://cassandra.cerias.purdue.edu/CVE_changes/today.html']

    # 爬取cvvid
    def parse(self, response):
        for sel in response.css('a'):
            cvvid = sel.xpath('text()').extract_first().strip()
            cvvid = 'CVE-' + cvvid
            idItem = IDItem()
            idItem['cvvID'] = cvvid
            yield idItem

