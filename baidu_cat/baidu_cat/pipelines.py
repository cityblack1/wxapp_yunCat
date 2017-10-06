# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from cat_images.models import CatImage

class BaiduCatPipeline(object):
    def process_item(self, item, spider):
        instance = CatImage()
        instance.title = item['title']
        instance.image_url = item['image_url']
        instance.height = item['height']
        instance.width = item['width']
        instance.save(image_name=item['image_name'])
        save_title(item['title'])
        return item
