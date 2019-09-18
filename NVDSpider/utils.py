# -*- coding: utf-8 -*-
# 工具函数
import os
import zipfile

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

# 解压文件夹内zip
def unzip_file(folder_path):
    try:
        files = os.listdir(folder_path)
        for file in files:
            file = folder_path + file
            if zipfile.is_zipfile(file):
                file_list = zipfile.ZipFile(file, 'r')
                for zf in file_list.namelist():
                    file_list.extract(zf, folder_path)
        return True
    except:
        return False

# 解压后删除zip
def delete_zip(folder_path):
    try:
        files = os.listdir(folder_path)
        for file in files:
            file = folder_path + file
            if zipfile.is_zipfile(file):
                os.remove(file)
        return True
    except:
        return False
