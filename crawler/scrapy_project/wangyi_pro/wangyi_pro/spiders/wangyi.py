import scrapy
from wangyi_pro.items import WangyiProItem
from selenium import webdriver


class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    #  allowed_domains = ['https://news.163.com']
    start_urls = ['https://news.163.com/']
    # 存储板块对应详情页的url
    module_urls = []

    def __init__(self):
        self.bro = webdriver.Chrome()

    def parse(self, response):
        """解析所要爬取的板块对应的详情页的url"""
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        module_index = [3, 4, 6, 7, 8]  # 国内、国际、军事、航空、无人机5个板块对应的li标签顺序
        for idx in module_index:
            module_url = li_list[idx].xpath('./a/@href').extract_first()  # 板块对应的详情页面url
            self.module_urls.append(module_url)

        # 依次对每一个板块对应的页面进行请求
        for url in self.module_urls:
            #  print(url)
            yield scrapy.Request(url, callback=self.parse_each_module)

    def parse_each_module(self, response):
        """解析每一个板块页面中对应的新闻的标题和新闻内容的url,这里的response是经过篡改后的"""
        div_list = response.xpath('/html/body/div/div[3]/div[4]/div[1]/div/div/ul/li/div/div')
        for div_tag in div_list:
            news_title = div_tag.xpath('./div/div/h3/a/text()').extract_first()  # 新闻标题
            news_content_url = div_tag.xpath('./div/div/h3/a/@href').extract_first()  # 新闻内容的url
            #  print(news_title)
            #  print(news_content_url)
            # 使用请求传参
            item = WangyiProItem()
            item['news_title'] = news_title
            # 对新闻内容url发起请求
            if news_content_url is None:
                continue
            yield scrapy.Request(url=news_content_url, callback=self.parse_content, meta={'item': item})

    def parse_content(self, response):
        """对新闻内容爬取并解析"""
        news_content = response.xpath('//*[@id="endText"]//text()').extract()
        news_content = ''.join(news_content)
        item = response.meta['item']
        item['news_content'] = news_content
        #  print(item)
        
        yield item

    def closed(self, spider):
        """关闭浏览器"""
        self.bro.quit()
