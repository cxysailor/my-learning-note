# xpath数据解析

## 1. xpath是最常用、最便捷高效的一种数据解析方式，通用性比较强。

## 2. xpath的解析原理

- 实例化一个etree的对象，并且将需要解析的页面源码数据加载进来
- 调用etree对象中的xpath方法，结合着xpath表达式，实现标签的定位和内容的获取

## 3. 环境安装
		pip install --user lxml

## 4. xpath的具体实现流程

### 4.1 实例化etree对象

- etree是从lxml中导入的

		from lxml import etree
- 加载本地的html文档
		* etree.parse(file_path)
- 加载网上获取的网页源码数据
		* etree.HTML('page_text')

### 4.2 调用etree对象实例化的xpath()方法获取标签和数据
		
		xpath('xpath_expression')

## 5. xpath表达式

### 5.1 标签定位

| 层级符号                            | 说明                              | 举例                        |
| ------                              | ------                            | ------                      |
| 斜杠/                               | 从根节点开始定位，一个/是一个层级 | '/html/body/div'            |
| 双斜杠//                            | 在2个标签之间，表示多个层级       | '/html//div'                |
| 双斜杠//                            | 放在开头，表示从任意位置开始      | '//div'                     |
| 属性定位tag[@attr='value']          | 使用标签的属性定位                | '//div[@class="song"]'      |
| 索引定位tag[@attr='value'/tag[num]] | 使用标签的索引定位(索引从1开始)   | '//div[@class="song"]/p[3]' |

以本地的test.html文档为例，其内容

		注意：html文档中所有的自闭合标签后面都要有/，即<meta charset="UTF-8"/>,否则在使用xpath解析时会出错！！！

```html
<!DOCTYPE html>
<html lang="en">
<head>
        <meta charset="UTF-8"/>
        <title>BeautifulSoup4 Testing</title>
</head>
<body>
        <div>
                <p>百里守约</p>
        </div>
		<div class='song'>
				<p>李清照</p>
				<p>王安石</p>
				<p>苏轼</p>
				<p>柳宗元</p>
				<a href="http://www.song.com" title='赵匡胤' target='_self'>
						<span>This is a span</span>
				宋朝是最强大的王朝，不是军队的强大，而是经济很强大，国民都很有钱</a>
				<a href="" class='du'>总为浮云能蔽日，长安不见使人愁</a>
				<img src="http://www.baidu.com/meinv.jpg" alt=""/>
		</div>
		<div class='tang'>
				<ul>
						<li><a href="http://www.baidu.com" title='qing'>清明时节雨纷纷，路上行人欲断魂。借问酒家何处有，牧童遥指杏花村。</a></li>
						<li><a href="http://www.163.com" title='qin'>秦时明月汉时关，万里长征人未还。但使龙城飞将在，不叫胡马度阴山。</a></li>
						<li><a href="http://www.126.com" title='qi'>岐王宅里寻常见，崔九堂前几度闻。正是江南好风景，落花时节又逢君。</a></li>
						<li id='df'><a href="http://www.sina.com" title='du'>杜甫</a></li>
						<li><a href="http://www.dudu.com" title='du'>杜牧</a></li>
						<li><b>杜小月</b></li>
						<li><i>度蜜月</i></li>
						<li><a href="http://www.haha.com" title='feng'>凤凰台上凤凰游，凤去台空江自流。吴宫花草埋幽径，晋代衣冠成古丘。三山半落青天外，二水中分白鹭洲。总为浮云能蔽日，长安不见使人愁。</a></li>
				</ul>
		</div>
</body>
</html>

```
**实例化etree对象** 

		tree = etree.parse('test.html')

**获取title标签** 
		
		tree.xpath('/html/head/title')

		[<Element title at 0x7f0e16d5e880>]  # 返回一个对象的列表(1个title元素标签)

**获取div标签** 

		tree.xpath('/html/body/div')

		[<Element div at 0x7f63f552ebc0>, <Element div at 0x7f63f552eac0>, <Element div at 0x7f63f552ec00>] (3个div元素标签)

		tree.xpath('/html//div')  # 获取了同样的标签
		
		[<Element div at 0x7f63f552ebc0>, <Element div at 0x7f63f552eac0>, <Element div at 0x7f63f552ec00>] (3个div元素标签)

		tree.xpath('//div')  # 获取了同样的标签

		[<Element div at 0x7f63f552ebc0>, <Element div at 0x7f63f552eac0>, <Element div at 0x7f63f552ec00>] (3个div元素标签)
		
