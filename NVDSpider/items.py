# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MonthItem(scrapy.Item):
    # url
    href = scrapy.Field()

# cvvID
class IDItem(scrapy.Item):
    # cvvID
    cvvID = scrapy.Field()
    # url
    href = scrapy.Field()

# V3标准的影响
class CVSSV3(scrapy.Item):
    # 基准分数
    baseScore_V3 = scrapy.Field()
    # 漏洞危险程度
    baseType_V3 = scrapy.Field()
    # 向量
    vector_V3 = scrapy.Field()
    # 影响分数
    impactScore_V3 = scrapy.Field()
    # 可利用性分数
    explScore_V3 = scrapy.Field()

    # 攻击向量
    AV_V3 = scrapy.Field()
    # 攻击复杂性
    AC_V3 = scrapy.Field()
    # 权限要求
    PR_V3 = scrapy.Field()
    # 用户交互
    UI_V3 = scrapy.Field()
    # 影响范围
    S_V3 = scrapy.Field()
    # 机密性
    C_V3 = scrapy.Field()
    # 完整性
    I_V3 = scrapy.Field()
    # 可用性
    A_V3 = scrapy.Field()

# V2标准的影响
class CVSSV2(scrapy.Item):
    # 基准分数
    baseScore_V2 = scrapy.Field()
    # 漏洞危险程度
    baseType_V2 = scrapy.Field()
    # 向量
    vector_V2 = scrapy.Field()
    # 影响分数
    impactScore_V2 = scrapy.Field()
    # 可利用性分数
    explScore_V2 = scrapy.Field()

    # 攻击复杂度
    AV_V2 = scrapy.Field()
    # 攻击途径
    AC_V2 = scrapy.Field()
    # 认证
    AU_V2 = scrapy.Field()
    # 机密性
    C_V2 = scrapy.Field()
    # 完整性
    I_V2 = scrapy.Field()
    # 可用性
    A_V2 = scrapy.Field()
    #
    addInfo_V2 = scrapy.Field()


# 漏洞详情
class VulnItem(scrapy.Item):
    # cvvID
    cvvID = scrapy.Field()
    # 当前描述
    currentDes = scrapy.Field()
    # 分析描述
    # analDes = scrapy.Field()
    # 发布日期
    publishDate = scrapy.Field()
    # 最后修改日期
    lastModifedDate = scrapy.Field()
    # CWE类型
    CWEType = scrapy.Field()
    # CWE描述
    # CWEDetail = scrapy.Field()
    # CVSSV3
    # 基准分数
    baseScore_V3 = scrapy.Field()
    # 漏洞危险程度
    baseType_V3 = scrapy.Field()
    # 向量
    vector_V3 = scrapy.Field()
    # 影响分数
    impactScore_V3 = scrapy.Field()
    # 可利用性分数
    explScore_V3 = scrapy.Field()

    # 攻击向量
    AV_V3 = scrapy.Field()
    # 攻击复杂性
    AC_V3 = scrapy.Field()
    # 权限要求
    PR_V3 = scrapy.Field()
    # 用户交互
    UI_V3 = scrapy.Field()
    # 影响范围
    S_V3 = scrapy.Field()
    # 机密性
    C_V3 = scrapy.Field()
    # 完整性
    I_V3 = scrapy.Field()
    # 可用性
    A_V3 = scrapy.Field()
    # cvssV3 = CVSSV3()

    # CVSSV2
    # 基准分数
    baseScore_V2 = scrapy.Field()
    # 向量
    vector_V2 = scrapy.Field()
    # 影响分数
    impactScore_V2 = scrapy.Field()
    # 可利用性分数
    explScore_V2 = scrapy.Field()

    # 攻击复杂度
    AV_V2 = scrapy.Field()
    # 攻击途径
    AC_V2 = scrapy.Field()
    # 认证
    AU_V2 = scrapy.Field()
    # 机密性
    C_V2 = scrapy.Field()
    # 完整性
    I_V2 = scrapy.Field()
    # 可用性
    A_V2 = scrapy.Field()
    #
    # addInfo_V2 = scrapy.Field()








