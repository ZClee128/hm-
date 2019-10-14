# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline

class HanmanPipeline(object):
    def process_item(self, item, spider):
        # print('sdfsdf',item)
        return item


class HanmanImagePipeline(ImagesPipeline):
    def get_media_requests(self,item,info):
        imageLink = item['pdf']
        yield scrapy.Request(imageLink)

    # def process_item(self, item, spider):
    #     print("sdfsf",item)
    #     return item