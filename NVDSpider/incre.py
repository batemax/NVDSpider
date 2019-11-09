# -*- coding: utf-8 -*-
# 每天抓取增量文件
import os

from mongoSync import mongoSync
from utils import unzip_file, delete_zip

def zip2json(file_path):
    zip_result = unzip_file(file_path)
    if zip_result:
        delete_result = delete_zip(file_path)
        print("解压完成")
        return delete_result
    else:
        return zip_result

