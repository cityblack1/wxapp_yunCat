import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yun_cat.settings")
django.setup()
from cat_images.models import CatImage


all_pic = CatImage.objects.all()
for i in all_pic:
    try:
        i.zip_images()
        print('meicuo')
    except Exception as e:
        print(e)

        print('出现错误')
        print(i.image)
        continue