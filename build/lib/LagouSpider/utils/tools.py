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
    user_trace_token=20180226001828-5c601f0f-6537-44be-a9c9-c1c381f97c3f; _ga=GA1.2.1250218167.1519575509; LGUID=20180226001829-83f7b1fb-1a47-11e8-917d-525400f775ce; index_location_city=%E6%B7%B1%E5%9C%B3; _gid=GA1.2.2062001429.1521558973; hideSliderBanner20180305WithTopBannerC=1; JSESSIONID=ABAAABAAAIAACBI41D253C29C1CCFBCFC565C3ADACD2917; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1521558978,1521598449,1521612039,1521622382; TG-TRACK-CODE=index_navigation; X_HTTP_TOKEN=3dc49121699a69dc7f6f5deda3dcab57; LGSID=20180321221313-fe3263bc-2d11-11e8-b56c-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fpassport.lagou.com%2Flogin%2Flogin.html%3Fmsg%3Dvalidation%26uStatus%3D2%26clientIp%3D183.53.66.197; SEARCH_ID=9c40e391eb7b4c379e4f104799c6b4ca; _putrc=04201950329B43E0; login=true; unick=%E5%BE%90%E9%9B%84%E5%B3%B0; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=8; gate_login_token=d4ad590e51863daf7ee4b04feb97b60ba07f5fd778a2516a; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1521642759; LGRID=20180321223239-b4e9d754-2d14-11e8-9348-525400f775ce
    """
    print(format_cookies(cookies))

    # city = '%E6%B7%B1%E5%9C%B3' # 深圳
    # print(unquote_city(city))