import scrapy
import re

from scrapy import Request
from ..items import BaiduCatItem
from cat_images.models import CatImage

import time

import pickle

headers = {
    "Accept":"text/plain, */*; q=0.01",
    "Accept-Encoding":"gzip, deflate, sdch",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Connection":"keep-alive",
    "Host":"image.baidu.com",
    "Referer":"http://image.baidu.com/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs9&word=%E8%90%8C%E5%AE%A0%E5%9B%BE%E7%89%87&oriquery=%E5%9B%BE%E7%89%87&ofr=%E5%9B%BE%E7%89%87&sensitive=0",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    "X-Requested-With":"XMLHttpRequest"
    }

try:
    with open('record.txt', 'rb') as f:
        record = pickle.load(f)
except:
    with open('record.txt', 'wb') as f:
        pickle.dump(set(), f, True)
    with open('record.txt', 'rb') as f:
        record = pickle.load(f)


def parse_url(url):
    mapping_dict = {'2': 'g', 'o': 'w', 'g': 'n', 'a': '0', 'j': 'e', 'r': 'p', 'v': 'c', 'q': 'q', '1': 'd', 'k': 'b', '8': '1', '3': 'j', 'd': '2', '5': 'o', 's': 'l', 'u': 'f', 'c': '5', 'b': '8', 'm': '6', 'h': 'k', 'e': 'v', 'l': '9', '9': '4', 't': 'i', 'i': 'h', 'p': 't', '0': '7', '7': 'u', 'f': 's', '4': 'm', 'w': 'a', '6': 'r', 'n': '3'}
    url = url.replace("_z2C$q", ":").replace("AzdH3F", "/").replace("_z&e3B", ".")[4:]
    url = 'http' + ''.join([mapping_dict.get(i, i) for i in url])
    return url


class JsonCatSpider(scrapy.Spider):
    name = 'json_cat'
    allowed_domains = ['image.baidu.com/search/acjson']
    start_urls = ['http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1506541957215_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E8%90%8C%E5%AE%A0%E5%9B%BE%E7%89%87%E5%B0%8F%E7%8C%AB&f=3&oq=%E8%90%8C%E5%AE%A0%E5%9B%BE%E7%89%87&rsp=2']

    def parse(self, response):
        for i in range(0, 5000, 30):
            time.sleep(0.2)
            time_stamp = str(time.time())
            time_stamp.replace('.', '')
            while len(time_stamp) < 13:
                time_stamp += '0'
            while len(time_stamp) > 13:
                time_stamp = time_stamp[:-2]

            yield Request('http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E8%90%8C%E5%AE%A0%E5%9B%BE%E7%89%87&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&word=%E8%90%8C%E5%AE%A0%E5%9B%BE%E7%89%87&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&pn={i}&rn=30&gsm={time}'.format(i=i, time=time_stamp), headers=headers, callback=self.parse_detail, meta={'cookiejar': 1}, dont_filter=True)

    def parse_detail(self, responce):
        html = responce.body.decode('utf-8')
        image_url = [parse_url(url) for url in re.findall('objURL":"(.*?)"', html)]
        title = re.findall('"fromPageTitleEnc":"(.*?)"', html)
        width = re.findall('"width":(\d+)', html)
        height = re.findall('"height":(\d+)', html)
        suf_type = re.findall('"type":"(.*?)"', html)
        items = zip(image_url, title, width, height, suf_type)

        for item in items:
            bd_item = BaiduCatItem()
            bd_item['image_url'] = item[0]
            bd_item['title'] = item[1]
            if bd_item['title'] in record:
                print('记录已经存在')
                continue
            bd_item['width'] = item[2]
            bd_item['height'] = item[3]
            bd_item['image_name'] = item[1] + '.' + item[4]
            yield Request(item[0], callback=self.save_data, meta=bd_item, dont_filter=True)

    def save_data(self, responce):
        if responce.status == 200:
            instance = CatImage()
            instance.title = responce.meta['title']
            instance.image_url = responce.meta['image_url']
            instance.height = responce.meta['height']
            instance.width = responce.meta['width']
            instance.save_image(image_name=responce.meta['image_name'], response=responce.body)
            with open('record.txt', 'wb') as f:
                record.add(responce.meta['title'])
                pickle.dump(record, f, True)
