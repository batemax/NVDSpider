# -*- coding: utf-8 -*-
# 爬取ID
import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from NVDSpider.items import IDItem
from urllib.parse import urljoin

class idSpider(scrapy.Spider):
    name = 'idSpider'
    allowed_domains = ['nvd.nist.gov']
    start_urls = ['https://nvd.nist.gov/vuln/full-listing/']

    # 爬取每月list
    def parse(self, response):
        le = LinkExtractor(restrict_css='ul.list-inline li')
        for link in le.extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse_id)

    # 爬取cveid
    def parse_id(self, response):
        for sel in response.css('div#page-content div.row span.col-md-2'):
            # url = sel.xpath('a/@href').extract_first().strip()
            cvvid = sel.xpath('a/text()').extract_first().strip()
            idItem = IDItem()
            # url = urljoin('https://nvd.nist.gov',url)
            idItem['cvvID'] = cvvid
            # idItem['url'] = url
            yield idItem
            # yield cvvid