**获取class属性为song的div标签** 

		tree.xpath('//div[@class="song"]')

		[<Element div at 0x7fcad1b8ebc0>]

**获取class属性为song的div标签下的内容为苏轼的p标签** 

		tree.xpath('//div[@class="song"]/p[3]')

### 5.2 获取数据(标签的文本和属性值)

#### 5.2.1 获取文本


| 方法或属性 | 说明                     | 举例                                   |
| ------     | ------                   | ------                                 |
| /text()    | 获取标签下直系的文本内容 | '//div[@class="tang"]//li[5]/a/text()' |
| //text()   | 获取标签下所有的文本内容 | '//li[7]//text()'                      |

		tree.xpath('//div[@class="tang"]//li[5]/a/text()')[0]  # 获取杜牧

		tree.xpath('//li[7]//text()')[0]  # 获取度蜜月

		tree.xpath('//div[@class="tang"]//text()')  # 获取class属性为tang的div标签下的所有文本内容

#### 5.2.2 获取属性值

|方法 |说明 |举例 |
|------ |------ |------ |
|tag/@attr |获取标签属性的值 |'//div[@class="song"]//img/@src' |

		tree.xpath('//div[@class="song"]/img/@src')  # 获取img标签的src属性值

## 6. xpath应用示例

### 6.1 爬取58同城上二手房的房源信息 

知识点：xpath标签定位与文本、属性值的获取

```python
#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : xpath_demo.py
#   Last Modified : 2020-08-18 20:27
#   Describe      :
#
# ====================================================
import time
import random
import requests
from lxml import etree


class Crawl58SecondHandHouse():
    """爬取58同城上的二手房信息"""
    def __init__(self):
        self.url = 'https://sh.58.com/pudongxinqu/ershoufang/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'
        }
        self.proxy = [
            {'http': 'http://102.69.32.1:8080'},
            {'http': 'http://112.111.77.191:9999'},
            {'http': 'http://123.55.102.240:9999'},
            {'http': 'http://94.51.83.2:8080'},
            {'http': 'http://178.210.129.150:1234'},
            {'http': 'http://185.222.59.161:5836'},
            {'http': 'http://183.89.41.17:8080'},
            {'http': 'http://175.42.123.143:9999'},
            {'http': 'http://168.228.193.217:999'},
            {'http': 'http://51.158.29.37:5836'}
        ]
        self.num = 1
        self.li_lists = []

    def get_info(self):
        """获取数据"""
        # 爬取网页
        page_text = requests.get(url=self.url, headers=self.headers, proxies=random.choice(self.proxy)).text
        # 实例化对象
        tree = etree.HTML(page_text)
        # 获取页面总数
        pages = tree.xpath('//div[@class="pager"]/a')
        max_page = pages[-2].xpath('./span/text()')[0]
        max_page = int(max_page)
        # 爬取每一页的信息
        for n in range(0, max_page):
            # 新的url - 每一页的url
            each_url = self.url + 'pn' + str(n + 1)
            print(each_url)
            # 爬取新的url
            each_page_text = requests.get(url=each_url, headers=self.headers, proxies=random.choice(self.proxy)).text
            #  print(each_page_text)
            each_page_tree = etree.HTML(each_page_text)
            # 获取class属性为house-list-wrap的ul标签下的所有的li标签
            li_list = each_page_tree.xpath('//ul[@class="house-list-wrap"]/li')
            self.li_lists.append(li_list)
            time.sleep(0.5)
        return self.li_lists

    def saving_info(self):
        """保存数据"""
        lis = self.get_info()
        with open('./ershoufang.txt', mode='w', encoding='utf-8') as fp:
            for lls in lis:
                for li in lls:
                    try:
                        # 房源标题
                        title = li.xpath('./div[2]/h2/a/text()')[0]
                        # 总价
                        price = str(li.xpath('./div[3]/p[1]/b/text()')[0]) \
                                + li.xpath('./div[3]/p[1]/text()')[0]
                        # 单价
                        unit_price = li.xpath('./div[3]/p[2]/text()')[0]
                        # 房型布局
                        layout = li.xpath('./div[2]/p[1]/span[1]/text()')[0]
                        # 房子面积
                        area = li.xpath('./div[2]/p[1]/span[2]/text()')[0]
                        # 房子朝向
                        toward = li.xpath('./div[2]/p[1]/span[3]/text()')[0]
                        # 楼层
                        layer = li.xpath('./div[2]/p[1]/span[4]/text()')[0]
                        # 楼盘名称
                        name = li.xpath('./div[2]/p[2]/span[1]/a[1]/text()')[0]
                        # 楼盘坐落地区
                        strict = li.xpath('./div[2]/p[2]/span[1]/a[2]/text()')[0]
                        # 楼盘地址
                        location = li.xpath('./div[2]/p[2]/span[1]/a[3]/text()')[0] \
                                + li.xpath('./div[2]/p[2]/span[2]/text()')[0]
                    except IndexError as e:
                        #  print(e)
                        location = li.xpath('./div[2]/p[2]/span[1]/a[3]/text()')[0]
                    #  保存数据
                    fp.write(((str(self.num) + '.'
                               + title + ','
                               + price + ','
                               + unit_price + ','
                               + layout + ','
                               + str(area) + ','
                               + toward + ','
                               + layer + ','
                               + name + ','
                               + strict + ','
                               + location
                               + '\n')))
                    self.num += 1


if __name__ == "__main__":
    c = Crawl58SecondHandHouse()
    c.saving_info()
    print('All Done !')

```

