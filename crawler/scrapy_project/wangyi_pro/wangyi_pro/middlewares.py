# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import time
from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from scrapy.http import HtmlResponse


class WangyiProDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        """拦截响应对象，进行篡改，以便获取符合要求的数据"""
        bro = spider.bro  # 获取在spider中定义的浏览器对象
        # 挑选出指定的响应对象 - 即5个板块的响应对象 - 进行篡改：
        # 1. 通过url指定request
        # 2. 通过request指定response
        if request.url in spider.module_urls:  # spider就是中wangyi.py中定义的类的实例
            # response即是需要的5个板块的响应对象
            # 针对这些响应对象进行篡改
            # 需要实例化一个新的响应对象 - 符合要求的,包含动态加载的新闻数据，来替换原来的响应对象
            # 如何获取动态加载的数据? - 可以使用selenium来实现
            # 因为这里的方法process_response在每次请求时都会被调用，所以比较好的方式是在爬虫类wangyi.py
            # 中实例化selenium浏览器，而不是在这里
            bro.get(request.url)  # 对5个板块进行请求
            time.sleep(2)
            # 获取页面源码 - 其中就包含了动态加载的数据
            page_text = bro.page_source
            new_response = HtmlResponse(url=request.url, body=page_text, encoding='utf-8', request=request)
            return new_response
        else:
            # response其它请求返回的响应对象，将其返回
            return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass
