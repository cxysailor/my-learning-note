# Scrapy框架

## 1. 简介

框架就是一个集成了很多功能，并且具有很强的通用性的项目模板.

Scrapy就是爬虫中封装好的一个框架

Scrapy框架封装的主要功能：
1. 高性能的持久化存储
2. 异步的数据下载
3. 高性能的数据解析
4. 分布式

## 2. 环境安装

**Mac OS 或者Linux系统** 

`pip install --user scrapy` 

**Windows系统** 

-  pip install --user wheel
-  下载twisted [twisted](https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted) 
-  安装twisted pip install Twisted‑20.3.0‑cp38‑cp38‑win_amd64.whl  # 下载windows平台的对应python版本的安装包
-  pip install --user pywin32
-  pip install --user scrapy

现在比较简单了，Windows系统下直接使用pip就可以安装妥了

在终端命令行输入scrapy，如果没有错误提示，则说明安装好了

## 3. 创建scrapy项目

scrapy项目需要2步
- 创建工程
- 创建一个爬虫程序

### 3.1 创建一个工程

创建一个目录，比如scrapy_project，进入这个目录，使用

`scrapy startproject project_name` 命令

```bash
❯ scrapy startproject first_blood
New Scrapy project 'first_blood', using template directory '/home/cxy/.local/lib/python3.8/site-packages/scrapy/templates/project', created in:
    /home/cxy/python_learning/crawler/scrapy_project/first_blood

You can start your first spider with:
    cd first_blood
    scrapy genspider example example.com
```
说明已经创建了名为first_blood的工程

同时，也提示了，进入first_blood目录，创建一个scrapy爬虫程序

先不忙着创建程序，先来看看生成了什么

这个目录下多了一个与工程同名的目录

```bash
❯ ls
first_blood

```

再看看这个目录下有什么

```bash
❯ cd first_blood
❯ ls -l
总用量 4
drwxr-xr-x 3 cxy cxy 117  9月  2 20:35 first_blood
-rw-r--r-- 1 cxy cxy 265  9月  2 20:35 scrapy.cfg
```
还有一个first_blood目录和一个scrapy.cfg文件

scrapy.cfg是一个配置文件

看一下这个first_blood目录有什么

```bash
❯ tree first_blood
first_blood
├── __init__.py
├── items.py
├── middlewares.py
├── pipelines.py
├── settings.py
└── spiders
    └── __init__.py

1 directory, 6 files

```

### 3.2 创建一个爬虫程序

进入一级first_blood目录，执行

`scrapy genspider [-t template] <name> <domain>` 

```bash
$ scrapy genspider -t crawl scrapyorg scrapy.org
Created spider 'scrapyorg' using template 'crawl'
```

```bash
$ scrapy genspider example example.com
Created spider 'example' using template 'basic'
```

```bash
❯ cd first_blood # 进入目录
❯ scrapy genspider first www.baidu.com # 创建爬虫程序first
Created spider 'first' using template 'basic' in module:
  first_blood.spiders.first

```

再看一下first_blood目录发生来什么

```bash
❯ tree first_blood
first_blood
├── __init__.py
├── items.py
├── middlewares.py
├── pipelines.py
├── __pycache__
│   ├── __init__.cpython-38.pyc
│   └── settings.cpython-38.pyc
├── settings.py
└── spiders
    ├── first.py # 这个就是生成的爬虫的源文件
    ├── __init__.py
    └── __pycache__
        └── __init__.cpython-38.pyc

3 directories, 10 files

```

## 4. 运行爬虫

在终端命令行输入

`scrapy crawl <spider>` 

## 5. 爬虫源文件first.py

```python
import scrapy


class FirstSpider(scrapy.Spider):
    # 爬虫文件的名称 - 爬虫源文件的唯一标识
    name = 'first'
    # 允许的域名 - 用来限定start_urls列表中那些url可以请求发送
    # 该域名下的所有的网页都会被请求；非其下的网页则不请求
    # 即仅请求百度下的网页，而不会请求搜狗的网页
    allowed_domains = ['www.baidu.com']
    # 起始url列表 - 其中的url会被scrapy自动的发送请求
    start_urls = ['http://www.baidu.com/', 'https://sougou.com']

    def parse(self, response):
        """用于数据解析
        response: 请求成功后对应的请求对象
        其请求对象的个数与start_urls中的url个数相对应
        要想获取所有的请求对象，就需要多次调用这个函数
        """
        print(response)

```

