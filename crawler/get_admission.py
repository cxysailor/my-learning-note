#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : get_admission.py
#   Last Modified : 2020-08-27 14:09
#   Describe      : 
#
# ====================================================
import os
import requests
from lxml import etree


url = 'https://www.ynzs.cn/html/content/4068.html'
headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
        }
if not os.path.exists('./pdf_file'):
    os.mkdir('./pdf_file')

a_tag_lists = []
response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
page_text = response.text

tree = etree.HTML(page_text)
a_tag_list = tree.xpath('//div[@class="wap-read"]//a')
for a_tag in a_tag_list:
    pdf_url = a_tag.xpath('./@href')[0]
    pdf_name = a_tag.xpath('./@title')[0]
    print(pdf_name, 'Downloading...')
    pdf_data = requests.get(url=pdf_url, headers=headers).text
    f_path = './pdf_file/' + pdf_name
    with open(f_path, mode='w', encoding='utf-8') as fp:
        fp.write(pdf_data)
    print(pdf_name, 'Done!')
print('All done!')
