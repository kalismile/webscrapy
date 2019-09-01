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
        'https': 'http://192.168.124.9:8888',
        'http': 'http://192.168.124.9:8888',
    }
    headers = {
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.10.0.1',
        'sdk-version': '1',
        'X-SS-STUB': 'B4652F5852D19A8ECDC4853D0263EEDB',
        'X-SS-REQ-TICKET': '1567349133929',
        'X-Gorgon': '0300000040014caa6ed1c213b59d6d8f8b56f701e76fdb0455ad',
        'X-Khronos': '1567349133'


    }
    cookies = {
        'odin_tt' : '1c6cd036ccdb7cae02f73e9d64df9e1d5ee96e5cbf4c1308c07af180ddb3b3be195d31dff7bd635ce7989e52900ab996e64795c637d2c73acd97d729e506a873',
        'qh[360]':'1',
        'install_id' : '84609604981',
        'ttreq' : '1$2eab338ad50bd6b83f8b6323dc3f8b49a6007f3a'

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
        'keyword': '051YP',
        'offset': '0',
        'count': '10',
        'is_pull_refresh': '0',
        'search_source': 'normal_search',
        'hot_search': '0',
        'latitude': '39.916295',
        'longitude': '116.410344',
        'search_id': '',
        'query_correct_type': '1',

    }

    r = requests.post(
        'https://aweme-hl.snssdk.com/aweme/v1/general/search/single/?',
        headers=headers,
        cookies=cookies,
        params=params,
        data=data,
        verify='/home/kali/Desktop/DO_NOT_TRUST_FiddlerRoot.crt',
        proxies=proxies
    )
    data = {

    }

    return r.text


if __name__ == "__main__":
    print(search_user_sec_user_id('051YP'))
