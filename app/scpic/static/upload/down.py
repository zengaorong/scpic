#coding=utf-8
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from bs4 import BeautifulSoup

headers = {'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
           'Accept-Language': 'zh-CN,zh;q=0.9',
           'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36',
           'Connection': 'keep-alive',
           'Referer': 'http://www.baidu.com/'
           }

# serch_url = "https://nhentai.net/search/?q=%E6%AC%B2%E6%9C%9B%E5%9B%9E%E5%B8%B0%E7%AC%AC554%E7%AB%"
#
# respons = requests.get(serch_url)
# print respons.text

# for key in range(1,10):
#     url = "https://i.nhentai.net/galleries/1224608/%s.jpg"%key
#     ir = requests.get(url,timeout=10)
#     open(r'1224608_%s.jpg'%key , 'wb').write(ir.content)


# url = "https://nhentai.net/g/233153/"
# respons = requests.get(url)
# respons.encoding='utf-8'
# print respons.text
# with open("233.html","wb") as f:
#     f.writelines(respons.text)

# later_url = "https://nhentai.net/tag/yaoi/?page=2"

# soup = BeautifulSoup(open("233.html"),"html.parser")
# div_list = soup.find_all("div" ,{'class':'thumb-container'})
#
# name = soup.find('meta',{'itemprop':'name'})['content']
# id = soup.find('img',{'class':'lazyload'})['data-src'].split('/')[-2]
# print name
# print id
# id = div_list[0]
# print len(div_list)

# for key in range(1,len(div_list)+1):
#     url = "https://i.nhentai.net/galleries/1224608/%s.jpg"%key
#     ir = requests.get(url,timeout=10)
#     open(r'1224608_%s.jpg'%key , 'wb').write(ir.content)

#252336,233153
# 107041,170116

#
down_ids = [237530,116175,58311,199025,199027,127317,67326,258492,242957,257953,39980]
# down_ids = [259598]
res_session = requests.session()
def down_pics(down_ids):
    for key in down_ids:
        url = "https://nhentai.net/g/%s/"%key
        respons = res_session.get(url)
        soup = BeautifulSoup(respons.text,"html.parser")
        div_list = soup.find_all("div" ,{'class':'thumb-container'})
        name = soup.find('meta',{'itemprop':'name'})['content']
        name = validateTitle(name)
        nums = len(div_list)
        # id = soup.find('img',{'class':'lazyload'})['data-src'].split('/')[-2]



        for num in range(1,nums+1):
            url = "https://nhentai.net/g/%s/%s/"%(key,num)
            first_page_respon = res_session.get(url)
            soup = BeautifulSoup(first_page_respon.text,'html.parser')
            image = soup.find('img',{'class':'fit-horizontal'})
            id = image['src'].split('/')[-2]
            type = image['src'].split('/')[-1].split('.')[-1]


            # url = "https://i.nhentai.net/galleries/%s/%s.jpg"%(id,num)
            url = "https://i.nhentai.net/galleries/%s/%s.%s"%(id,num,type)
            print url
            ir = res_session.get(url)
            mkdir(name)
            open(r'%s/%s.jpg'%(name,num) , 'wb').write(ir.content)

import re
def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title

import os
def mkdir(path):

    # 判断路径是否存在
    # 存在     True
    # 不存在   False

    isExists=os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        #print path+' 创建成功'
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        #print path+' 目录已存在'
        return False

down_pics(down_ids)