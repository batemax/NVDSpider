# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NvdspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class IDItem(scrapy.Item):
    _id = scrapy.Field()
    vuln_url = scrapy.Field()

class VulnItem(scrapy.Item):
    _id = scrapy.Field()
    vuln_desc = scrapy.Field()
    vuln_url = scrapy.Field()
    rel_time = scrapy.Field()
    upd_time = scrapy.Field()

    vuln_type = scrapy.Field()

    v3_vector = scrapy.Field()
    v3_AV = scrapy.Field()
    v3_AC = scrapy.Field()
    v3_PR = scrapy.Field()
    v3_UI = scrapy.Field()
    v3_S = scrapy.Field()
    v3_C = scrapy.Field()
    v3_I = scrapy.Field()
    v3_A = scrapy.Field()
    v3_impact_score = scrapy.Field()
    v3_base_score = scrapy.Field()
    v3_exp_score = scrapy.Field()
    v3_vuln_level = scrapy.Field()

    v2_vector = scrapy.Field()
    v2_AV = scrapy.Field()
    v2_AC = scrapy.Field()
    v2_AU = scrapy.Field()
    v2_C = scrapy.Field()
    v2_I = scrapy.Field()
    v2_A = scrapy.Field()
    v2_impact_score = scrapy.Field()
    v2_base_score = scrapy.Field()
    v2_exp_score = scrapy.Field()
    v2_vuln_level = scrapy.Field()
    v2_add_info = scrapy.Field()

