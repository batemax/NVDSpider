# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from NVDSpider.items import MonthItem
from NVDSpider.items import VulnItem

class idSpider(scrapy.Spider):
    name = 'idSpider'
    allowed_domains = ['nvd.nist.gov']
    start_urls = ['https://nvd.nist.gov/vuln/full-listing/']

    # 爬取每月list
    def parse(self, response):
        # print(response.body)
        num = 0
        le = LinkExtractor(restrict_css='ul.list-inline li')
        for link in le.extract_links(response):
            if num < 9:
                num = num + 1
                yield scrapy.Request(link.url, callback=self.parse_id)
            else:
                return scrapy.Request(link.url, callback=self.parse_id)

    # 爬取cveid
    def parse_id(self, response):
        # print(response.body)
        num = 0
        le = LinkExtractor(restrict_css='div#page-content span.col-md-2')
        for link in le.extract_links(response):
            if num < 9:
                num = num + 1
                yield scrapy.Request(link.url, callback=self.parse_detail)
            else:
                return scrapy.Request(link.url, callback=self.parse_detail)


    # 爬取详情
    def parse_detail(self,response):
        # print(response.body)
        sel = response.css('div#page-content')
        vulnItem = VulnItem()
        # cvvID
        vulnItem['cvvID'] = sel.xpath('//table//h2/span/text()').extract_first()
        # 当前描述
        vulnItem['currentDes'] = sel.xpath('//table/tr/td/div/div[1]/p[@data-testid="vuln-description"]/text()').extract_first().strip()
        # 发布日期
        vulnItem['publishDate'] = sel.xpath('//table/tr/td/div/div[2]/div/span[@data-testid="vuln-published-on"]/text()').extract_first().strip()
        # 最后修改日期
        vulnItem['lastModifedDate'] = sel.xpath('//table/tr/td/div/div[2]/div/span[@data-testid="vuln-last-modified-on"]/text()').extract_first().strip()
        # CWE类型
        vulnItem['CWEType'] = sel.xpath('//table/tr/td/div/div[1]//div[@class="technicalDetails"]/ul/li/a/text()').extract_first().strip()


        impact = sel.xpath('//table/tr/td/div/div[1]/div[@data-testid="vuln-cvss-container"]')

        score_v3 = impact.xpath('/div[1]/p[@data-testid="vuln-cvssv3-score-container"]')
        impact_v3 = impact.xpath('/div[1]/p[@data-testid="vuln-cvssv3-metrics-container"]')
        score_v2 = impact.xpath('/div[2]/p[@data-testid="vuln-cvssv2-score-container"]')
        impact_v2 = impact.xpath('/div[2]/p[@data-testid="vuln-cvssv2-metrics-container"]')

        # CVSS V3.0

        # 基础分数
        vulnItem['baseScore_V3'] = score_v3.xpath('/div[1]/p[@data-testid="vuln-cvssv3-score-container"]/a/span[@data-testid="vuln-cvssv3-base-score"]/text()').extract_first().strip()
        # 漏洞类型
        vulnItem['baseType_V3'] = score_v3.xpath('//table/tr/td/div/div[1]/div[@data-testid="vuln-cvss-container"]/div[1]/p[@data-testid="vuln-cvssv3-score-container"]/a/span[@data-testid="vuln-cvssv3-base-score"]/text()').extract_first().strip()
        # 影响分数
        vulnItem['impactScore_V3'] = score_v3.xpath('//table/tr/td/div/div[1]/div[1]/div[1]/p[1]/span[2]/text()').extract_first().strip()
        # 可利用性分数
        vulnItem['explScore_V3'] = score_v3.xpath('//table/tr/td/div/div[1]/div[1]/div[1]/p[1]/span[3]/text()').extract_first().strip()
        # 向量
        vector_v3 = score_v3.xpath('//table/tr/td/div/div[1]/div[1]/div[1]/p[1]/span[1]/text()[1]').extract_first()
        vector_v3 = re.sub(r'[\(]$','',vector_v3).strip()
        vulnItem['vector_V3'] = vector_v3

        # 攻击向量
        vulnItem['AV_V3'] = impact_v3.xpath('//table/tr/td/div/div[1]/div[1]/div[1]/p[2]/span[1]/text()').extract_first().strip()
        # 攻击复杂性
        vulnItem['AC_V3'] = impact_v3.xpath('//table/tr/td/div/div[1]/div[1]/div[1]/p[2]/span[2]/text()').extract_first().strip()
        # 权限要求
        vulnItem['PR_V3'] = impact_v3.xpath('//table/tr/td/div/div[1]/div[1]/div[1]/p[2]/span[3]/text()').extract_first().strip()
        # 用户交互
        vulnItem['UI_V3'] = impact_v3.xpath('//table/tr/td/div/div[1]/div[1]/div[1]/p[2]/span[4]/text()').extract_first().strip()
        # 影响范围
        vulnItem['S_V3'] = impact_v3.xpath('//table/tr/td/div/div[1]/div[1]/div[1]/p[2]/span[5]/text()').extract_first().strip()
        # 机密性
        vulnItem['C_V3'] = impact_v3.xpath('//table/tr/td/div/div[1]/div[1]/div[1]/p[2]/span[6]/text()').extract_first().strip()
        # 完整性
        vulnItem['I_V3'] = impact_v3.xpath('//table/tr/td/div/div[1]/div[1]/div[1]/p[2]/span[7]/text()').extract_first().strip()
        # 可用性
        vulnItem['A_V3'] = impact_v3.xpath('//table/tr/td/div/div[1]/div[1]/div[1]/p[2]/span[8]/text()').extract_first().strip()

        # CVSS V2.0
        # 基准分数
        vulnItem['baseScore_V2'] = score_v2.xpath('//table/tr/td/div/div[1]/div[1]/div[2]/p[1]/a/span[1]/text()').extract_first().strip()
        # # 向量
        vector_v2 = score_v2.xpath('//table/tr/td/div/div[1]/div[1]/div[2]/p[1]/span[1]/text()[1]').extract_first()
        vector_v2 = re.sub(r'[\(]$', '', vector_v2).strip()
        vulnItem['vector_V2'] = vector_v2
        # 影响分数
        vulnItem['impactScore_V2'] = score_v2.xpath('//table/tr/td/div/div[1]/div[1]/div[2]/p[1]/span[2]/text()').extract_first().strip()
        # 可利用性分数
        vulnItem['explScore_V2'] = score_v2.xpath('//table/tr/td/div/div[1]/div[1]/div[2]/p[1]/span[3]/text()').extract_first().strip()

        # 攻击复杂度
        vulnItem['AV_V2'] = impact_v2.xpath('//table/tr/td/div/div[1]/div[1]/div[2]/p[2]/span[1]/text()').extract_first().strip()
        # 攻击途径
        vulnItem['AC_V2'] = impact_v2.xpath('//table/tr/td/div/div[1]/div[1]/div[2]/p[2]/span[2]/text()').extract_first().strip()
        # 认证
        vulnItem['AU_V2'] = impact_v2.xpath('//table/tr/td/div/div[1]/div[1]/div[2]/p[2]/span[3]/text()').extract_first().strip()
        # 机密性
        vulnItem['C_V2'] = impact_v2.xpath('//table/tr/td/div/div[1]/div[1]/div[2]/p[2]/span[4]/text()').extract_first().strip()
        # 完整性
        vulnItem['I_V2'] = impact_v2.xpath('//table/tr/td/div/div[1]/div[1]/div[2]/p[2]/span[5]/text()').extract_first().strip()
        # 可用性
        vulnItem['A_V2'] = impact_v2.xpath('//table/tr/td/div/div[1]/div[1]/div[2]/p[2]/span[6]/text()').extract_first().strip()

        return vulnItem

