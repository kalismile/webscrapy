from urllib.parse import quote
import urllib3
import certifi
import json
import time
import math 
import random
import os
# import tkinter as tk

    
def search_user_sec_user_id(keyword):
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
    keyword = quote(keyword, 'utf-8')
    ticks = time.time()
    new_ticks = str(ticks).replace('.', '')
    ts=new_ticks[0:10]
    rticket=new_ticks[0:13]
    device_id=random.random()
    device_id=math.ceil(device_id*100000000000)
    device_id=str(device_id)
    url='https://aweme-hl.snssdk.com/aweme/v1/general/search/single/?manifest_version_code=730&_rticket='+rticket+'&app_type=normal&iid=80593983692&channel=huawei&device_type=HWI-AL00&language=zh&resolution=1080*2160&openudid=dd9979d88efc3c7e&update_version_code=7302&os_api=26&dpi=408&ac=wifi&device_id='+device_id+'&mcc_mnc=46003&os_version=8.0.0&version_code=730&app_name=aweme&version_name=7.3.0&js_sdk_version=1.19.2.0&device_brand=HUAWEI&ssmix=a&device_platform=android&aid=1128&ts='+ts+'&keyword='+keyword+'&offset=0&count=10&is_pull_refresh=0&search_source=normal_search&hot_search=0&latitude=31.992811&longitude=112.120394&search_id=&query_correct_type=1'
    r=http.request('GET',url)
    return json.loads(r.data.decode('utf-8'))


def search_user_vedio_list(search_user):
    sec_user_id=search_user['data'][0]['user_list'][0]['user_info']['sec_uid']
    aweme_count=search_user['data'][0]['user_list'][0]['user_info']['aweme_count']
    vedio_list=[]
    for i in range(math.ceil(aweme_count/10)):
    # for i in range(2):
        ticks = time.time()
        new_ticks = str(ticks).replace('.', '')
        ts=new_ticks[0:10]
        rticket=new_ticks[0:13]
        max_cursor=new_ticks[0:14]
        device_id=random.random()
        device_id=math.ceil(device_id*100000000000)
        device_id=str(device_id)
        max_cursor=new_ticks[0:13]*2
        url='https://aweme-hl.snssdk.com/aweme/v1/aweme/post/?max_cursor='+max_cursor+'&sec_user_id='+sec_user_id+'&count=10&retry_type=no_retry&iid=80593983692&device_id='+device_id+'&ac=wifi&channel=huawei&aid=1128&app_name=aweme&version_code=730&version_name=7.3.0&device_platform=android&ssmix=a&device_type=HWI-AL00&device_brand=HUAWEI&language=zh&os_api=26&os_version=8.0.0&openudid=dd9979d88efc3c7e&manifest_version_code=730&resolution=1080*2160&dpi=408&update_version_code=7302&_rticket='+rticket+'&app_type=normal&js_sdk_version=1.19.2.0&mcc_mnc=46003&ts='+ts
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
        r=http.request('GET',url)
        r=r.data
        r=json.loads(r)
        for j in range(len(r['aweme_list'])):
            download_url=r['aweme_list'][j]['video']['play_addr']['url_list'][0]
            vedio_list.append(download_url)
        time.sleep(3)
    # 文件写入
    f=open('download_url.txt','a')
    for i in range(len(vedio_list)):
        f.write(vedio_list[i])
        f.write('\n')
    f.close()
    return vedio_list

def download_vedio(vedio_list,folder):
    for i in range(len(vedio_list)):
        url=vedio_list[i]
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
        r=http.request('GET',url)
        data=r.data

        if os.path.exists(folder):
            pass
        else:
            os.mkdir(folder)

        f=open(folder+'/'+folder+'-'+str(i)+'.mp4','wb')
        f.write(data)
        f.close()
        time.sleep(10)


def input_user_name(user_name):
    search_user=search_user_sec_user_id(user_name)
    #'zh19980123'
    vedio_list=search_user_vedio_list(search_user)
    download_vedio(vedio_list,user_name)

if __name__ == "__main__":
    # input_user_name('zh19980123')
    input_user_name('v1x18605023825')
    input_user_name('2157023904')
    input_user_name('908916488')
    input_user_name('9240977')
    input_user_name('MiLa520.')
    input_user_name('LANBOX888')
    input_user_name('1501052357')
    input_user_name('C520666888')   
    input_user_name('cswmwt')   
    input_user_name('2200930081')   




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
#first
#test git
#test again
#again and again





