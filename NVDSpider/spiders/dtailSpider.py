# -*- coding: utf-8 -*-
# 爬取详情
import scrapy
from NVDSpider.items import VulnItem
import re
import json
from urllib.parse import urljoin
from NVDSpider.utils import parseDate


class detailSpider(scrapy.Spider):
    name = 'detailSpider'
    allowed_domains = ['nvd.nist.gov']

    # 从json读取需要爬取的cvvid
    start_urls = ['https://nvd.nist.gov/vuln/detail/CVE-2019-15530']

    # 爬取详情
    def parse(self, response):
        # print(response.body)
        sel = response.css('div#page-content')
        vulnItem = VulnItem()
        # cvvID
        vulnItem['cvvID'] = sel.xpath('//table//h2/span/text()').extract_first()
        # 当前描述
        vulnItem['currentDes'] = sel.xpath('//table/tr/td/div/div[1]/p[@data-testid="vuln-description"]/text()').extract_first().strip()
        # 发布日期
        publishDate = sel.xpath('//table/tr/td/div/div[2]/div/span[@data-testid="vuln-published-on"]/text()').extract_first().strip()
        vulnItem['publishDate'] = parseDate(publishDate)
        # 最后修改日期
        lastModifedDate = sel.xpath('//table/tr/td/div/div[2]/div/span[@data-testid="vuln-last-modified-on"]/text()').extract_first().strip()
        vulnItem['lastModifedDate'] = parseDate(lastModifedDate)
        # CWE类型
        vulnItem['CWEType'] = sel.xpath('//table/tr/td/div/div[1]//div[@class="technicalDetails"]/ul/li/a/text()').extract_first().strip()

        impact = sel.xpath('//table/tr/td/div/div[1]/div[@data-testid="vuln-cvss-container"]')

        score_v3 = impact.xpath('div[1]/p[@data-testid="vuln-cvssv3-score-container"]')
        impact_v3 = impact.xpath('div[1]/p[@data-testid="vuln-cvssv3-metrics-container"]')
        score_v2 = impact.xpath('div[2]/p[@data-testid="vuln-cvssv2-score-container"]')
        impact_v2 = impact.xpath('div[2]/p[@data-testid="vuln-cvssv2-metrics-container"]')

        # CVSS V3.0

        # 基础分数
        baseScore_V3 = score_v3.xpath('a/span[@data-testid="vuln-cvssv3-base-score"]/text()').extract_first().strip()
        vulnItem['baseScore_V3'] = float(baseScore_V3)
        # 危险程度
        baseType_V3 = score_v3.xpath('a/span[@data-testid="vuln-cvssv3-base-score-severity"]/text()').extract_first().strip()
        vulnItem['baseType_V3'] = baseType_V3
        # 影响分数
        impactScore_V3 = score_v3.xpath('span[@data-testid="vuln-cvssv3-impact-score"]/text()').extract_first().strip()
        vulnItem['impactScore_V3'] = float(impactScore_V3)
        # 可利用性分数
        explScore_V3 = score_v3.xpath('span[@data-testid="vuln-cvssv3-exploitability-score"]/text()').extract_first().strip()
        vulnItem['explScore_V3'] = float(explScore_V3)
        # 向量
        vector_v3 = score_v3.xpath('span[@data-testid="vuln-cvssv3-vector"]/text()[1]').extract_first()
        vector_v3 = re.sub(r'[\(]$', '', vector_v3).strip()
        vulnItem['vector_V3'] = vector_v3

        # 攻击向量
        vulnItem['AV_V3'] = impact_v3.xpath('span[@data-testid="vuln-cvssv3-av"]/text()').extract_first().strip()
        # 攻击复杂性
        vulnItem['AC_V3'] = impact_v3.xpath('span[@data-testid="vuln-cvssv3-ac"]/text()').extract_first().strip()
        # 权限要求
        vulnItem['PR_V3'] = impact_v3.xpath('span[@data-testid="vuln-cvssv3-pr"]/text()').extract_first().strip()
        # 用户交互
        vulnItem['UI_V3'] = impact_v3.xpath('span[@data-testid="vuln-cvssv3-ui"]/text()').extract_first().strip()
        # 影响范围
        vulnItem['S_V3'] = impact_v3.xpath('span[@data-testid="vuln-cvssv3-s"]/text()').extract_first().strip()
        # 机密性
        vulnItem['C_V3'] = impact_v3.xpath('span[@data-testid="vuln-cvssv3-c"]/text()').extract_first().strip()
        # 完整性
        vulnItem['I_V3'] = impact_v3.xpath('span[@data-testid="vuln-cvssv3-i"]/text()').extract_first().strip()
        # 可用性
        vulnItem['A_V3'] = impact_v3.xpath('span[@data-testid="vuln-cvssv3-a"]/text()').extract_first().strip()

        # CVSS V2.0
        # 基准分数
        baseScore_V2 = score_v2.xpath('a/span[@data-testid="vuln-cvssv2-base-score"]/text()').extract_first().strip()
        vulnItem['baseScore_V2'] = float(baseScore_V2)

        vulnItem['baseType_V2'] = score_v2.xpath('a/span[@data-testid="vuln-cvssv2-base-score-severity"]/text()').extract_first().strip()
        # # 向量
        vector_v2 = score_v2.xpath('span[@data-testid="vuln-cvssv2-vector"]/text()[1]').extract_first()
        vector_v2 = re.sub(r'[\(]$', '', vector_v2).strip()
        vulnItem['vector_V2'] = vector_v2
        # 影响分数

        impactScore_V2 = score_v2.xpath('span[@data-testid="vuln-cvssv2-impact-subscore"]/text()').extract_first().strip()
        vulnItem['impactScore_V2'] = float(impactScore_V2)
        # 可利用性分数
        explScore_V2 = score_v2.xpath('span[@data-testid="vuln-cvssv2-exploitability-score"]/text()').extract_first().strip()
        vulnItem['explScore_V2'] = float(explScore_V2)

        # 攻击复杂度
        vulnItem['AV_V2'] = impact_v2.xpath('span[@data-testid="vuln-cvssv2-av"]/text()').extract_first().strip()
        # 攻击途径
        vulnItem['AC_V2'] = impact_v2.xpath('span[@data-testid="vuln-cvssv2-ac"]/text()').extract_first().strip()
        # 认证
        vulnItem['AU_V2'] = impact_v2.xpath('span[@data-testid="vuln-cvssv2-au"]/text()').extract_first().strip()
        # 机密性
        vulnItem['C_V2'] = impact_v2.xpath('span[@data-testid="vuln-cvssv3-c"]/text()').extract_first().strip()
        # 完整性
        vulnItem['I_V2'] = impact_v2.xpath('span[@data-testid="vuln-cvssv2-i"]/text()').extract_first().strip()
        # 可用性
        vulnItem['A_V2'] = impact_v2.xpath('span[@data-testid="vuln-cvssv2-a"]/text()').extract_first().strip()

        return vulnItem