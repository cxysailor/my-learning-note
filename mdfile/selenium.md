# Selenium模块的基本使用

## 1. selenium模块与爬虫之间的关联
1. 便捷地获取网站中动态加载的数据 - 这些数据通过普通的requests无法获取
2. 便捷地实现模拟登录

## 2. selenium模块简介

是基于浏览器自动化的一个模块，通俗地说就是通过程序代码控制浏览器的操作。

## 3. selenium模块使用流程

### 3.1 环境的安装

- pip install --user selenium

### 3.2 下载一个浏览器的驱动程序

- chrome的驱动器[chromedriver](http://chromedriver.storage.googleapis.com/index.html) 
- 国内可以使用淘宝的镜像下载chromedriver[chromedriver taobao](http://npm.taobao.org/mirrors/chromedriver) 
- firefox的驱动器[firefoxdriver](https://github.com/mozilla/geckodriver/releases) 
- 下载自己浏览器当前版本对应的驱动器即可

	比如我现在Manjaro系统上的版本是：
	Chromium	84.0.4147.125 (正式版本) Arch Linux （64 位）
	那就下载这个版本对应的即可

Manjaro系统20.0.3版本上安装来chromium，即可直接使用，无需再次下载了。

以上都准备妥以后，就可以开始正式的使用selenium了。

### 3.3 实例化一个浏览器对象

```python
from selenium import webdriver

driver = webdriver.Chrome(
		executable_path="chromedriver",
		port=0,
		options=None,
		service_args=None,
		desired_capabilities=None,
		service_log_path=None,
		chrome_options=None,
		keep_alive=True
)
参数可以不写，或者仅需要指定webdriver的路径executable_path
```

### 3.4 编写基于浏览器自动化的操作代码

- 发起请求 - driver.get(url)
- 标签定位 - 使用driver.find_element系列的方法
- 标签交互 - tag.send_keys('string') - 给标签传入一个字符
- 点击按钮 - tag.click()
- 执行js程序 - driver.execute_script('js') - 比如这样的一段代码window.scrollTo(0,document.body.scrollHeight)用于向下滚动一屏
- 前进与后退 - driver.forward() driver.back()
- 关闭浏览器 - driver.quit()
