# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from scrapy.pipelines.images import ImagesPipeline


#  class ImgsProPipeline:
#      def process_item(self, item, spider):
#          return item


class ImgsPipeline(ImagesPipeline):
    """新定义的处理图片的类"""
    # 重写父类的3个方法

    def get_media_requests(self, item, info):
        """根据图片url进行图片请求"""
        #  print(item['src'])
        yield scrapy.Request(item['src'])

    def file_path(self, request, response=None, info=None):
        """指定图片数据持久化存储的路径"""
        # 获取图片名称 - 从url分离出来，取最后一部分apic27741_s.jpg
        # http://pic1.sc.chinaz.com/Files/pic/pic9/202009/apic27741_s.jpg
        img_name = request.url.split('/')[-1]
        return img_name

    def item_completed(self, results, item, info):
        """完成item的处理 - 并返回给下一个即将执行的管道类"""
        return item  # 将item返回给下一个即将执行下管道类
