# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaiduCatItem(scrapy.Item):
    title = scrapy.Field()
    image_url = scrapy.Field()
    width = scrapy.Field()
    height = scrapy.Field()
    image_name = scrapy.Field()
