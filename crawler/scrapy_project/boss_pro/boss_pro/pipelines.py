# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BossProPipeline:
    fp = None

    def open_spider(self, spider):
        """爬虫开始"""
        self.fp = open('./boss.txt', mode='w', encoding='utf-8')

    def process_item(self, item, spider):
        """处理item并保存到本地"""
        job_name = item['job_name']
        job_desc = item['job_desc']
        self.fp.write(job_name + ':' + job_desc + '\n')
        return item

    def close_spider(self, spider):
        """结束爬虫"""
        self.fp.close()
