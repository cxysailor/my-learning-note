# 异步爬虫

## 1. 先看一段代码的执行

```python
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


# 这个函数会阻塞，要等待它执行完成才能继续向下执行其他代码
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

```
执行代码的输出：

```python
# 正在爬取... http://downsc.chinaz.net/Files/DownLoad/jianli/202008/jianli13381.rar
程序执行到这里会阻塞，直到这一步执行完毕，才会继续向下执行
# 响应数据的长度为:  378667
# 正在爬取... http://downsc.chinaz.net/Files/DownLoad/jianli/202008/jianli13387.rar
程序执行到这里会阻塞，直到这一步执行完毕，才会继续向下执行
# 响应数据的长度为:  390241
# 正在爬取... http://downsc.chinaz.net/Files/DownLoad/jianli/202008/jianli13380.rar
程序执行到这里会阻塞，直到这一步执行完毕，才会继续向下执行
# 响应数据的长度为:  352406                            
#                                    
# [Process exited 0]             

```
这是一个单线程串行的执行流程，每次调用get_content()函数，都要等待它执行完成，获取了数据后，

才会执行下面其它的代码。如果url比较多时，这个等待时间就会很长，造成程序的效率比较低。

这就相当于在一条线上排队执行，前面的执行完了，才能开始下一个的执行。

## 2. 异步

为解决上述问题，可以使用异步的方式执行程序。

异步的实现方式：

1. 多线程、多进程 - 由于有更好的解决方案，故不推荐使用
- 优点：为每一个阻塞的操作单独开启线程或进程，阻塞操作就会异步执行
- 缺点：多线程或多进程无法无限制地开启；开启过多的线程或进程会耗费资源、影响效率
2. 线程池、进程池 - 适当使用
- 优点：可以降低系统对线程或进程创建和销毁的频率，从而降低对系统的开销
- 缺点：池中的线程或进程数量是有上限的，当阻塞的操作数超过池的上限时，还是会影响效率
- 使用原则：将阻塞且耗时的操作使用进程池、线程池处理
3. 单线程 + 异步协程 - 推荐使用这种方式
- event_loop:事件循环，相当于一个无限循环。可以把一些函数注册到这个事件循环上，当满足某些条件时，函数就会循环执行
- coroutine:协程对象，可以将协程对象注册到事件循环，它会被事件循环调用
- async:关键字，用于定义一个协程。使用async关键字定义一个方法，这个方法在调用时不会被立即执行，而是返回一个协程对象
- task：任务，是会协程对象的进一步封装，包含来任务的各个状态
- future:代表将来执行或还没有执行的任务，实际上与task没有本质的区别
- await:用来挂起阻塞方法的执行

## 3. 进程池的效率

这个是一段单线程串行执行的代码

```python
 1 import time
 2 
 3 name_list = [
 4         'Jacky',
 5         'Tom Hanks',
 6         'Angelina Julie'
 7         ]
 8 
 9 
10 def get_page(string):
11     print('正在下载..', string)
12     time.sleep(2)  # 模拟程序阻塞
13     print('下载成功:', string)
14 
15 
16 if __name__ == "__main__":
17     start_time = time.time()
18     for i in range(len(name_list)):
19         get_page(name_list[i])
20     end_time = time.time()
21     print(f'用时:{start_time - end_time}秒!')
```
执行结果如下

```python
0 正在下载.. Jacky                                                                                                                                        
1 下载成功: Jacky
2 正在下载.. Tom Hanks
3 下载成功: Tom Hanks
4 正在下载.. Angelina Julie
5 下载成功: Angelina Julie       
6 用时:-6.021696090698242秒!
7                                
8 [Process exited 0]
```

使用了进程池的代码执行

```python
 1 import time                                                                            
 2 from multiprocessing.dummy import Pool                                                 
 3                                                                                        
 4 name_list = [
 5         'Jacky',                                                                       
 6         'Tom Hanks',                                                                   
 7         'Angelina Julie'                                                               
 8         ]
 9 
10                                                                                        
11 def get_page(string):                                                                  
12     print('正在下载..', string)                                                        
13     time.sleep(2)                                                                      
14     print('下载成功:', string)                                                         
15                                                                                        
16                                                                                                      
17 if __name__ == "__main__":                                                                           
18     start_time = time.time()                                                                               
19     #  for i in range(len(name_list)):                                                                     
20     #      get_page(name_list[i])                                                                          
21     # 创建一个包含3个进程的进程池
22     pool = Pool(3)
23     # 将列表中的每一个元素传给get_page()执行
24     pool.map(get_page, name_list)
25     end_time = time.time()                                                                      
26     print(f'用时:{start_time - end_time}秒!') 
```

