#! /usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
from scrapy_example.items import Xici_ip_item

class Xici_ip(scrapy.Spider):
	name = "xici_ip"
	#allowed_domains = ["xici.com"]

	start_urls = []

	for a in range(1,99):
		start_urls.append('http://www.xicidaili.com/nn/' + str(a))

	def parse(self, response):
		for every_Ip in response.xpath('//table/tr'):

			item = Xici_ip_item()

			item['ip'] = every_Ip.xpath('td[2]/text()').extract_first()
			item['port'] = every_Ip.xpath('td[3]/text()').extract_first()
			item['location_address'] = every_Ip.xpath('td[4]/a/text()').extract_first()
			item['HTTP_HTTPS'] = every_Ip.xpath('td[6]/text()').extract_first()

			item['connect_speed'] = every_Ip.xpath('td[7]/div/@title').extract_first()
			item['connect_time'] = every_Ip.xpath('td[8]/div/@title').extract_first()
			item['live_time'] = every_Ip.xpath('td[9]/text()').extract_first()
			item['last_check'] = every_Ip.xpath('td[10]/text()').extract_first()

			try:
				item['proxy_ip'] = item['ip']+":"+item['port']
			except TypeError :
				pass
			else:
				yield item






























