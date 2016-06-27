# -*- coding: utf-8 -*-

import re
import scrapy

from app_rank.items import AppleAppItem

class AppleAppCnFree(scrapy.Spider):
    name = 'apple_cn_free'
    allowed_domains = ["apple.com"]
    data_source = 'apple_cn_free'
    start_urls = ['http://www.apple.com/cn/itunes/charts/free-apps/']


    def parse(self, response):
        self.log(response.url)

        main_xpath = response.selector.xpath('//*[@id="main"]')

        apps_sel = main_xpath.css('.section').css('.apps').css('.grid').xpath('.//ul/li')
        for sel in apps_sel:
            item = AppleAppItem()
            item['data_source'] = self.data_source
            item['order'] = sel.xpath('.//strong/text()').re(r'\d+')[0]
            item['image_url'] = sel.xpath('./a/img/@src').extract()[0]
            item['download_url'] = sel.xpath('./h3/a/@href').extract()[0]
            item['name'] = sel.xpath('./h3/a/text()').extract()[0]
            item['app_type'] = sel.xpath('./h4/a/text()').extract()[0]
            yield item


class AppleAppCnPaid(scrapy.Spider):
    name = 'apple_cn_paid'
    allowed_domains = ["apple.com"]
    data_source = 'apple_cn_paid'
    start_urls = ['http://www.apple.com/cn/itunes/charts/paid-apps/']


    def parse(self, response):
        self.log(response.url)

        main_xpath = response.selector.xpath('//*[@id="main"]')

        apps_sel = main_xpath.css('.section').css('.apps').css('.grid').xpath('.//ul/li')
        for sel in apps_sel:
            item = AppleAppItem()
            item['data_source'] = self.data_source
            item['order'] = sel.xpath('.//strong/text()').re(r'\d+')[0]
            item['image_url'] = sel.xpath('./a/img/@src').extract()[0]
            item['download_url'] = sel.xpath('./h3/a/@href').extract()[0]
            item['name'] = sel.xpath('./h3/a/text()').extract()[0]
            item['app_type'] = sel.xpath('./h4/a/text()').extract()[0]
            yield item


class AppleAppEnFree(scrapy.Spider):
    name = 'apple_en_free'
    allowed_domains = ["apple.com"]
    data_source = 'apple_en_free'
    start_urls = ['http://www.apple.com/itunes/charts/free-apps/']


    def parse(self, response):
        self.log(response.url)

        main_xpath = response.selector.xpath('//*[@id="main"]')

        apps_sel = main_xpath.css('.section').css('.apps').css('.chart-grid').xpath('.//ul/li')
        for sel in apps_sel:
            item = AppleAppItem()
            item['data_source'] = self.data_source
            item['order'] = sel.xpath('.//strong/text()').re(r'\d+')[0]
            item['image_url'] = sel.xpath('./a/img/@src').extract()[0]
            item['download_url'] = sel.xpath('./h3/a/@href').extract()[0]
            item['name'] = sel.xpath('./h3/a/text()').extract()[0]
            item['app_type'] = sel.xpath('./h4/a/text()').extract()[0]
            yield item


class AppleAppEnPaid(scrapy.Spider):
    name = 'apple_en_paid'
    allowed_domains = ["apple.com"]
    data_source = 'apple_en_paid'
    start_urls = ['http://www.apple.com/itunes/charts/paid-apps/']


    def parse(self, response):
        self.log(response.url)

        main_xpath = response.selector.xpath('//*[@id="main"]')

        apps_sel = main_xpath.css('.section').css('.apps').css('.chart-grid').xpath('.//ul/li')
        for sel in apps_sel:
            item = AppleAppItem()
            item['data_source'] = self.data_source
            item['order'] = sel.xpath('.//strong/text()').re(r'\d+')[0]
            item['image_url'] = sel.xpath('./a/img/@src').extract()[0]
            item['download_url'] = sel.xpath('./h3/a/@href').extract()[0]
            item['name'] = sel.xpath('./h3/a/text()').extract()[0]
            item['app_type'] = sel.xpath('./h4/a/text()').extract()[0]
            yield item
