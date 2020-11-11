#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C) 2020 cxysailor-master All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : bd_film.py
#   Last Modified : 2020-11-09 19:05
#   Describe      : 
#
# ====================================================
import time
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}
url = 'https://www.bd-film.cc/jd/15087.htm'
response = requests.get(url=url, headers=headers).text
#  print(response)
text = etree.HTML(response)
movie_url = text.xpath('//*[@id="downlist"]/div/div[3]/a/@href')
#  print(movie_url)
movie = requests.get(movie_url, headers=headers).content
time.sleep(0.5)
print(movie)