### 6.2 爬取彼岸图网的美女图片

知识点：解决中文乱码问题

```python
#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : xpath_netbian.py
#   Last Modified : 2020-08-19 21:26
#   Describe      :
#
# ====================================================
import time
import os
import requests
from lxml import etree


class NetBiAnPic():
    """获取彼岸图网上的图片"""
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
        }
        self.url = 'http://pic.netbian.com/4kmeinv/'

    def get_infomation(self):
        """爬取信息"""
        # 爬取美女图的首页
        response = requests.get(url=self.url, headers=self.headers)
        # 可以手动设置编码格式 - 解决中文乱码问题，但是通常使用下面43行的做法
        #  response.encoding = 'gbk'
        page_text = response.text
        # 创建etree实例
        tree = etree.HTML(page_text)

        # 获取src与alt的属性值
        li_list = tree.xpath('//div[@class="slist"]//li')  # 获取所有相关的li标签
        return li_list

    def save_images(self):
        """爬取并保存图片"""
        li_list = self.get_infomation()
        #  print(li_list)
        # 创建图片存储目录
        if not os.path.exists('./images'):
            os.mkdir('./images')
        for li in li_list:
            img_url = 'http://pic.netbian.com' + li.xpath('./a/img/@src')[0]  # 图片的url
            ex_name = li.xpath('./a/img/@src')[0].split('.')[1]  # 图片的扩展名
            img_name = li.xpath('./a/img/@alt')[0] + '.' + ex_name  # 图片名称
            # 解决中文乱码问题 - 比较通用的办法，哪里有乱码就在哪里解决
            img_name = img_name.encode('iso-8859-1').decode('gbk')
            #  print(img_url, img_name)

            # 爬取图片数据
            img_data = requests.get(url=img_url, headers=self.headers).content

            # 保存图片
            img_path = './images/' + img_name  # 图片路径
            with open(img_path, mode='wb') as fp:
                fp.write(img_data)
            print(img_name, 'Completed downloading!')
            time.sleep(0.5)


if __name__ == "__main__":
    nbap = NetBiAnPic()
    nbap.save_images()
    print('All Completed!')

```

### 6.3 爬取真气网上的城市名称

知识点：多个xpath表达式写在一起，使用|分隔，表示or

```python
#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : xpath_city.py
#   Last Modified : 2020-08-21 13:35
#   Describe      : 
#
# ====================================================
import requests
from lxml import etree


class GetAllCity():
    """获取真气网上的城市名称"""
    def __init__(self):
        super(GetAllCity, self).__init__()
        self.url = 'https://www.aqistudy.cn/historydata/'
        self.headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'
        }
        self.city_list = []  # 存储城市

    def get_info(self):
        """获取信息"""
        page_text = requests.get(url=self.url, headers=self.headers).text
        #  print(page_text)
        tree = etree.HTML(page_text)
        # 将两个xpath表达式写在一起 - 这个例子的知识点
        a_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
        for a in a_list:
            city = a.xpath('./text()')[0]
            self.city_list.append(city)
        print(self.city_list, len(self.city_list))


if __name__ == "__main__":
    gac = GetAllCity()
    gac.get_info()

```
### 6.4 爬取站长素材中的免费简历模板

