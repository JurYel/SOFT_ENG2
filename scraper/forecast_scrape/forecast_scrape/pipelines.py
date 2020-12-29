from itemadapter import ItemAdapter
import pymysql

class ForecastScrapePipeline:
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
        sql = "INSERT INTO weather(night_period, day_period, night_temp, day_temp, night_humidity, day_humidity) VALUES(%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql,
                            (
                                item.get("night_period"),
                                item.get("day_period"),
                                item.get("night_temp"),
                                item.get("day_temp"),
                                item.get("night_humidity"),
                                item.get("day_humidity")
                            ))
        self.conn.commit()
        return item

    def close_spider(self,spider):
        self.conn.close()
