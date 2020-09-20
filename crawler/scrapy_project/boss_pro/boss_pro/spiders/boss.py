import scrapy
from boss_pro.items import BossProItem


class BossSpider(scrapy.Spider):
    name = 'boss'
    #  allowed_domains = ['www.zhipin.com/']
    start_urls = ['https://www.zhipin.com/job_detail/?query=python&city=100010000&industry=&position=100109']
    base_url = 'https://www.zhipin.com/c100010000/?query=python&page=%d'
    page_num = 2  # 因为第一页已经爬取了，故从第二页开始

    def parse(self, response):
        """解析岗位名称及其对应的岗位描述内容的url"""
        li_list = response.xpath('//*[@id="main"]/div/div[2]/ul/li')
        #  print(li_list)
        for li_tag in li_list:
            item = BossProItem()  # 实例化一个item对象
            job_name = li_tag.xpath('.//div[@class="job-title"]/span[1]/a/text()').extract_first()
            base_url = 'https://www.zhipin.com'
            detail_url = base_url + li_tag.xpath('.//div[@class="jog-title"]/span[1]/a/@href').extract_first()
            # 将job_name封装到item中
            item['job_name'] = job_name

            # 对详情页detail_url发起请求获取详情页的数据 - 需要手动发送请求
            # 由于岗位名称与岗位描述不在同一个页面上
            # 数据解析的方法就不一样
            # 所以callback不能调用self.parse了
            # 需要重新定义一个解析函数，对岗位描述进行解析
            # 岗位描述job_desc是在另外一个函数parse_detail中解析的，所以要将item传递过去
            # 可以中yield语句中加上meta={}参数来实现item的传递 - 由于是中发送请求的过程中传递的参数，故叫请求传参
            yield scrapy.Request(url=detail_url, callback=self.parse_detail, meta={'item': item})

        # 执行分页爬取的功能
        if self.page_num <= 3:
            new_url = format(self.base_url % self.page_num)
            self.page_num += 1
            # 发送请求
            yield scrapy.Request(new_url, callback=self.parse)

    def parse_detail(self, response):
        """解析详情页中的岗位描述内容"""
        # 回调函数接收请求传参传递过来的item - 这样就完成来请求传参的过程，将item传递过来了
        item = response.meta['item']
        job_desc = response.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div//text()').extract()
        job_desc = ''.join(job_desc)
        # 将job_desc封装到item中
        item['job_desc'] = job_desc
        # 将封装了岗位名称和岗位描述的item提交给管道，进行存储
        yield item
