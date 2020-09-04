import scrapy


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    allowed_domains = ['https://www.qiushibaike.com/']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        """解析段子的作者和段子内容"""
        div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
        # 存储封装起来的数据
        all_data = []
        for div in div_list:
            author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            content = div.xpath('./a[1]/div/span//text()').extract()
            content = ''.join(content)
            #  print(author, content)
            #  break

            # 将数据封装起来，以便存储
            data_dict = {
                'author': author,
                'content': content
            }
            all_data.append(data_dict)

        return all_data
