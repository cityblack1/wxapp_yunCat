from scrapy.cmdline import execute

import sys
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yun_cat.settings")
django.setup()

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "json_cat"])