试着执行一次

```python
scrapy crawl first
```

发现并没有出现预期的结果

```bash
❯ scrapy crawl first
2020-09-04 00:31:37 [scrapy.utils.log] INFO: Scrapy 2.3.0 started (bot: first_blood)
2020-09-04 00:31:37 [scrapy.utils.log] INFO: Versions: lxml 4.5.2.0, libxml2 2.9.10, cssselect 1.1.0, parsel 1.6.0, w3lib 1.22.0, Twisted 20.3.0, Python 3.8.5 (default, Jul 27 2020, 08:42:51) - [GCC 10.1.0], pyOpenSSL 19.1.0 (OpenSSL 1.1.1g  21 Apr 2020), cryptography 3.1, Platform Linux-5.7.17-2-MANJARO-x86_64-with-glibc2.2.5
2020-09-04 00:31:37 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.epollreactor.EPollReactor
2020-09-04 00:31:37 [scrapy.crawler] INFO: Overridden settings:
{'BOT_NAME': 'first_blood',
 'EDITOR': '/usr/bin/nano',
 'NEWSPIDER_MODULE': 'first_blood.spiders',
 'ROBOTSTXT_OBEY': True,
 'SPIDER_MODULES': ['first_blood.spiders']}
2020-09-04 00:31:37 [scrapy.extensions.telnet] INFO: Telnet Password: aba474a865aa267e
2020-09-04 00:31:37 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.memusage.MemoryUsage',
 'scrapy.extensions.logstats.LogStats']
2020-09-04 00:31:37 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2020-09-04 00:31:37 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2020-09-04 00:31:37 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2020-09-04 00:31:37 [scrapy.core.engine] INFO: Spider opened
2020-09-04 00:31:37 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2020-09-04 00:31:37 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2020-09-04 00:31:37 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://www.baidu.com/robots.txt> (referer: None)
2020-09-04 00:31:37 [scrapy.downloadermiddlewares.robotstxt] DEBUG: Forbidden by robots.txt: <GET http://www.baidu.com/>
2020-09-04 00:31:37 [scrapy.core.engine] DEBUG: Crawled (509) <GET https://www.sougou.com/robots.txt> (referer: None)
2020-09-04 00:31:37 [scrapy.core.engine] DEBUG: Crawled (509) <GET https://www.sougou.com> (referer: None)
2020-09-04 00:31:37 [scrapy.spidermiddlewares.httperror] INFO: Ignoring response <509 https://www.sougou.com>: HTTP status code is not handled or not allowed
2020-09-04 00:31:37 [scrapy.core.engine] INFO: Closing spider (finished)
2020-09-04 00:31:37 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/exception_count': 1,
 'downloader/exception_type_count/scrapy.exceptions.IgnoreRequest': 1,
 'downloader/request_bytes': 661,
 'downloader/request_count': 3,
 'downloader/request_method_count/GET': 3,
 'downloader/response_bytes': 1314,
 'downloader/response_count': 3,
 'downloader/response_status_count/200': 1,
 'downloader/response_status_count/509': 2,
 'elapsed_time_seconds': 0.376861,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2020, 9, 3, 16, 31, 37, 705601),
 'httperror/response_ignored_count': 1,
 'httperror/response_ignored_status_count/509': 1,
 'log_count/DEBUG': 4,
 'log_count/INFO': 11,
 'memusage/max': 54308864,
 'memusage/startup': 54308864,
 'response_received_count': 3,
 'robotstxt/forbidden': 1,
 'robotstxt/request_count': 2,
 'robotstxt/response_count': 2,
 'robotstxt/response_status_count/200': 1,
 'robotstxt/response_status_count/509': 1,
 'scheduler/dequeued': 2,
 'scheduler/dequeued/memory': 2,
 'scheduler/enqueued': 2,
 'scheduler/enqueued/memory': 2,
 'start_time': datetime.datetime(2020, 9, 3, 16, 31, 37, 328740)}
2020-09-04 00:31:37 [scrapy.core.engine] INFO: Spider closed (finished)

```
原因就在这里