执行结果如下

```python
0 正在下载.. Jacky                                                                                                           
1 正在下载.. Tom Hanks                                                                   
2 正在下载.. Angelina Julie                                                              
3 下载成功: Jacky                                                                        
4 下载成功: Angelina Julie                                                               
5 下载成功: Tom Hanks                                                                    
6 用时:-2.07009220123291秒!                                                              
7                                                                                                      
8 [Process exited 0]  
```
**可以看到，使用进程池后执行时间是没有使用进程池的三分之一** 

## 4. 进程池的应用示例

爬取梨视频上生活板块的视频数据

知识点：
- 进程池应用中发送阻塞且耗时比较多大操作上
- 页面分析时，视频的真实url不是通过页面源代码加载的，而是在一段js代码内

```html
<script type="text/javascript">
var contId="1693011",liveStatusUrl="liveStatus.jsp",liveSta="",playSta="1",autoPlay=!1,isLiving=!1,isVrVideo=!1,hdflvUrl="",sdflvUrl="",hdUrl="",sdUrl="",ldUrl="",srcUrl="https://video.pearvideo.com/mp4/adshort/20200821/cont-1693011-15029820-104803_adpkg-ad_hd.mp4",vdoUrl=srcUrl,skinRes="//www.pearvideo.com/domain/skin",videoCDN="//video.pearvideo.com";
var player;
function newPrismplayer(_sourceId,_source,_isLive,_autoplay){
    var $hornId = $("#"+_sourceId);
此处省略    
</script>
```
可以看到真实的url在一段JavaScript代码中，使用xpath或BeautifulSoup4都无法解析出来，只能使用正则表达式来解析获取

pattern = 'srcUrl"(.*?)",vdoUrl'

以下是具体的实现代码

```python
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
#   Describe      :
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

```

执行结果如下

```python
0 你也想去故宫修文物吗？单霁翔院长告诉你这些事情.mp4 Downloading...                                                                          
1 日本新冠患者累计破6万：连续14天日增破千例，专家称到峰顶.mp4 Downloading...              
2 故宫博物院前院长单霁翔：中国人凭什么充满文化自信？.mp4 Downloading...                   
3 老美清华毕业不回国，10年赖在中国民间学厨.mp4 Downloading...                             
4 老美清华毕业不回国，10年赖在中国民间学厨.mp4 Completed!                                 
5 日本新冠患者累计破6万：连续14天日增破千例，专家称到峰顶.mp4 Completed!                  
6 你也想去故宫修文物吗？单霁翔院长告诉你这些事情.mp4 Completed!                           
7 故宫博物院前院长单霁翔：中国人凭什么充满文化自信？.mp4 Completed!                       
8                                                                                         
9 [Process exited 0]                                                                      
10                   
```
将保存和下载分开写成两个函数

```python
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
#   Describe      : Release 3.0
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

    def download_data(self, video_data):
        """下载数据 - 阻塞并耗时的操作，加进进程池"""
        name = video_data['name']
        url = video_data['url']
        print('Downloading...', name)
        video_content = requests.get(url=url, headers=self.headers).content
        self.save_data(name, video_content)
        time.sleep(2)
        print('Completed: ', name)

    def save_data(self, name, data):
        """保存数据"""
        file_path = './videos/' + name
        with open(file_path, mode='wb') as fp:
            fp.write(data)


if __name__ == "__main__":
    # 创建文件保存路径
    if not os.path.exists('./videos'):
        os.mkdir('./videos')
    glv = GetLiVideo()
    # 实例化进程池 - 包含4个进程
    pool = Pool(4)
    v_information = glv.get_each_video_url()
    pool.map(glv.download_data, v_information)  # pool.man()返回一个列表
    pool.close()  # 关闭pool，使其不再接受新的任务
    #  pool.terminate()  # 结束工作进程，不再处理未完成的任务
    pool.join()  # 主进程阻塞，等待子进程退出
    pool.join()

```

