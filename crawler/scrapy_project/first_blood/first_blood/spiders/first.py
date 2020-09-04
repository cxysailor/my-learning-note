import scrapy


class FirstSpider(scrapy.Spider):
    # 爬虫文件的名称 - 爬虫源文件的唯一标识
    name = 'first'
    # 允许的域名 - 用来限定start_urls列表中那些url可以请求发送
    # 该域名下的所有的网页都会被请求；非其下的网页则不请求
    # 即仅请求百度下的网页，而不会请求搜狗的网页
    allowed_domains = ['www.baidu.com']
    # 起始url列表 - 其中的url会被scrapy自动的发送请求
    start_urls = ['http://www.baidu.com/', 'https://www.sogou.com']

    def parse(self, response):
        """用于数据解析
        response: 请求成功后对应的请求对象
        其请求对象的个数与start_urls中的url个数相对应
        要想获取所有的请求对象，就需要多次调用这个函数
        """
        print(response)
