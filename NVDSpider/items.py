# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class monthItem(scrapy.Item):
    # url
    href = scrapy.Field()

# cvvID
class IDItem(scrapy.Item):
    # cvvID
    cvvID = scrapy.Field()
    # url
    href = scrapy.Field()


# 漏洞详情
class NvdspiderItem(scrapy.Item):
    # cvvID
    cvvID = scrapy.Field()

