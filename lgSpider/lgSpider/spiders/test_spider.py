# -*- coding:utf-8 -*-

import scrapy
from bs4 import BeautifulSoup


class tsSpride(scrapy.Spider):
    name = 'test' # 爬虫的唯一名字，在项目中爬虫名字一定不能重复

    # start_requests() 必须返回一个迭代的Request
    def start_requests(self):
        # 待爬取的URL列表
        urls = ['http://www.jianshu.com/',]
        # 模拟浏览器
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        for url in urls:
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    # 处理每个请求的下载响应
    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        titles = soup.find_all('a', 'title')
        for title in titles:
            print(title.string)