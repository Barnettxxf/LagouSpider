# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
#--------------------------------------------------------------------------------
headers = {
    # 'Accept':'application/json, text/javascript, */*; q=0.01',
    # 'Accept-Encoding':'gzip, deflate, br',
    # 'Accept-Language':'zh-CN,zh;q=0.9',
    # 'Cache-Control':'no-cache',
    # 'Connection':'keep-alive',
    # 'Content-Length':'43',
    # 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie':'user_trace_token=20180226001828-5c601f0f-6537-44be-a9c9-c1c381f97c3f; _ga=GA1.2.1250218167.1519575509; LGUID=20180226001829-83f7b1fb-1a47-11e8-917d-525400f775ce; index_location_city=%E6%B7%B1%E5%9C%B3; _gid=GA1.2.1223808493.1520424650; JSESSIONID=ABAAABAAAGFABEFB77BB3B7111D3D41FDC2C041AFBB54E0; hideSliderBanner20180305WithTopBannerC=1; X_HTTP_TOKEN=3dc49121699a69dc7f6f5deda3dcab57; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1520267233,1520267244,1520424650,1520513390; TG-TRACK-CODE=search_code; LGSID=20180308231330-42b742c5-22e3-11e8-b153-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_python%25E7%2588%25AC%25E8%2599%25AB%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fgongsi%2F917.html; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1520523033; LGRID=20180308233033-a4479bd9-22e5-11e8-a238-525400f775ce; SEARCH_ID=61534bc4e91f4f1e89eb9aff99c7dd99',
    # 'Host':'www.lagou.com',
    # 'Origin':'https://www.lagou.com',
    # 'Pragma':'no-cache',
    'Referer':'https://www.lagou.com/jobs/list_python%E7%88%AC%E8%99%AB?labelWords=&fromSearch=true&suginput=',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/64.0.3282.167 Chrome/64.0.3282.167 Safari/537.36',
    #'X-Anit-Forge-Code':'0',
    #'X-Anit-Forge-Token':'None',
    #'X-Requested-With':'XMLHttpRequest'
}

data = {
            'first': 'true',
            'pn': '5',
            'kd': 'python爬虫',
        }
url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false&isSchoolJob=0'

response = requests.post(url, data=data, headers=headers)
# with open('test.html', 'w', encoding='utf-8') as f:
#     f.write(response.text)
print(response.text)
#--------------------------------------------------------------------------------
# headers = {
#     'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/64.0.3282.167 Chrome/64.0.3282.167 Safari/537.36',
# }
#
# url = 'https://www.lagou.com/gongsi/interviewExperiences.html?companyId=107664'
# response = requests.get(url, headers=headers)
# # print(response.text)
# soup = BeautifulSoup(response.text)
# data = soup.select_one('#interviewExperiencesData').text
# print(data)
#--------------------------------------------------------------------------------
# data = {
#     'companyId': 107664,
#     'positionType': '',
#     'pageSize': 10,
#     'pageNo': 3
# }
# headers = {
#     'Referer': 'https://www.lagou.com/gongsi/interviewExperiences.html?companyId=107664',
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/64.0.3282.167 Chrome/64.0.3282.167 Safari/537.36',
# }
# url = 'https://www.lagou.com/gongsi/searchInterviewExperiences.json'
# response = requests.post(url, data=data, headers=headers)
# with open('test.json', 'w', encoding='utf-8') as f:
#     f.write(response.text)
#--------------------------------------------------------------------------------

