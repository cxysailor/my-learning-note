#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : async.py
#   Last Modified : 2020-08-23 17:40
#   Describe      :
#
# ====================================================
import asyncio

async def request(url):
    """async关键字修饰的函数，被调用时不会立即执行，而是返回一个协程对象"""
    print('正在请求的url是:', url)
    print(f'{url}请求成功!')
    return url

def call_back_func(tsk):
    # result返回的就是任务对象中封装的协程对象对应函数的返回值 - 即request函数的返回值url
    print('我是回调函数，我被调用了！', tsk.result())


if __name__ == "__main__":
    # 调用request函数返回一个协程对象
    c = request('https://www.baidu.com')
    # 创建一个事件循环对象
    loop = asyncio.get_event_loop()
    # 将协程对象c注册到事件循环对象loop中并启动loop
    #  loop.run_until_complete(c)

    # task的使用
    # 基于loop创建一个task对象
    #  tsk = loop.create_task(c)
    #  print(tsk)  # 查看task的状态
    # 将task注册到loop并启动
    #  loop.run_until_complete(tsk)
    #  print(tsk)  # 查看task的状态

    # future的使用
    #  fut = asyncio.ensure_future(c)
    #  print(fut)
    #  loop.run_until_complete(fut)
    #  print(fut)

    # 绑定回调函数
    fut = asyncio.ensure_future(c)
    # 将回调函数绑定到任务对象中
    fut.add_done_callback(call_back_func)
    loop.run_until_complete(fut)
