# -*- coding: utf-8 -*-
# 下载存量文件
import scrapy
from scrapy.linkextractors import LinkExtractor
from NVDSpider.items import IDItem
from urllib.parse import urljoin
class dataSpider(scrapy.Spider):
    name = 'dataSpider'
    allowed_domains = ['nvd.nist.gov']
    start_urls = ['http://nvd.nist.gov/']

    # 爬取每月list
    def parse(self, response):
        le = LinkExtractor(restrict_css='ul.list-inline li')
        for link in le.extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse_id)