# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WangyiProPipeline:
    fp = None

    def open_spider(self, spider):
        """开始爬虫"""
        self.fp = open('./wangyi_news.txt', mode='w', encoding='utf-8')

    def process_item(self, item, spider):
        news_title = item['news_title']
        news_content = item['news_content']
        self.fp.write(news_title + ':' + news_content + '\n')
        #  print(item)
        return item

    def close_spider(self, spider):
        """结束爬虫"""
        print('爬虫结束！')
        self.fp.close()