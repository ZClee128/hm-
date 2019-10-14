# -*- coding: utf-8 -*-
import scrapy
import json
from hanman.items import HanmanItem
from hanman.items import PdfItem
class HmSpider(scrapy.Spider):
    name = 'hm'
    # allowed_domains = ['http://duolihm.com']
    baseUrl = 'http://duolihm.com'
    start_urls = [baseUrl]
# 所有章节
# //ul[@id = 'chapterList']/li[@class = 'item']/a/@href
# 每本书的连接
# //ul[@class= 'comic-list horizontal']/li[@class = 'item']/a[@class = 'thumbnail']/@href
# 每本书的名字
# //ul[@class= 'comic-list horizontal']/li[@class = 'item']/a[@class = 'thumbnail']/img/@alt
    def parse(self, response):
        link = response.xpath(
            "//ul[@class= 'comic-list horizontal']/li[@class = 'item']/a[@class = 'thumbnail']/@href")
        name = response.xpath(
            "//ul[@class= 'comic-list horizontal']/li[@class = 'item']/a[@class = 'thumbnail']/@title")
        for a in link:
            item = HanmanItem()
            item["imageLink"] = a.extract()
            for b in name:
                item["name"] = b.extract().encode("utf-8")
            url = self.baseUrl + a.extract()
            yield scrapy.Request(url, callback=self.myparse, dont_filter=True)

    def myparse(self, response):
        link = response.xpath(
            "//ul[@id = 'chapterList']/li[@class = 'item']/a/@href")
        for a in link:
            url = self.baseUrl + a.extract()
            yield scrapy.Request(url, callback=self.downloging, dont_filter=True)

    def downloging(self, response):
        link = response.xpath("//div[@class='comicpage']/img[@class='lazyload']/@src")
        for a in link:
            item = PdfItem()
            item["pdf"] = a.extract()
            yield item