```bash
{'BOT_NAME': 'first_blood',
 'EDITOR': '/usr/bin/nano',
 'NEWSPIDER_MODULE': 'first_blood.spiders',
 'ROBOTSTXT_OBEY': True,  # 就是这里没有设置，导致来没有返回请求的结果
 'SPIDER_MODULES': ['first_blood.spiders']}

```

这个网站的robots协议，如果遵守这个协议，就会有很多数据请求不到

故目前先将其设置为False

在settings.py设置文件中，找到

`ROBOTSTXT_OBEY = True` 

将其改为False

`ROBOTSTXT_OBEY = False` 

再次执行，就可以获取请求的结果了

```bash
2020-09-04 00:48:30 [scrapy.core.engine] INFO: Spider opened
2020-09-04 00:48:30 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2020-09-04 00:48:30 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2020-09-04 00:48:30 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://www.baidu.com/> (referer: None)
<200 http://www.baidu.com/>
2020-09-04 00:48:30 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.sogou.com> (referer: None)
<200 https://www.sogou.com>
2020-09-04 00:48:31 [scrapy.core.engine] INFO: Closing spider (finished)

```

若不想看到这些日志信息，可以在执行的时候加上--nolog参数

```bash
❯ scrapy crawl first --nolog
<200 http://www.baidu.com/>
<200 https://www.sogou.com>

```

这样就只有自己编写的代码的输出了

但是这样做法，就会忽略所有的提示信息，即使程序代码出错也不会提示，给代码调试带来不便

所以还是应该设置log提示的级别，在settings.py文件中，写入

`LOG_LEVEL = 'ERROR'` 

## 6. 数据解析 - 使用scrapy爬取糗事百科上段子的内容及其作者

### 6.1 创建工程qiubai_pro

```bash
❯ scrapy startproject qiubai_pro
New Scrapy project 'qiubai_pro', using template directory '/home/cxy/.local/lib/python3.8/site-packages/scrapy/templates/project', created in:
    /home/cxy/python_learning/crawler/scrapy_project/qiubai_pro

You can start your first spider with:
    cd qiubai_pro
    scrapy genspider example example.com
```

### 6.2 创建爬虫程序qiubai

```bash
❯ cd qiubai_pro
❯ scrapy genspider qiubai https://www.qiushibaike.com/
Created spider 'qiubai' using template 'basic' in module:
  qiubai_pro.spiders.qiubai

```

### 6.3 修改settings.py文件

```python
ROBOTSTXT_OBEY = False  # 将True改为False

LOG_LEVEL = 'ERROR'  # 添加这一行内容
```

### 6.4 进入spider/qiubai.py文件编写代码

```python
import scrapy


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    allowed_domains = ['https://www.qiushibaike.com/']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        """解析段子的作者和段子内容"""
        div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
        for div in div_list:
            author = div.xpath('./div[1]/a[2]/h2/text()')[0]
            content = div.xpath('./a[1]/div/span//text()')
            print(author, content)
			break

```

### 6.5 运行爬虫

```bash
❯ scrapy crawl qiubai
<Selector xpath='./div[1]/a[2]/h2/text()' data='\n爆笑大蒜派\n'> [<Selector xpath='./a[1]/div/span//text()' data='\n\n\n早上醒来发现50多岁的丈母娘剃了一个光头，这让我感到非常的疑惑。'>, <Selector xpath='./a[1]/div/span//text()' data='难道丈母娘最近和老丈人吵架了？打算远离凡尘出家为尼？'>, <Selector xpath='./a[1]/div/span//text()' data='昨晚我和老婆去丈母娘家里吃饭，丈母娘在厨房炒菜，我在一边帮忙洗菜。'>, <Selector xpath='./a[1]/div/span//text()' data='只见丈母娘很熟练的往锅里倒油，放肉，然后颠锅翻炒，煤气灶里的火苗嗖的一下子...'>, <Selector xpath='./a[1]/div/span//text()' data='我刚想夸丈母娘厨艺了得呢，老丈人在旁边说道：“你昨天才把头发烧没了，今天是...'>, <Selector xpath='./a[1]/div/span//text()' data='然后丈母娘和老丈人因为这点小事吵了一架，谁也不搭理谁。'>, <Selector xpath='./a[1]/div/span//text()' data='早上小舅子拿出两套校服，说：爸妈，你俩穿校服吧！'>, <Selector xpath='./a[1]/div/span//text()' data='丈母娘\n…\n'>, <Selector xpath='./a[1]/div/span//text()' data='查看全文'>]

```

