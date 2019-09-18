# -*- coding: utf-8 -*-
# 文件下载pipeline
import os
import re

import scrapy
from scrapy.exceptions import DropItem

from NVDSpider.items import FileItem
from scrapy.pipelines.files import FilesPipeline
from NVDSpider.settings import FILES_STORE


class FilePipeline(FilesPipeline):

    def get_media_requests(self, item, info):
        for file_url in item['file_urls']:
            yield scrapy.Request(file_url)
        # if isinstance(item, FileItem):
        #     for file_url in item['file_urls']:
        #         yield scrapy.Request(file_url)

    def file_path(self, request, response=None, info=None):
        file_name = request.url.split('/')[-1]
        # return 'full/%s' % file_name
        return file_name

    def item_completed(self, results, item, info):
        file_paths = [x['path'] for ok, x in results if ok]
        if not file_paths:
            raise DropItem("没有文件")
        return item
