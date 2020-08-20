# BeautifulSoup4解析

## 1. BeautifulSoup4是Python独有的一种数据解析方式

## 2. 数据解析原理：
1. 标签定位
2. 提取标签、标签属性中存储的数据值

## 3. BeautifulSoup4数据解析原理：
1. 实例化一个BeautifulSoup4对象，并且将页面源码数据加载到该对象中
2. 调用BeautifulSoup4对象中的属性或方法，进行标签定位和数据提取

## 4. 环境安装
```python
pip install --user bs4  # BeautifulSoup4来自bs4库

pip install --user lxml  # bs4使用的解析器
```
## 5. 如何实例化对象

先导入BeautifulSoup包

实例化对象时，分为加载本地html文件和加载网页源码2种。

导入BeautifulSoup4包

```python
from bs4 import BeautifulSoup as bs
```

将本地的html文件加载到BeautifulSoup4对象实例中

```python
with open('./test.html', mode='r', encoding='utf-8') as fp:
		soup = bs(fp, 'lxml')
```
将网页源码加载到BeautifulSoup4实例对象中

```python
page_text = response.text  # 获取的网页源码
soup = bs(page_text, 'lxml')
```

## 6. 用于解析数据的方法和属性

比如解析这样一个html文件test.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
        <meta charset="UTF-8">
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
				<img src="http://www.baidu.com/meinv.jpg" alt="">
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

### 6.1 提供的用于定位标签的常用的方法和属性 

- soup.tag_name 返回的是html中第一次出现的对应的标签(比如soup.a，即找到第一个a标签...)
- soup.find('tag_name')
		* 第1种用法:等价于soup.tag_name,返回的是html中第一次出现的对应的标签(比如soup.find(a)，即找到第一个a标签...)
		* 第2种用法:属性定位 - 根据属性定位到对应的标签
				soup.find('tag_name', attr='xxxx')
				soup.find('div', class_='song')  # 定位到class属性为song的div
- soup.find_all('tag_name', [attr_='xxxx']) - 返回一个列表
		* 获取所有对应tag_name的标签
				soup.find_all('a')  # 获取所有的a标签
		* 获取所有对应属性的标签
				soup.find_all('a', title='du')  # 获取所有title属性为du的a标签
- soup.select('selector')  根据选择器来定位相应的标签 - 返回一个列表
		* 选择器selector可以是id选择器、class选择器、tag选择器等
				+ soup.select('.tang')  # 使用class为tang的标签 - class选择器
				+ soup.select('#df')  # 获取id为df的标签 - id选择器
				+ soup.select('a')  # 获取所有的a标签 - tag选择器
				+ soup.select('b')  # 获取所有的b标签 - tag选择器
		* 选择器selector可以是层级选择器 
				+ soup.select('.tang > ul > li > a')[0]  # 获取class为tang的标签下的ul，li下的li标签，li下的a标签，取其中的第一个a标签 
				+ soup.select('.tang > ul a')[0]  # 大于号>表示一个层级；空格表示多个层级 与上面获取的结果一样

### 6.2 获取标签中的文本数据

在定位到标签后，可以调用下列属性或方法来获取文本数据:

- text属性
		* soup.a.text 获取第一个a标签中的文本内容
		* soup.select('.tang > ul > li a')[1].text
- string属性
		* soup.select('.tang > ul > li a')[1].string
		* soup.select('#df > a')[0].string
- get_text()方法
		* soup.select('#df > a')[0].get_text()

text属性和get_text()方法可以获取某一个标签下的所有的文本内容，无论是直系还是隔代的标签都可以获取到

string属性只能获取该标签下直系的标签的文本内容

### 6.3 获取标签中的属性值

定位到标签后，在后面加上中括号[],里面写上属性名

		soup.tag_name['attr']

		soup.select('.tang > ul > li > a')[1]['title']
		soup.a['href']

## 7. BeautifulSoup4应用示例

