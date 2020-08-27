#!/usr/bin/env python4
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : asyn_get_video.py
#   Last Modified : 2020-08-22 20:18
#   Describe      : Release 1.0
#
# ====================================================
import os
import re
import time
from multiprocessing.dummy import Pool
import requests
from lxml import etree


class GetLiVideo():
    """获取梨视频上生活板块的热门视频"""
    def __init__(self):
        super(GetLiVideo, self).__init__()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
        }
        self.url = 'https://www.pearvideo.com/category_5'
        self.video_info = []  # 保存视频的url与名称

    def get_each_video_url(self):
        """获取视频的真实url及其名称"""
        # 对生活板块首页发起请求
        page_text = requests.get(url=self.url, headers=self.headers).text
        tree = etree.HTML(page_text)
        li_list = tree.xpath('//ul[@id="listvideoListUl"]/li')
        for li_tag in li_list:
            # 视频详情页url
            detail_url = 'https://www.pearvideo.com/' + li_tag.xpath('./div/a/@href')[0]
            # 视频名称
            video_name = li_tag.xpath('./div/a//div[@class="vervideo-title"]/text()')[0] + '.mp4'
            # 爬取视频详情页url获取其真实的url供下载
            video_url_page = requests.get(url=detail_url, headers=self.headers).text
            # 使用正则解析 - 因为真实url在js代码中，xpath和bs4都无法解析
            pattern = 'srcUrl="(.*?)",vdoUrl'
            video_url = re.findall(pattern, video_url_page)[0]
            video_dict = {
                'url': video_url,
                'name': video_name
            }
            self.video_info.append(video_dict)
        return self.video_info

    def download_save_data(self, video_information):
        """下载并保存数据 - 阻塞并耗时的操作，加进进程池"""
        url = video_information['url']
        name = video_information['name']
        print(name, 'Downloading...')
        video_data = requests.get(url=url, headers=self.headers).content
        file_path = './videos/' + name
        with open(file_path, mode='wb') as fp:
            fp.write(video_data)
        print(name, 'Completed!')
        time.sleep(2)


if __name__ == "__main__":
    # 创建文件保存路径
    if not os.path.exists('./videos'):
        os.mkdir('./videos')
    glv = GetLiVideo()
    # 实例化进程池 - 包含4个进程
    pool = Pool(4)
    v_information = glv.get_each_video_url()
    pool.map(glv.download_save_data, v_information)
    pool.close()  # 关闭pool，使其不再接受新的任务
    #  pool.terminate()  # 结束工作进程，不再处理未完成的任务
    pool.join()  # 主进程阻塞，等待子进程退出
    pool.join()
