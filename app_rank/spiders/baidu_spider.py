# -*- coding: utf-8 -*-

import re
import scrapy

from app_rank.items import BaiduappItem

class BaiduSoftSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ["baidu.com"]
    DOMAIN_URL = "http://shouji.baidu.com/"
    start_urls = ['http://shouji.baidu.com/rank/top/']
    page_base_url = 'http://shouji.baidu.com/rank/top/'


    def parse(self, response):
        # self.log(response.url)

        page_urls = response.selector.css('.pager').xpath('.//ul/li/a/@href').extract()
        for url in page_urls:
            _url = self.page_base_url + url.lstrip('/')
            yield scrapy.Request(_url, callback=self.parse)

        detail_pages = response.selector.xpath('//*[@id="ranking"]').css('.app-box').xpath('.//@href').extract()
        for url in detail_pages:
            _url = self.DOMAIN_URL + url.lstrip('/')
            yield scrapy.Request(_url, callback=self.parse_detail)


    def parse_detail(self, response):
        self.log(response.url)

        item = BaiduappItem()
        item['url'] = response.url
        item['name'] = response.selector.css('.app-name').xpath('.//span/text()').extract()[0].strip()
        num, unit = response.selector.css('.download-num').re(r':\s*(\d+\.?\d+)(.*?)</span')
        num_float = float(num)
        if unit.strip() == u'亿':
            item['download_num'] = num_float * 100000000
        elif unit.strip() == u'万':
            item['download_num'] = num_float * 10000
        elif unit.strip() == u'千':
            item['download_num'] = num_float * 1000
        elif unit.strip() == u'百':
            item['download_num'] = num_float * 100
        else:
            item['download_num'] = ''.join(num, unit)

        item['size'] = response.selector.css('.size').re(r':(.*?)</span>')[0].strip()
        item['version'] = response.selector.css('.version').re(r':(.*?)</span>')[0].strip()

        yield item
