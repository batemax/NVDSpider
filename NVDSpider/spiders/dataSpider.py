# -*- coding: utf-8 -*-
# 下载存量文件
import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from NVDSpider.items import FileItem
from NVDSpider.items import IDItem
from urllib.parse import urljoin


class dataSpider(scrapy.Spider):
    name = 'dataSpider'
    allowed_domains = ['nvd.nist.gov']
    start_urls = ['https://nvd.nist.gov/vuln/data-feeds']

    # 下载zip文件
    def parse(self, response):
        sel = response.xpath('//table[@data-testid="vuln-feed-table"]/tbody//a/@href').extract()
        regex = re.compile(r'^.*\.(json)\.(zip)$')
        filtered = [i for i in sel if regex.match(i)]
        url_list = list(filtered)
        print(url_list)
        file_item = FileItem()
        file_item['file_urls'] = url_list
        yield file_item
