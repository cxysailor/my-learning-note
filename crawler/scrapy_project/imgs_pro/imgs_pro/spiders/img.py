import scrapy
from imgs_pro.items import ImgsProItem


class ImgSpider(scrapy.Spider):
    name = 'img'
    #  allowed_domains = ['https://sc.chinaz.com/tupian/']
    start_urls = ['https://sc.chinaz.com/tupian/']

    def parse(self, response):
        """解析出图片的url"""
        div_list = response.xpath('//*[@id="container"]/div')
        for div in div_list:
            # 对于懒加载 - 要使用其伪属性来解析数据
            src = div.xpath('./div/a/img/@src2').extract_first()
            #  print(src)

            # 实例化item对象
            item = ImgsProItem()
            # 将获取的图片url封装
            item['src'] = src
            #  print(item['src'])
            # 将item提交
            yield item
