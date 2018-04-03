# -*- coding:utf-8 -*-

from urllib.parse import unquote, quote

import time


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
    cookies = """
    user_trace_token=20180226001828-5c601f0f-6537-44be-a9c9-c1c381f97c3f; _ga=GA1.2.1250218167.1519575509; LGUID=20180226001829-83f7b1fb-1a47-11e8-917d-525400f775ce; index_location_city=%E6%B7%B1%E5%9C%B3; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; ab_test_random_num=0; JSESSIONID=ABAAABAAAIAACBI9DA8C95B0EAE10083E158176261668F9; _gid=GA1.2.1479758398.1522661344; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1522228134,1522234524,1522388458,1522661344; gate_login_token=""; X_HTTP_TOKEN=3dc49121699a69dc7f6f5deda3dcab57; LG_LOGIN_USER_ID=46f371ae76c5967a25dd77964ea0238579ea5ac81eeaa27e; _putrc=04201950329B43E0; login=true; unick=%E5%BE%90%E9%9B%84%E5%B3%B0; _gat=1; LGSID=20180403090637-42245fd1-36db-11e8-b6ea-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; hasDeliver=16; gate_login_token=7fa964c836656a60799278ec13b106317c3137d0c8846134; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1522688521; LGRID=20180403090653-4bb0e61f-36db-11e8-b6ea-5254005c3644; TG-TRACK-CODE=index_navigation; SEARCH_ID=b4ccdc660a8c495d87d4d83f7cbabd62
    """
    print(format_cookies(cookies))

    # city = '%E6%B7%B1%E5%9C%B3' # 深圳
    # print(unquote_city(city))