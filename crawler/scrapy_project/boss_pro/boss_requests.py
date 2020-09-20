#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : boss_requests.py
#   Last Modified : 2020-09-09 16:33
#   Describe      : 
#
# ====================================================
import time
import requests
from lxml import etree
from selenium import webdriver

url = 'https://www.zhipin.com/job_detail/?query=python&city=100010000&industry=&position='
headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    }
cookies = {
        'cookie': '__g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1599621998,1599626920,1599639328; lastCity=100010000; __c=1599639328; __l=l=%2Fwww.zhipin.com%2F&r=&g=&friend_source=0&friend_source=0; __a=99303340.1599621998.1599626920.1599639328.19.3.3.19; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1599639360; __zp_stoken__=e622bPGtWXm1MYmlKZn5qRg8dYnA5QmpNTnocTmgFaz1KeF4wPRd2bkBdCCB8ZmQFJl0lJCl0cxNfPXgdBW9ua0xCCAkldjggVSE3bC9xSUQeCC4cGzFBD3o9cR1bSAM5IAxYQm19IGx8QDB%2BDQ%3D%3D'
        }
response = requests.get(url=url, headers=headers, cookies=cookies).text
#  session = requests.Session()
#  response = session.post(url=url, headers=headers)
#  page_text = session.get(url=url, headers=headers).text
print(response)
tree = etree.HTML(response)
a_list = tree.xpath('//*[@id="main"]/div/div[2]/ul/li[1]/div/div[1]/div[1]/div/div[1]/span[1]/a')
print(a_list)
for a_tag in a_list:
    print(a_tag)
    job_name = a_tag.text
    print(job_name)
#  driver = webdriver.Chrome()
#  response = driver.get(url=url)
#  time.sleep(50)
#  print(response)
