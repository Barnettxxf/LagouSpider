# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouspiderItem(scrapy.Item):
    companyid = scrapy.Field()
    industryfield = scrapy.Field()
    education = scrapy.Field()
    workyear = scrapy.Field()
    createtime = scrapy.Field()
    salary = scrapy.Field()
    positionname = scrapy.Field()
    companysize = scrapy.Field()
    companyshortname = scrapy.Field()
    financestage = scrapy.Field()
    companylablelist = scrapy.Field()
    district = scrapy.Field()
    positionlables = scrapy.Field()
    firsttype = scrapy.Field()
    secondtype = scrapy.Field()
    longitude = scrapy.Field()
    latitude = scrapy.Field()
    companyfullname = scrapy.Field()
    formatcreatetime = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
            INSERT INTO lagoujob (companyid,industryfield,education,workyear,createtime,salary,positionname,companysize,
            companyshortname,financestage,companylablelist,district,positionlables,firsttype,secondtype,longitude,
            latitude,companyfullname,formatcreatetime)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ON DUPLICATE KEY UPDATE financestage=VALUES (financestage), positionname=VALUES (positionname), district=VALUES (district),
            firsttype=VALUES (firsttype), secondtype=VALUES (secondtype), longitude=VALUES (longitude), latitude=VALUES (latitude);
        """
        params = (
            self['companyid'], self['industryfield'], self['education'], self['workyear'], self['createtime'], self['salary'],
            self['positionname'], self['companysize'], self['companyshortname'], self['financestage'], self['companylablelist'], self['district'],
            self['positionlables'], self['firsttype'], self['secondtype'], self['longitude'], self['latitude'], self['companyfullname'], self['formatcreatetime']
        )

        return insert_sql, params

class LagouInterviewItem(scrapy.Item):
    id = scrapy.Field()
    userid = scrapy.Field()
    myscore = scrapy.Field()
    describescore = scrapy.Field()
    interviewscore = scrapy.Field()
    companyscore = scrapy.Field()
    comprehensivescore = scrapy.Field()
    content = scrapy.Field()
    positionname = scrapy.Field()
    companyname = scrapy.Field()
    createtime = scrapy.Field()
    isinterview = scrapy.Field()
    tagarray = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
            INSERT INTO lagouinterviewcomment
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE content=VALUES (content), tagarray=VALUES (tagarray);
        """

        params = (
            self['id'], self['userid'], self['myscore'], self['describescore'], self['interviewscore'], self['companyscore'],
            self['comprehensivescore'], self['content'],
            self['positionname'], self['companyname'], self['createtime'], self['isinterview'], self['tagarray']
        )

        return insert_sql, params
