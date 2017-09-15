import sys,os
from scrapy.cmdline import execute


sys.path.append(os.path.join(os.path.join(__file__)))
execute(['scrapy','crawl','jd'])