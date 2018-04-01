# LagouSpider
#### 简介

​	使用scrapy爬虫框架，使用IP代理池，随机UA等反反爬技术，请求Ajax数据来获取拉勾网python(深圳)职位信息。另外有一个项目[LagouRedis](https://github.com/Barnettxxf/LagouRedis)是用分布式爬虫爬取拉勾全网职位信息.

​	爬取包含两部分，招聘信息和公司面试评价。

​	招聘信息：companyid(公司ID), industryfield(公司ID), education(学历), workyear(工作经验), createtime(创建时间), salary(工资), positionname(职位名称), companysize(公司规模), companyshortname(公司简称), financestage(金融状态), companylablelist(公司标签), district(公司地址), positionlables(职位标签), firsttype(职位分类1), secondtype(职位分类2), longitude(经度), latitude(纬度), companyfullname(公司全名), formatcreatetime(发布时间)等十九个字段。

​	公司面试评价：id(评价ID), userid(用户ID), myscore(得分), describescore(描述得分), interviewscore(面试得分), companyscore(公司得分), comprehensivescore(总体得分), content(面试者评价), positionname(面试职位), companyname(公司名称), createtime(创建时间), isinterview(是否面试), tagarray(精简评价)等十三个字段。

​	

## Requirements

​	Ubuntu 17.10

​	python3 (anaconda3)

​	scrapy

​	pymysql

​	twisted

​	scrapyd

​	scrapyd-client

​	以上第三方库可以使用requirements直接安装，`pip install -r requirements`, 即可配置python环境需求，此外还需要用到MySQL数据库。



## 使用方法

​	方法同类似[LagouRedis](https://github.com/Barnettxxf/LagouRedis)，可以直接运行main.py文件来启动爬虫，或者使用scrapy命令行来启用爬虫，scrapyd部署没有写脚本实现，可以参考[Scrapyd官网](https://scrapyd.readthedocs.io/en/stable/)进行使用。



## Bug

​	如遇Bug请邮件我(1306513796@qq.com), 或者有任何改进意见也可邮件我~



## 说明

​	仅作学习交流使用

