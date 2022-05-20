# -*- coding: utf-8 -*-
import scrapy
import json

class ZmljlSpider(scrapy.Spider):
    name = "zmljl"
    start_urls = [
        'http://jyhpt.tj.gov.cn/zmljl/list?resultDeptType=1&pageIndex=1&pageSize=10&_=1653013889574'
    ]

    def parse(self,response):
        sites = json.loads(response.body)
        # json.dump(sites,fp=open('E:/auto-tjcrawl-data/1.json','w'),ensure_ascii=False)
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljosnn)
