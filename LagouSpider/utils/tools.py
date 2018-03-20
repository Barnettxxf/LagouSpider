# -*- coding:utf-8 -*-

from urllib.parse import unquote, quote

def format_cookies(cookie_str):
    cookie_list = cookie_str.split(';')
    container = {}
    for cookie in cookie_list:
        key = cookie.split('=')[0].strip()
        value = cookie.split('=')[1].strip()
        container[key] = value

    print('cookies length:', len(container))
    return container


def unquote_city(string, encoding=None):
    return unquote(string, encoding=encoding)


if __name__ == '__main__':
    # cookies = """
    # user_trace_token=20180226001828-5c601f0f-6537-44be-a9c9-c1c381f97c3f; _ga=GA1.2.1250218167.1519575509; LGUID=20180226001829-83f7b1fb-1a47-11e8-917d-525400f775ce; index_location_city=%E6%B7%B1%E5%9C%B3; JSESSIONID=ABAAABAAAIAACBI0F6208F8F96C4F25F0401ABC9F24BABC; hideSliderBanner20180305WithTopBannerC=1; _gid=GA1.2.2062001429.1521558973; LGSID=20180320231612-a050094e-2c51-11e8-914f-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1520935912,1521373019,1521377635,1521558978; TG-TRACK-CODE=index_search; SEARCH_ID=6cff551f6f6c41f49b8b6bfd8357e21f; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1521559018; LGRID=20180320231715-c5bfcfbf-2c51-11e8-914f-525400f775ce
    # """
    # print(format_cookies(cookies))

    city = '%E6%B7%B1%E5%9C%B3'
    print(unquote_city(city))