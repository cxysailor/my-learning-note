import scrapy


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    allowed_domains = ['https://www.qiushibaike.com/']
    start_urls = ['http://https://www.qiushibaike.com//']

    def parse(self, response):
        pass
