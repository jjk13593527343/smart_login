# -*- encoding:utf-8 -*-
import hashlib
import base64
import requests
import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class Unity(object):
    @staticmethod
    def md5_(values):
        md5 = hashlib.md5()
        md5.update(values)
        return md5.hexdigest()

    @staticmethod
    def base64_en(values):
        return base64.b64encode(values)

    @staticmethod
    def base64_de(values):
        return base64.b64decode(values)

    @staticmethod
    def time(values):
        return '-'.join(re.findall('\d+', values))

    @staticmethod
    def Date_processing(values):
        pass

    @staticmethod
    def max_page(values):
        r = r'.*当前页:(\d+)/(\d+)'
        a, current, page_cout = re.findall('\d+', values)
        return current, page_cout

    @staticmethod
    def Punishment_doc(values):
        r = r'(\d+)'
        return re.findall(r,values)

    @staticmethod
    def date_edit(values):
        return '-'.join(re.findall('\d+',values))

    @staticmethod
    def Mosaic_url(values):
        return '-'.join(re.findall('\d+',values))

    @staticmethod
    def Punishment_doc(values):
        return ''.join(re.findall('\d+',values))

if __name__ == '__main__':
    pass

