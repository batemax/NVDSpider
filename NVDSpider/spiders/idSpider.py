# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from NVDSpider.items import IDItem
from NVDSpider.items import monthItem


class idSpider(scrapy.Spider):
    name = 'idSpider'
    allowed_domains = ['nvd.nist.gov']
    # start_urls = ['https://nvd.nist.gov/vuln/full-listing/']
    # start_urls = ['https://nvd.nist.gov/vuln/full-listing/2019/5']
    start_urls = ['https://nvd.nist.gov/vuln/detail/CVE-2018-1608']

    # 爬取每月list
    # def parse(self, response):
    #     le = LinkExtractor(restrict_css='ul.list-inline li')
    #     for link in le.extract_links(response):
    #         yield scrapy.Request(link.url, callback=self.parse_id)

    # 爬取cveid
    # def parse(self, response):
    #     le = LinkExtractor(restrict_css='div#page-content span.col-md-2')
    #     for link in le.extract_links(response):
    #         idItem = IDItem()
    #         idItem['href'] = link.url
    #         yield idItem


    # 爬取详情
    def parse(self,response):
        pass