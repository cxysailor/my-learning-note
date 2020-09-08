import scrapy


class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    #  allowed_domains = ['http://www.521609.com/meinvxiaohua/']
    start_urls = ['http://www.521609.com/meinvxiaohua/']

    # 生成一个url模板
    url = 'http://www.521609.com/meinvxiaohua/list12%d.html'
    page_num = 2

    def parse(self, response):
        li_list = response.xpath('/html/body/div[4]/div[2]/div[2]/ul/li')
        for li in li_list:
            img_name = li.xpath('./a[2]/text() | ./a[2]/b/text()').extract_first()
            print(img_name)

        if self.page_num <= 11:
            new_url = format(self.url % self.page_num)
            print(new_url)
            self.page_num += 1
            # 手动发送请求
            # callback回调parse函数进行数据解析，因为所有页面的解析方式都一样
            yield scrapy.Request(url=new_url, callback=self.parse)
