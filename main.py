import certifi
import json
import time
import math
import random
import os
import requests
# import tkinter as tk


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
        verify=certifi.where(),
        proxies=proxies
    )
    return json.loads(r.data.decode('utf-8'))


def search_user_vedio_list(search_user):
    sec_user_id = search_user['data'][0]['user_list'][0]['user_info']['sec_uid']
    # aweme_count=search_user['data'][0]['user_list'][0]['user_info']['aweme_count']
    vedio_list = []

    max_cursor = 0
    while(True):
        # for i in range(2):
        ticks = time.time()
        new_ticks = str(ticks).replace('.', '')
        ts = new_ticks[0:10]
        rticket = new_ticks[0:13]

        url = 'https://api-hl.amemv.com/aweme/v1/aweme/post/?max_cursor=' + \
            str(max_cursor)+'&sec_user_id='+sec_user_id+'&count=10&retry_type=no_retry&iid=80593983692&device_id=58231544547&ac=wifi&channel=huawei&aid=1128&app_name=aweme&version_code=730&version_name=7.3.0&device_platform=android&ssmix=a&device_type=HWI-AL00&device_brand=HUAWEI&language=zh&os_api=26&os_version=8.0.0&openudid=dd9979d88efc3c7e&manifest_version_code=730&resolution=1080*2160&dpi=408&update_version_code=7302&_rticket='+rticket+'&app_type=normal&js_sdk_version=1.19.2.0&mcc_mnc=46003&ts='+ts
        http = urllib3.PoolManager(
            cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        r = http.request('GET', url)
        r = r.data
        r = json.loads(r)
        max_cursor = r['max_cursor']
        for j in range(len(r['aweme_list'])):
            try:
                download_url = r['aweme_list'][j]['video']['bit_rate'][0]['play_addr']['url_list'][0]
                vedio_list.append(download_url)
            except:
                pass
        time.sleep(3)

        print(max_cursor)
        print(r['has_more'])
        if not int(r['has_more']):
            break
    # 去重
    vedio_list_alone = list(set(vedio_list))
    # 文件写入
    f = open('download_url.txt', 'a')
    for i in range(len(vedio_list_alone)):
        f.write(vedio_list_alone[i])
        f.write('\n')
    f.close()
    return vedio_list_alone


def download_vedio(vedio_list, folder):
    for i in range(len(vedio_list)):
        url = vedio_list[i]
        http = urllib3.PoolManager(
            cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        r = http.request('GET', url)
        data = r.data

        if os.path.exists(folder):
            pass
        else:
            os.mkdir(folder)

        f = open(folder+'/'+folder+'-'+str(i)+'.mp4', 'wb')
        f.write(data)
        f.close()
        time.sleep(5)


def input_user_name(user_name):
    search_user = search_user_sec_user_id(user_name)
    # 'zh19980123'
    vedio_list = search_user_vedio_list(search_user)
    download_vedio(vedio_list, user_name)


if __name__ == "__main__":

    input_user_name('051YP')


# # top = tk.Tk()

# # inputer = tk.Entry(top)  # 用于输入(只能一行文本，如果要多行使用Text组件)

# def task():
#     # 点击按钮后要执行的操作
#     text = inputer.get()
#     print(text)
#     search_user=search_user_sec_user_id(text)
#     #'zh19980123'
#     vedio_list=search_user_vedio_list(search_user)
#     download_vedio(vedio_list)
#     print(vedio_list)


# bt = tk.Button(top, text="Download", command=task)  # 按钮

# inputer.pack()   # 将小部件放置到主窗口中
# bt.pack()    # 将小部件放置到主窗口中

# top.mainloop()   # 进入消息循环
