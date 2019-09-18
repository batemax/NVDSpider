# -*- coding: utf-8 -*-
# 测试爬虫
import re
from datetime import datetime

import scrapy
from urllib.parse import urljoin
from NVDSpider.items import VulnItem

class detailSpider(scrapy.Spider):
    name = 'testSpider'
    allowed_domains = ['nvd.nist.gov']
    start_urls = ['https://nvd.nist.gov/vuln/detail/CVE-2019-15927']
    # 爬取每日更新
    def parse(self, response):
        sel = response.css('div#page-content')
        vulnItem = VulnItem()

        vuln_id = sel.xpath('//span[@data-testid="page-header-vuln-id"]/text()').extract_first()
        rel_time = sel.xpath('//span[@data-testid="vuln-published-on"]/text()').extract_first()
        upd_time = sel.xpath('//span[@data-testid="vuln-last-modified-on"]/text()').extract_first()
        vuln_desc = sel.xpath('//p[@data-testid="vuln-description"]/text()').extract_first()
        vuln_url = urljoin('https://nvd.nist.gov/vuln/detail/', vuln_id)

        vulnItem['_id'] = vuln_id
        vulnItem['rel_time'] = datetime.strptime(rel_time, '%m/%d/%Y')
        vulnItem['upd_time'] = datetime.strptime(upd_time, '%m/%d/%Y')
        vulnItem['vuln_desc'] = vuln_desc
        vulnItem['vuln_url'] = vuln_url

        # 是否有参考信息
        try:
            hyper_link = sel.xpath('//table[@data-testid="vuln-hyperlinks-table"]/tbody')
            vuln_ref = []
            for tr in hyper_link.xpath('tr'):
                ref_data = {}
                ref_url = tr.xpath('td[1]/a/@href').extract_first()
                ref_tags = []
                for tag in tr.xpath('td[2]/span'):
                    tag = tag.xpath('text()').extract_first()
                    ref_tags.append(tag)
                ref_data['ref_url'] = ref_url
                ref_data['ref_tags'] = ref_tags
                vuln_ref.append(ref_data)
            vulnItem['vuln_ref'] = vuln_ref
        except:
            print(vuln_id+"没有参考信息")

        # 是否有v2信息
        try:
            impact = sel.xpath('//div[@data-testid="vuln-cvss-container"]')
            v2_score = impact.xpath('//p[@data-testid="vuln-cvssv3-score-container"]')
            v2_metric = impact.xpath('//p[@data-testid="vuln-cvssv3-metrics-container"]')

            v2_vector = v2_score.xpath('//span[@data-testid="vuln-cvssv2-vector"]/text()').extract_first().strip()
            v2_impact_score = v2_score.xpath(
                '//span[@data-testid="vuln-cvssv2-impact-subscore"]/text()').extract_first().strip()
            v2_base_score = v2_score.xpath(
                '//span[@data-testid="vuln-cvssv2-base-score"]/text()').extract_first().strip()
            v2_exp_score = v2_score.xpath(
                '//span[@data-testid="vuln-cvssv2-exploitability-score"]/text()').extract_first().strip()
            v2_vuln_level = v2_score.xpath(
                '//span[@data-testid="vuln-cvssv2-base-score-severity"]/text()').extract_first().strip()

            v2_AV = v2_metric.xpath('//span[@data-testid="vuln-cvssv2-av"]/text()').extract_first().strip()
            v2_AC = v2_metric.xpath('//span[@data-testid="vuln-cvssv2-ac"]/text()').extract_first().strip()
            v2_AU = v2_metric.xpath('//span[@data-testid="vuln-cvssv2-au"]/text()').extract_first().strip()
            v2_C = v2_metric.xpath('//span[@data-testid="vuln-cvssv3-c"]/text()').extract_first().strip()
            v2_I = v2_metric.xpath('//span[@data-testid="vuln-cvssv2-i"]/text()').extract_first().strip()
            v2_A = v2_metric.xpath('//span[@data-testid="vuln-cvssv2-a"]/text()').extract_first().strip()

            v2_add_info = []
            for add_info in v2_metric.xpath('//span[@data-testid="vuln-cvssv2-additional"]/text()').extract():
                if add_info.strip() != '':
                    v2_add_info.append(add_info.strip())

            vulnItem['v2_vector'] = re.sub(r'[(]$', '', v2_vector).strip()
            vulnItem['v2_impact_score'] = float(v2_impact_score)
            vulnItem['v2_base_score'] = float(v2_base_score)
            vulnItem['v2_exp_score'] = float(v2_exp_score)
            vulnItem['v2_vuln_level'] = v2_vuln_level
            vulnItem['v2_AV'] = v2_AV
            vulnItem['v2_AC'] = v2_AC
            vulnItem['v2_AU'] = v2_AU
            vulnItem['v2_C'] = v2_C
            vulnItem['v2_I'] = v2_I
            vulnItem['v2_A'] = v2_A
            vulnItem['v2_add_info'] = v2_add_info
        except:
            print(vuln_id+"没有V2信息")
        else:
            # 是否有v3信息
            try:
                v3_score = impact.xpath('//p[@data-testid="vuln-cvssv3-score-container"]')
                v3_metric = impact.xpath('//p[@data-testid="vuln-cvssv3-metrics-container"]')

                v3_vector = v3_score.xpath('//span[@data-testid="vuln-cvssv3-vector"]/text()').extract_first().strip()
                v3_impact_score = v3_score.xpath(
                    '//span[@data-testid="vuln-cvssv3-impact-score"]/text()').extract_first().strip()
                v3_base_score = v3_score.xpath(
                    '//span[@data-testid="vuln-cvssv3-base-score"]/text()').extract_first().strip()
                v3_exp_score = v3_score.xpath(
                    '//span[@data-testid="vuln-cvssv3-exploitability-score"]/text()').extract_first().strip()
                v3_vuln_level = v3_score.xpath(
                    '//span[@data-testid="vuln-cvssv3-base-score-severity"]/text()').extract_first().strip()

                v3_AV = v3_metric.xpath('//span[@data-testid="vuln-cvssv3-av"]/text()').extract_first().strip()
                v3_AC = v3_metric.xpath('//span[@data-testid="vuln-cvssv3-ac"]/text()').extract_first().strip()
                v3_PR = v3_metric.xpath('//span[@data-testid="vuln-cvssv3-pr"]/text()').extract_first().strip()
                v3_UI = v3_metric.xpath('//span[@data-testid="vuln-cvssv3-ui"]/text()').extract_first().strip()
                v3_S = v3_metric.xpath('//span[@data-testid="vuln-cvssv3-s"]/text()').extract_first().strip()
                v3_C = v3_metric.xpath('//span[@data-testid="vuln-cvssv3-c"]/text()').extract_first().strip()
                v3_I = v3_metric.xpath('//span[@data-testid="vuln-cvssv3-i"]/text()').extract_first().strip()
                v3_A = v3_metric.xpath('//span[@data-testid="vuln-cvssv3-a"]/text()').extract_first().strip()

                vulnItem['v3_vector'] = re.sub(r'[(]$', '', v3_vector).strip()
                vulnItem['v3_impact_score'] = float(v3_impact_score)
                vulnItem['v3_base_score'] = float(v3_base_score)
                vulnItem['v3_exp_score'] = float(v3_exp_score)
                vulnItem['v3_vuln_level'] = v3_vuln_level
                vulnItem['v3_AV'] = v3_AV
                vulnItem['v3_AC'] = v3_AC
                vulnItem['v3_PR'] = v3_PR
                vulnItem['v3_UI'] = v3_UI
                vulnItem['v3_S'] = v3_S
                vulnItem['v3_C'] = v3_C
                vulnItem['v3_I'] = v3_I
                vulnItem['v3_A'] = v3_A
            except:
                print(vuln_id+"没有V3信息")
        finally:
            print(vulnItem)
            # return vulnItem
    def close_spider(self):
        self.client.close()