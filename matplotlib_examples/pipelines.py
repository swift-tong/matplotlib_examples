# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.files import FilesPipeline
from urllib.parse import urlparse
from os.path import join,dirname,basename

class MatplotlibExamplesPipeline(object):
    def process_item(self, item, spider):
        return item


class MyPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        print('urlparse(request.url)=',urlparse(request.url))
        path = urlparse(request.url).path
        print('path=',path)
        return join(basename(dirname(path)), basename(path))