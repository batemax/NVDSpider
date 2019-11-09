# -*- coding: utf-8 -*-
# 下载增量文件
import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from NVDSpider.items import FileItem
from NVDSpider.items import IDItem
from urllib.parse import urljoin


class increDataSpider(scrapy.Spider):
    name = 'increDataSpider'
    allowed_domains = ['nvd.nist.gov']
    start_urls = ['https://nvd.nist.gov/vuln/data-feeds']
    custom_settings = {
        'ITEM_PIPELINES': {
            'NVDSpider.pipelines.IncreFilePipeline.IncreFilePipeline': 10
        }
    }

    # 下载zip文件
    def parse(self, response):
        sel = response.xpath('//tr[@data-testid="vuln-json-feed-row-modified-zip"]//a/@href').extract()
        regex = re.compile(r'^.*\.(json)\.(zip)$')
        filtered = [i for i in sel if regex.match(i)]
        url_list = list(filtered)
        print(url_list)
        file_item = FileItem()
        file_item['file_urls'] = url_list
        yield file_item