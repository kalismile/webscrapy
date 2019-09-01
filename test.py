import certifi
import json
import time
import math
import random
import os
import requests


def search_user_sec_user_id(user_name):

    ticks = time.time()
    new_ticks = str(ticks).replace('.', '')
    proxies = {
        'https':'http://192.168.124.9:8888',
        'http':'http://192.168.124.9:8888',
    }
    params = {
        'os_api': '22',
        'device_type': 'm2',
        'ssmix': 'a',
        'manifest_version_code': '720',
        'dpi': '240',
        'js_sdk_version': '1.19.4.16',
        'uuid': '865166026335151',
        'app_name': 'aweme',
        'version_name': '7.2.0',
        'ts': str(new_ticks[0:10]),
        'app_type': 'normal',
        'ac': 'wifi',
        'update_version_code': '7202',
        'channel': 'aweGW',
        '_rticket': str(new_ticks[0:13]),
        'device_platform': 'android',
        'iid': '84609604981',
        'version_code': '720',
        'openudid': '926bb1e95c3d4e10',
        'device_id': '66662367106',
        'resolution': '1080*1920',
        'os_version': '5.1.1',
        'language': 'zh',
        'device_brand': 'meizu',
        'aid': '1128',
        'mcc_mnc': '46000',
    }
    data = {
        #  body
        'cursor': '0',
        'keyword': '051YP',
        'count': '10',
        'type': '1',
        'is_pull_refresh': '0',
        'hot_search': '0',
        'search_source': '',
        'search_id': '',
        'query_correct_type': '1',
    }

    r = requests.post(
        'https://aweme-hl.snssdk.com/aweme/v1/general/search/single/?',
        params=params,
        data=data,
        verify='/home/kali/Desktop/DO_NOT_TRUST_FiddlerRoot.crt',
        proxies=proxies
    )
    data={

    }

    return r.text
if __name__ == "__main__":
    print(search_user_sec_user_id('051YP'))
