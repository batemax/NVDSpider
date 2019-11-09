# -*- coding: utf-8 -*-
# 爬取每日更新
import scrapy
from scrapy.linkextractors import LinkExtractor
from NVDSpider.items import IDItem
from urllib.parse import urljoin


class increSpider(scrapy.Spider):
    name = 'increSpider'
    allowed_domains = ['cassandra.cerias.purdue.edu']
    start_urls = ['https://cassandra.cerias.purdue.edu/CVE_changes/today.html']
    custom_settings = {
        'ITEM_PIPELINES': {
            'NVDSpider.pipelines.MongoPipeline.MongoPipeline': 300
        }
    }
    # 爬取每日更新
    def parse(self, response):
        for sel in response.xpath('//a'):
            cvvid = sel.xpath('text()').extract_first().strip()
            cvvid = 'CVE-'+cvvid
            idItem = IDItem()
            url = urljoin('https://nvd.nist.gov/vuln/detail/', cvvid)
            idItem['_id'] = cvvid
            idItem['vuln_url'] = url

            # print(idItem)
            yield idItem