**获取三国演义的章节标题及其内容**，网址为:[三国演义](https://www.shicimingju.com/book/sanguoyanyi.html) 

**对网页进行分析：**

- 打开网页，可以看到小说的标题、年代、作者、对小说的简介以及每个章节的标题等
- 通过对源代码的分析，章节标题在这个div中,里面有章节标题及其内容的链接

```html
<div class="book-mulu">
    <ul>
        <li><a href="/book/sanguoyanyi/1.html">第一回·宴桃园豪杰三结义 斩黄巾英雄首立功</a></li>
		<li><a href="/book/sanguoyanyi/2.html">第二回·张翼德怒鞭督邮 何国舅谋诛宦竖</a></li>
		...
	</ul>
</div>
```
- 打开任意一个标题链接，就进入到对应的文章内容页面，对这个页面进行分析。文章内容在

```html
<div class="chapter_content">
		<p>&nbsp;&nbsp;&nbsp;&nbsp;滚滚长江东逝水，浪花淘尽英雄。是非成败转头空。青山依旧在，几度夕阳红。    白发渔樵江渚上，惯看秋月春风。一壶浊酒喜相逢。古今多少事，都付笑谈中。</p>
		<p>&nbsp;&nbsp;&nbsp;&nbsp;——调寄《临江仙》</p>
		<p>&nbsp;&nbsp;&nbsp;&nbsp;话说天下大势，分久必合，合久必分。周末七国分争，并入于秦。及秦灭之后，楚、汉分争，又并入于汉。汉朝自高祖斩白蛇而起义，一统天下，后来光武中兴，传至献帝，遂分为三国。推其致乱之由，殆始于桓、灵二帝。桓帝禁锢善类，崇信宦官。及桓帝崩，灵帝即位，大将军窦武、太傅陈蕃，共相辅佐。时有宦官曹节等弄权，窦武、陈蕃谋诛之，机事不密，反为所害，中涓自此愈横。</p>
		<p>&nbsp;&nbsp;&nbsp;&nbsp;建宁二年四月望日，帝御温德殿。方升座，殿角狂风骤起。只见一条大青蛇，从梁上飞将下来，蟠于椅上。帝惊倒，左右急救入宫，百官俱奔避。须臾，蛇不见了。忽然大雷大雨，</p>
</div>
```

**通过上面的分析，得出获取的思路：**

1. 爬取首页代码，获取其中的章节对应的标题和链接
2. 爬取每一个章节对应的链接，获取章节的内容

**具体的实现代码：**

```python
#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : cxysailor
#   Email         : cxysailor@163.com
#   File Name     : bs_sanguoyanyi.py
#   Last Modified : 2020-08-18 13:50
#   Describe      :
#
# ====================================================
import time
import requests
from bs4 import BeautifulSoup as bs


if __name__ == "__main__":
    # UA伪装
    headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
            }
    # 对首页进行爬取
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    # 获取首页数据
    page_text = requests.get(url=url, headers=headers).text
    # 在首页数据中解析出章节标题及其对应的内容链接
    soup = bs(page_text, 'lxml')  # 实例化一个bs4对象，并将获取的首页数据加载
    # 解析标题和url
    li_list = soup.select('.book-mulu > ul > li')  # 定位到li标签
    with open('./sanguoyanyi.txt', mode='w', encoding='utf-8') as fp:
        # 遍历出li标签的所有a标签并获取信息
        for li in li_list:
            title = li.a.string  # 标题
            detail_url = 'https://www.shicimingju.com' + li.a['href']  # 对应内容的url
            # 对detail_url发起请求，解析出章节内容
            detail_page_text = requests.get(url=detail_url, headers=headers).text
            # 解析章节内容
            detail_soup = bs(detail_page_text, 'lxml')
            div_tag = detail_soup.find('div', class_='chapter_content')  # 定位到class为chapter-conent的div标签
            # 获取内容
            content = div_tag.text
            # 保存
            fp.write(title + ':' + content + '\n')
            print(title, '爬取成功!')
            time.sleep(2)


```

