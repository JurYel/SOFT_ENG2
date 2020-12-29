# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class LazadaPipeline:
    def __init__(self,db,user,passwd,host):
        self.db = db
        self.user = user
        self.passwd = passwd
        self.host = host

    @classmethod
    def from_crawler(cls,crawler):
        db_settings = crawler.settings.getdict("DB_SETTINGS")

        if not db_settings:
            raise NotConfigured

        db = db_settings['db']
        user = db_settings['user']
        passwd = db_settings['passwd']
        host = db_settings['host']

        return cls(db,user,passwd,host)

    def open_spider(self,spider):
        self.conn = pymysql.connect(db=self.db,
                                    user=self.user,
                                    passwd=self.passwd,
                                    host=self.host,
                                    charset='utf8', use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = "INSERT INTO lazada(prod_name, price) VALUES(%s, %s)"
        self.cursor.execute(sql,
                            (
                                item.get("prod_name"),
                                item.get("price")
                            ))
        self.conn.commit()
        return item
    
    def close_spider(self,spider):
        self.conn.close()