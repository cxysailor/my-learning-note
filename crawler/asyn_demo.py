#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : asyn_demo.py
#   Last Modified : 2020-08-22 17:59
#   Describe      : 
#
# ====================================================
import requests

headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36v'
        }
urls = [
        "http://downsc.chinaz.net/Files/DownLoad/jianli/202008/jianli13381.rar",
        "http://downsc.chinaz.net/Files/DownLoad/jianli/202008/jianli13387.rar",
        "http://downsc.chinaz.net/Files/DownLoad/jianli/202008/jianli13380.rar"
        ]


def get_content(url):
    print('正在爬取...', url)
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        return response.content


def parse_content(content):
    print('响应数据的长度为: ', len(content))
    

if __name__ == "__main__":
    for url in urls:
        content = get_content(url)
        parse_content(content)
