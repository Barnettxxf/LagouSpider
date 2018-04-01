# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy import FormRequest
from LagouSpider.items import LagouspiderItem
from LagouSpider.items import LagouInterviewItem

class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false&isSchoolJob=0']


    headers = {
        'Referer': 'https://www.lagou.com/jobs/list_python%E7%88%AC%E8%99%AB?labelWords=&fromSearch=true&suginput=',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/64.0.3282.167 Chrome/64.0.3282.167 Safari/537.36',
    }

    def start_requests(self):
        page = 1
        data = {
            'first': 'true',
            'pn': str(page),
            'kd': 'python爬虫',
        }
        for url in self.start_urls:
                yield FormRequest(url, headers=self.headers, formdata=data, callback=self.parse_job, meta={'page': page})

    def parse_job(self, response):
        item = LagouspiderItem()
        page = response.meta.get('page', '')
        page += 1
        print('page', page)
        data = {
            'first': 'true',
            'pn': str(page),
            'kd': 'python爬虫',
        }

        try:
            content = json.loads(response.text)['content']
        except KeyError:
            print(response.text)
            return
        results = content['positionResult']['result']
        total_count = content['positionResult']['totalCount']
        result_size = content['positionResult']['resultSize']
        if result_size == 0:
            return
        total_page = total_count // result_size + 1


        for result in results:
            item['companyid'] = result['companyId']
            item['industryfield'] = result['industryField']
            item['education'] = result['education']
            item['workyear'] = result['workYear']
            item['createtime'] = result['createTime']
            item['salary'] = result['salary']
            item['positionname'] = result['positionName']
            item['companysize'] = result['companySize']
            item['companyshortname'] = result['companyShortName']
            item['financestage'] = result['financeStage']
            item['companylablelist'] = ','.join(result['companyLabelList'])
            item['district'] = result['district']
            item['positionlables'] = ','.join(result['positionLables'])
            item['firsttype'] = result['firstType']
            item['secondtype'] = result['secondType']
            item['longitude'] = result['longitude']
            item['latitude'] = result['latitude']
            item['companyfullname'] = result['companyFullName']
            item['formatcreatetime'] = result['formatCreateTime']

            yield item

            interview_url = 'https://www.lagou.com/gongsi/interviewExperiences.html?companyId={}'.format(item['companyid'])
            interview_headers = self.headers.copy()
            interview_headers['Refer'] = 'https://www.lagou.com/gongsi/{}.html'.format(item['companyid'])
            yield scrapy.Request(url=interview_url, headers=interview_headers, callback=self.parse_interview,
                                 meta={'companyid': item['companyid'], 'page': 1, 'interview': True})

        if page > 2:
            data['first'] = 'false'
        if page > total_page:
            return
        yield FormRequest(url=response.url, formdata=data, headers=self.headers, callback=self.parse_job,
                          meta={'page': page}, dont_filter=True)

    def parse_interview(self, response):
        item = LagouInterviewItem()
        page = response.meta.get('page', '')
        companyid = response.meta.get('companyid', '')
        if page == 1:
            # content = response.xpath('//*[@id="interviewExperiencesData"]/text()').extract_first()
            content = response.css('#interviewExperiencesData::text').extract_first()
            content = json.loads(content)
            totalcount = int(content['totalCount'])
            pageSize = int(content['pageSize'])
            totalpage = totalcount // pageSize + 1
        else:
            content = response.text
            content = json.loads(content)
            content = content['content']['data']['page']
            totalpage = response.meta.get('totalpage', '')
        results = content['result']
        if len(results) == 0:
            return
        for result in results:
            item['id'] = result['id']
            item['userid'] = result['userId']
            item['myscore'] = result['myScore']
            item['describescore'] = result['describeScore']
            item['interviewscore'] = result['interviewerScore']
            item['companyscore'] = result['companyScore']
            item['comprehensivescore'] = result['comprehensiveScore']
            item['content'] = result['content']
            item['positionname'] = result['positionName']
            item['companyname'] = result['companyName']
            item['createtime'] = result['createTime']
            item['isinterview'] = result['isInterview']
            item['tagarray'] = ''.join(result['tagArray'])
            yield item

        page += 1
        if not (page <= totalpage):
            return
        data = {
            'companyId': str(companyid),
            'positionType': '',
            'pageSize': '10',
            'pageNo': str(page)
        }
        headers = {
            'Referer': 'https://www.lagou.com/gongsi/interviewExperiences.html?companyId=%s' % companyid,
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/64.0.3282.167 Chrome/64.0.3282.167 Safari/537.36',
        }
        url = 'https://www.lagou.com/gongsi/searchInterviewExperiences.json'
        yield FormRequest(url=url, formdata=data, headers=headers, callback=self.parse_interview,
                          meta={'page': page, 'totalpage': totalpage, 'companyid': companyid})


