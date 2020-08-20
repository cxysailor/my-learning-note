#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : bs_demo.py
#   Last Modified : 2020-08-17 21:23
#   Describe      :
#
# ====================================================
#  import lxml
from bs4 import BeautifulSoup as bs


if __name__ == "__main__":
    with open('./test.html', mode='r', encoding='utf-8') as fp:
        soup = bs(fp, 'lxml')
    #  print(soup.a)
    #  print(soup.find('div'))
    #  print(soup.find('div', class_='song'))
    #  print(soup.find_all('a'))
    #  print(soup.find_all('a', title='du'))
    #  print(soup.select('.tang'))
    #  print(soup.select('#df'))
    #  print(soup.select('b'))
    #  print(soup.select('.tang > ul > li > a')[0])
    #  print(soup.select('.tang > ul > li a')[0])
    #  print(soup.a.text)
    #  print(soup.select('.tang > ul > li a')[1].text)
    #  print(soup.select('.tang > ul > li a')[1].string)
    #  print(soup.select('#df > a')[0].string)
    #  print(soup.select('#df > a')[0].get_text())
    print(soup.select('.tang > ul > li > a')[1]['title'])
