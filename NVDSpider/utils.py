# -*- coding: utf-8 -*-
# 工具函数

from datetime import datetime

def parseDate(s):
    mon_s, day_s, year_s = s.split('/')
    return datetime(int(year_s), int(mon_s), int(day_s))