**分析及思路** 

```html
1. 爬取并解析：http://sc.chinaz.com/jianli/free.html
2. 获取其中每个模板的url：
xpath表达式：//*[@id="container"]/div[1]/a/@href
元素标签
<a target="_blank" href="http://sc.chinaz.com/jianli/200821223120.htm">
   <img src="http://pic1.sc.chinaz.com/Files/pic/jianli/202008/jianli13378_s.jpg" alt="英语简历格式范文">
</a>
3. 对每个模板的url爬取并解析
4. 获取每个模板的下载链接
xpath表达式：//*[@id="down"]/div[2]/ul/li[1]/a/@href
元素标签
<a href="http://downsc.chinaz.net/Files/DownLoad/jianli/202008/jianli13378.rar" target="_blank">福建电信下载</a>
5. 爬取每个模板的下载链接，即可完成模板下载
6. 第一页的url是以free.html结尾，与后面的页面url不一致，且不能直接加上_1.html，所以需要做处理
7. 第二页是从free_2.html开始的，注意不是free_1.html

```

```python3
#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : xpath_template.py
#   Last Modified : 2020-08-21 15:06
#   Describe      : 爬取站长素材中的免费模板
#
# ====================================================
import os
import time
import requests
from lxml import etree


class TemplateGet():
    """docstring for TemplateGet"""
    def __init__(self):
        super(TemplateGet, self).__init__()
        self.url = 'http://sc.chinaz.com/jianli/free.html'
        self.headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
        }
        self.url_list = []
        self.temp_name = []

    def get_page(self, url):
        """获取免费模板页的网页源代码"""
        page_text = requests.get(url=url, headers=self.headers).text
        tree = etree.HTML(page_text)
        return tree

    def get_max_page_num(self):
        """获取页面的最大数值"""
        t = self.get_page(self.url)
        # 获取页面的最大数值 - 即共有多少个页面
        max_b = t.xpath('//div[@class="pagination fr clearfix clear"]/a/b')[-1]
        max_page = int(max_b.xpath('./text()')[0])
        return max_page

    def get_each_url(self, url):
        """获取每一页的url以及模板的名称"""
        tree = self.get_page(url)
        # 获取每个模板对应的a标签
        each_a_list = tree.xpath('//*[@id="container"]/div/a')
        for each_a in each_a_list:
            # 获取每个模板对应的url
            each_url = each_a.xpath('./@href')[0]
            # 获取每个模板的名称
            each_name = each_a.xpath('./img/@alt')[0].encode('iso-8859-1').decode('utf-8')
            self.url_list.append(each_url)
            self.temp_name.append(each_name)
        return self.url_list, self.temp_name

    def download_save_data(self, url):
        """下载一个页面中每个免费模板并保存"""
        if not os.path.exists('./template_lib'):
            os.mkdir('./template_lib')
        urls, names = self.get_each_url(url)
        for n in range(len(urls)):
            # 爬取每个模板的详情页面内容
            each_page_text = requests.get(url=urls[n], headers=self.headers).text
            each_tree = etree.HTML(each_page_text)
            # 获取模板的下载链接
            down_url = each_tree.xpath('//*[@id="down"]/div[2]/ul/li[1]/a[1]/@href')[0]
            #  print(down_url)
            # 下载模板
            each_data = requests.get(url=down_url, headers=self.headers).content
            # 保存文件路径
            file_path = './template_lib/' + str(n + 1) + names[n] + '.rar'
            # 保存下载的模板
            with open(file_path, mode='wb') as fp:
                fp.write(each_data)
            print(f'第{n}个下载完成')
            time.sleep(2)


if __name__ == "__main__":
    tg = TemplateGet()
    max_p = tg.get_max_page_num()  # 免费模板的页面总数
    #  print(max_page)
    # 这个循环控制的是每一个页面
    for nu in range(2):
    #  for nu in range(max_p):  # 下载所有的免费模板页面
        url = 'http://sc.chinaz.com/jianli/free'  # 由于第一页与其他页面的url不一样，需要特殊处理
        if nu == 0:
            url = url + '.html'
        else:
            url = url + '_' + str(nu + 1) + '.html'  # 第二页是free_2.html结尾
        print(url)
        tg.download_save_data(url)
    print('Done !')

```


