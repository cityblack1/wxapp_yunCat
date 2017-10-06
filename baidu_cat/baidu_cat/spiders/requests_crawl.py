import requests
import re
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yun_cat.settings")
django.setup()
import time
from cat_images.models import CatImage
from django.core.files.base import ContentFile


set_record = set()

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    }

def parse_url(url):
    mapping_dict = {'2': 'g', 'o': 'w', 'g': 'n', 'a': '0', 'j': 'e', 'r': 'p', 'v': 'c', 'q': 'q', '1': 'd', 'k': 'b', '8': '1', '3': 'j', 'd': '2', '5': 'o', 's': 'l', 'u': 'f', 'c': '5', 'b': '8', 'm': '6', 'h': 'k', 'e': 'v', 'l': '9', '9': '4', 't': 'i', 'i': 'h', 'p': 't', '0': '7', '7': 'u', 'f': 's', '4': 'm', 'w': 'a', '6': 'r', 'n': '3'}
    url = url.replace("_z2C$q", ":").replace("AzdH3F", "/").replace("_z&e3B", ".")[4:]
    url = 'http' + ''.join([mapping_dict.get(i, i) for i in url])
    return url

for i in range(0, 1000, 30):
    time.sleep(0.2)
    time_stamp = str(time.time())
    time_stamp.replace('.', '')
    while len(time_stamp) < 13:
        time_stamp += '0'
    while len(time_stamp) > 13:
        time_stamp = time_stamp[:-2]
    url1 = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=萌猫&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=萌猫&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn={i}&rn=30&gsm={time}'.format(i=i, time=time_stamp)

    try:
        session = requests.session()
        html = session.get(url1, headers=headers, timeout=3).content.decode('utf-8')
        image_url = [parse_url(url) for url in re.findall('objURL":"(.*?)"', html)]
        title = re.findall('"fromPageTitleEnc":"(.*?)"', html)
        width = re.findall('"width":(\d+)', html)
        height = re.findall('"height":(\d+)', html)
        suf_type = re.findall('"type":"(.*?)"', html)
        items = zip(image_url, title, width, height, suf_type)
    except:
        print('跳过本次根目录下载')
        continue

    for item in items:
        try:
            if item[0] in set_record:
                print('已经缓存')
                continue
            image_url = item[0]
            title = item[1]
            width = item[2]
            height = item[3]
            image_name = item[1] + '.' + item[4]

            instance = CatImage()
            instance.title = title
            instance.width = width
            instance.height = height
            instance.image_url = image_url

            content = session.get(image_url, headers=headers, timeout=3).content
            instance.save_image(image_name, content)
            print('储存成功', image_name)
            set_record.add(image_url)
        except:
            print("出错, 跳过本次下载")
            continue