可以看到：返回的不再是直接使用requests请求再通过解析获得的text结果了，而是author变成了选择器对象(因为取了索引0的内容)和content变成了选择器对象列表

那么如何获取出所需要的信息呢？可以使用extract()方法，即代码变成如下

```python
import scrapy


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    allowed_domains = ['https://www.qiushibaike.com/']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        """解析段子的作者和段子内容"""
        div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
        for div in div_list:
            author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()  # 使用extract()方法提取字符串
            content = div.xpath('./a[1]/div/span//text()').extract()  # 使用extract()方法提取字符串，这里返回一个列表
            print(author, content)
            break

```

再次执行

```bash
❯ scrapy crawl qiubai

世间同此薄凉
 ['\n\n\n突然，一个叫“单亲妈妈”的美女主动加我，我犹豫了一下，还是同意了。', '没想到这个单亲妈妈竟是我老婆的弟弟的媳妇，她和我舅子打架了，一怒之下，把名字改成单亲妈妈。', '我劝了她半天，然后又给小舅子打电话，数落他一顿，告诉他：你老婆已经改名单亲妈妈了。', '第二天早上，单亲妈妈已改回原来的名字了。', '我问弟媳，她说自从改成单亲妈妈，半天时间就有32人加她好友，小舅子怕了，主动承认错误。', '我看这招挺好呀，想想家中的悍妻，我也把微信名改成“单身爸爸”，然而一天了，也没人加好友。', '晚上回家还被老婆揍一顿。\n\n']

```

这样就获取到了需要的内容 - 作者和段子内容

不过，内容仍然是一个列表，可以使用join()方法获取，即对content进行如下处理：

```python
import scrapy


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    allowed_domains = ['https://www.qiushibaike.com/']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        """解析段子的作者和段子内容"""
        div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
        for div in div_list:
            author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
			# 若返回的列表中仅有一个元素，则上面一行语句可以使用下面这行语句代替
			# author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
            content = div.xpath('./a[1]/div/span//text()').extract()
            content = ''.join(content)  # 对content进行处理，获取其中的字符串
            print(author, content)
            break

```

最终达到了预期的目的

```bash
❯ scrapy crawl qiubai

禁言………


没想到，我一句话也有值一万块的时候。。。割。。。我们厂领导是外地人，昨天晚上喝了点酒，把别人车刮了掉点儿漆，本来不是啥大事儿，可对方见他酒驾，非要两千，不然就报警。我们领导无奈之下给我打了个电话，想让我这个本地人帮他说说话。我 到了之后，一看刮的也不严重，就给对方和我们领导都递了支烟，然后跟对方说到:“兄弟，我XX人，都是老乡，这是我们厂领导，给个面子，这也不严重，赔你五百算了吧。”我不说还好，我说完之后，那哥们儿立马不
…
查看全文
```

## 7. 持久化存储

Scrapy的持久化存储有2中方式
- 基于终端指令
- 基于管道

### 7.1 终端指令存储

`scrapy crawl <spider> -o <file_name>` 

使用终端指令存储，只能将spider爬虫文件(即第6节例子中的qiubai.py)中parse方法的返回值保存到本地的文本文件中

支持的文件格式： 'json', 'jsonlines', 'jl', 'csv', 'xml', 'marshal', 'pickle'

优点：简便、直接、快捷

缺点：局限性比较大 - 仅能存储为指定格式的文本文件，且仅能存储parse方法返回的数据

