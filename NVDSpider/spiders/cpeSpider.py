# -*- coding: utf-8 -*-
# 爬取CPE信息
import scrapy


class cpeSpider(scrapy.Spider):
    name = 'cpeSpider'
    allowed_domains = ['nvd.nist.gov']
    start_urls = ['https://nvd.nist.gov/vuln/detail/CVE-2011-2083/cpes']

    # 爬取每日更新
    def parse(self, response):
        sel = response.css('//div#vulnCpeTree')
        