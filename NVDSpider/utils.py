# -*- coding: utf-8 -*-
# 工具函数

# 转换漏洞等级到数字
def trans_level(str):
    if str == "CRITICAL":
        return 5
    elif str == "HIGH":
        return 4
    elif str == "MEDIUM":
        return 3
    elif str == "LOW":
        return 2
    elif str == "HIGH":
        return 4
    else:
        return 0