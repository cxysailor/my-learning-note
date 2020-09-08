# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class QiubaiProPipeline:
    fp = None
    def process_item(self, item, spider):
        """专门用来处理item类型对象 - 可以接收爬虫文件提交过来的item对象
        这个方法每接收到一个item对象，就会被调用一次
        """
        # 取出接收到的item对象中的数据
        author = item['author']
        content = item['content']

        # 将数据存储到本地
        self.fp.write(author + ':' + content + '\n')
        return item  # 会将item传递给下一个即将执行的管道类，这里是MysalProPipeline

    def open_spider(self, spider):
        """重写父类的方法 - 开始爬虫
        这个方法只在开始爬虫的时候被调用一次
        """
        print('开始爬虫...')
        self.fp = open('./qiubai.txt', mode='w', encoding='utf-8')

    def close_spider(self, spider):
        """重写父类方法 - 结束爬虫"""
        print('结束爬虫!')
        self.fp.close()


class MysqlProPipeline(object):
    """将数据保存到数据库 - 会接收上一个执行的管道类传递过来的item"""

    conn = None
    cursor = None

    def open_spider(self, spider):
        """开始爬虫，连接到数据库"""
        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='password',
            db='spiderdata',
            charset='utf8'
            )

    def process_item(self, item, spider):
        """处理item数据"""
        self.cursor = self.conn.cursor()  # 创建游标
        try:
            self.cursor.execute('insert into qiubai values("%s", "%s")' % (item["author"], item["content"]))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

        return item  # 再将tiem传递给下一个要执行的管道类

    def close_spider(self, spider):
        """关闭爬虫"""
        self.cursor.close()
        self.conn.close()
