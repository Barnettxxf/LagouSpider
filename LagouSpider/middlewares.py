# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import json
from scrapy import signals
from scrapy.downloadermiddlewares.cookies import CookiesMiddleware
import random
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from LagouSpider.utils.get_ip import GetIp
from twisted.internet.error import TimeoutError

t = GetIp()


class LagouspiderDownloaderMiddleware(object):
    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        return s

    def process_request(self, request, spider):
        return None

    def process_response(self, request, response, spider):

        interview = request.meta.get('interview', '')
        if interview:
            return response

        try:
            content = json.loads(response.text)
            if content['success'] is False:
                print('返回数据不对，重新请求')
                print('返回内容', content)
                return request
        except:
            print('返回数据不对，重新请求')
            print('返回内容', response)
            return request

        if response.status == 403:
            print('连接失败，重新请求')
            return request
        return response

    def process_exception(self, request, exception, spider):
        return request

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

    def spider_closed(self, spider):
        spider.logger.info('Spider closed: %s' % spider.name)


class RotateUserAgentMiddleware(UserAgentMiddleware):
    def __init__(self, user_agent=''):
        super(RotateUserAgentMiddleware, self).__init__(user_agent)
        self.user_agent = user_agent

    def process_request(self, request, spider):
        ua = random.choice(self.user_agent_list)
        print('User-Agent: ', ua)
        request.headers.setdefault('User-Agent', ua)

    # for more user agent strings,you can find it in http://www.useragentstring.com/pages/useragentstring.php
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]


class RandomProxyMiddleware(object):
    ip_list = t.ip_list

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        return s

    def process_request(self, request, spider):
        page = request.meta.get('page', '')
        if page % 3 == 0:
            ip, port = random.choice(self.ip_list)
            print('new_ip: ', 'https://' + ip + ':' + port)
            request.meta['proxy'] = 'https://' + ip + ':' + port

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

    def spider_closed(self, spider):
        spider.logger.info('Spider closed: %s' % spider.name)


class LagouCookiesMiddleware(object):
    cookies = {'user_trace_token': '20180226001828-5c601f0f-6537-44be-a9c9-c1c381f97c3f',
               '_ga': 'GA1.2.1250218167.1519575509',
               'LGUID': '20180226001829-83f7b1fb-1a47-11e8-917d-525400f775ce',
               'index_location_city': '%E6%B7%B1%E5%9C%B3',
               'showExpriedIndex': '1',
               'showExpriedCompanyHome': '1',
               'showExpriedMyPublish': '1',
               'ab_test_random_num': '0',
               'JSESSIONID': 'ABAAABAAAIAACBI9DA8C95B0EAE10083E158176261668F9',
               '_gid': 'GA1.2.1479758398.1522661344',
               'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1522228134,1522234524,1522388458,1522661344',
               'gate_login_token': '7fa964c836656a60799278ec13b106317c3137d0c8846134',
               'X_HTTP_TOKEN': '3dc49121699a69dc7f6f5deda3dcab57',
               'LG_LOGIN_USER_ID': '46f371ae76c5967a25dd77964ea0238579ea5ac81eeaa27e', '_putrc': '04201950329B43E0',
               'login': 'true', 'unick': '%E5%BE%90%E9%9B%84%E5%B3%B0', '_gat': '1',
               'LGSID': '20180403090637-42245fd1-36db-11e8-b6ea-5254005c3644', 'PRE_UTM': '', 'PRE_HOST': '',
               'PRE_SITE': '', 'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2F', 'hasDeliver': '16',
               'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1522688521',
               'LGRID': '20180403090653-4bb0e61f-36db-11e8-b6ea-5254005c3644', 'TG-TRACK-CODE': 'index_navigation',
               'SEARCH_ID': 'b4ccdc660a8c495d87d4d83f7cbabd62'}

    def process_request(self, request, spider):
        request.cookies = self.cookies