这种方式，不能直接将数据存储，而是要将数据封装起来才行

还是上面的代码例子，对数据进行一下封装，然后返回封装的数据进行存储

```python
import scrapy


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    allowed_domains = ['https://www.qiushibaike.com/']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        """解析段子的作者和段子内容 - 基于终端指令存储"""
        div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
        # 存储封装起来的数据
        all_data = []
        for div in div_list:
            author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            content = div.xpath('./a[1]/div/span//text()').extract()
            content = ''.join(content)
            #  print(author, content)
            #  break

            # 将数据封装起来，以便存储
            data_dict = {
                'author': author,
                'content': content
            }
            all_data.append(data_dict)

        return all_data

```

在终端命令行，执行下面的命令，将数据存储到当前目录的qiubai.csv文件中

```bash
❯ scrapy crawl qiubai -o ./qiubai.csv

```

在当前目录下，就生成了保存的文件quibai.csv

```bash
❯ tree
.
├── __init__.py
├── items.py
├── middlewares.py
├── pipelines.py
├── __pycache__
│   ├── __init__.cpython-38.pyc
│   └── settings.cpython-38.pyc
├── qiubai.csv  # 保存的数据文件
├── settings.py
└── spiders
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-38.pyc
    │   └── qiubai.cpython-38.pyc
    └── qiubai.py

3 directories, 12 files

```
### 7.2 基于管道存储

优点：通用性强，可以保存到本地各种格式的文件中，也可以保存到数据库中

缺点：编写代码时比较繁琐

**存储流程** 

1. 在爬虫程序中解析数据，上例中解析出来了author和content两个数据
2. 在item类(即items.py)中定义对应的两个属性

```python
# items.py

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QiubaiProItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	
	# 下面两个就是定义好的对应的属性
    author = scrapy.Field()
    content = scrapy.Field()
    #  pass

```

3. 将解析的数据封装存储到item类型的对象

```python
# qiubai.py

import scrapy
from qiubai_pro.items import QiubaiProItem


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    allowed_domains = ['https://www.qiushibaike.com/']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        """解析段子的作者和段子内容 - 基于管道存储"""
        div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
        # 存储封装起来的数据
        all_data = []
        for div in div_list:
            author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            content = div.xpath('./a[1]/div/span//text()').extract()
            content = ''.join(content)

            # 实例化item对象
            item = QiubaiProItem()
            # 将数据封装到item对象中
            item['author'] = author
            item['content'] = content
            # 将封装好的item对象提交给管道
            yield item

```

4. 将item类型的对象提交给管道进行持久化存储的操作
5. 在管道类(pipelines.py)的process_item中要将其接收到的item对象中的数据进行持久化存储操作

```python
pipelines.py

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QiubaiProPipeline:
    fp = None
    def process_item(self, item, spider):
        """专门用来处理item类型对象 - 可以接收爬虫文件提交过来的item对象
        这个方法每接收到一个item对象，就会被调用一次
        """
        # 取出接收到的item对象中的数据
        author = item['author']
        content = item['content']

        # 将数据存储到本地
        self.fp.write(author + ':' + content + '\n')
        return item

    def open_spider(self, spider):
        """重写父类的方法 - 开始爬虫
        这个方法只在开始爬虫的时候被调用一次
        """
        print('开始爬虫...')
        self.fp = open('./qiubai.txt', mode='w', encoding='utf-8')

    def close_spider(self, spider):
        """重写父类方法 - 结束爬虫"""
        print('结束爬虫!')
        self.fp.close()

```

6. 在配置文件中开启管道

```python
# 在settings.py中找到下面的内容

#ITEM_PIPELINES = {                                                                                                                                        
#    'qiubai_pro.pipelines.QiubaiProPipeline': 300,
#}

# 取消前面的注释
ITEM_PIPELINES = {                                                                                                                                        
    'qiubai_pro.pipelines.QiubaiProPipeline': 300,
}
# 这里的300表示的是优先级，数值越小则优先级越大
```

7. 执行爬虫后就会中当前目录下生成一个qiubai.txt的文件

`scrapy crawl qiubai` 
