# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem, NotConfigured
import MySQLdb

class MoviesAllPipeline:
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
        self.conn = MySQLdb.connect(db=self.db,
                                user=self.user,
                                passwd=self.passwd,
                                host=self.host,
                                charset='utf8',use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self,item,spider):
        if any(item.values()):
            sql = "INSERT INTO movies(title, year, ratings, metascore, votes, gross_income) VALUES(%s, %s, %s, %s, %s, %s)"
            self.cursor.execute(sql,
                                (
                                    item.get("title"),
                                    item.get("year"),
                                    item.get("ratings"),
                                    item.get("metascore"),
                                    item.get("votes"),
                                    item.get("gross_income")
                                ))
            self.conn.commit()
            return item
        else:
            raise DropItem(f"NULL Value found;")

    def close_spider(self,spider):
        self.conn.close()
