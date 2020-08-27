#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : asyn_coroutine.py
#   Last Modified : 2020-08-24 23:27
#   Describe      : 
#
# ====================================================
import time
import asyncio

urls = [
   'https://www.baidu.com',
   'https://www.sougou.com',
   'https://goubanjia.com'
]
stasks = []


async def request(url):
    print('Downloading...', url)
    # 在异步协程中如果出现来同步模块相关的代码
    # 则无法实现同步 - 即time.sleep(2)不会起到阻塞的作用
    #  time.sleep(2)
    # 在asyncio中遇到阻塞操作必须使用await关键字进行手动挂起
    await asyncio.sleep(2)
    print('Download completed!')


start = time.time()
for url in urls:
    c = request(url)
    # 创建一个协程任务
    tsk = asyncio.ensure_future(c)
    # 将协程任务添加到列表
    stasks.append(tsk)
# 创建事件循环
loop = asyncio.get_event_loop()
# 需要将任务封装到wait中，不能直接传入
loop.run_until_complete(asyncio.wait(stasks))
end = time.time()
print(f'Elapced {end - start} seconds!')
