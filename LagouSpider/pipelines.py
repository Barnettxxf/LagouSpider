# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import pymysql
from twisted.enterprise import adbapi

from LagouSpider.items import LagouspiderItem, LagouInterviewItem


class LagouspiderPipeline(object):
    def process_items(self, item, spider):
        return item


class MysqlTwistedPipline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = settings['LOCALMYSQLCONFIG']
        dbparms['cursorclass'] = pymysql.cursors.DictCursor
        dbpool = adbapi.ConnectionPool('pymysql', **dbparms)
        return cls(dbpool)

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider)
        return item

    def do_insert(self, cursor, item):
        insert_sql, params = item.get_insert_sql()
        cursor.execute(insert_sql, params)

    def handle_error(self, failure, item, spider):
        print(failure)

class MysqlPipline(object):
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor

    @classmethod
    def from_settings(cls, settings):
        dbparms = settings['LOCALMYSQLCONFIG']
        dbparms['cursorclass'] = pymysql.cursors.DictCursor
        conn = pymysql.connect(**dbparms)
        cursor = conn.cursor()
        return cls(conn, cursor)

    def process_item(self, item, spider):
        insert_sql, params = item.get_insert_sql()
        self.execute(insert_sql, params)
        return item

    def execute(self, sql, params):
        self.cursor.execute(sql, params)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def close_spider(self, spider):
        self.close()


class MongoPipline(object):

    conn = pymongo.MongoClient()

    def __init__(self):

        self.db = self.conn['lagou']

    def process_item(self, item, spider):
        if isinstance(item, LagouspiderItem):
            collection = self.db['lagoujob']
            self.insert(item, collection)
        else:
            collection = self.db['lagouinterviewcomment']
            self.insert(item, collection)

    def insert(self, item, collection):
        data = {}
        for key in item:
            data.setdefault(key, item[key])
        collection.insert_one(data)

    def closed_spider(self, spider):
        self.conn.close()

