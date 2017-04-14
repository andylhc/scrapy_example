#! /usr/bin/env python
# -*- coding: utf-8 -*-
# class scrapy.http.Request(url[, callback, method='GET', headers, body, cookies, meta, encoding='utf-8', priority=0, dont_filter=False, errback])
# meta={'dont_merge_cookies': True}) 则避免与现有的Cookie合并

import scrapy
from scrapy_example.items import Douban_book_item

class Douban_book(scrapy.Spider):
	name = 'douban_book'  # 豆瓣图书 Top250 的爬取
	# allowed_domains = ["douban.com"]
	start_urls=[ 'https://book.douban.com/top250?start=0&filter=', ]

	def parse(self, response):
		self.logger.info('A response from %s just arrived!', response.url)  # 在终端输出相关日志打印

		item=Douban_book_item()
		for base_book_tag in response.xpath('//p[@class="ulfirst"] | //p[@class="ul"]'):

			item['author_name'] = base_book_tag.xpath('./following-sibling::table//p[@class="pl"]/text()').re_first(r'[^/]+'),

			item['book_name'] = base_book_tag.xpath('./following-sibling::table//a[@title]/text()').extract_first().strip(),

			item['record_people_number'] = base_book_tag.xpath('./following-sibling::table//span[@class="pl"]/text()').re_first(r'(\d+)'),

			item['record_value'] = base_book_tag.xpath('./following-sibling::table//span[@class="rating_nums"]/text()').extract_first(),

			item['comment'] = base_book_tag.xpath('./following-sibling::table//span[@class="inq"]/text()').extract_first(),

			yield item

		next_page_url=response.xpath('//div[@class="paginator"]/span[@class="next"]/a/@href').extract_first()
		if next_page_url:
			yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)



from scrapy_example.items import Bosszhiping_query_item
from urllib.parse import quote
class Bosszhiping_query(scrapy.Spider):
	name='bosszhiping_query'  # boss直聘 查询 'python 爬虫' 工作，工作地点：上海

	def start_requests(self):
		url_first='https://www.zhipin.com/'
		yield scrapy.Request(url=url_first, callback=self.query_requests)


	def query_requests(self, response):
		self.logger.info('A response from %s just arrived!', response.url)  # 在终端输出相关日志打印

		key_word =quote( getattr(self, 'key_word', 'python 爬虫') ) # 默认搜索python 爬虫
		url_query_first_part='https://www.zhipin.com/job_detail/'
		url_query_second_part='?'+'query=%s&scity=101020100&source=2' % key_word   # python%20%E7%88%AC%E8%99%AB  就是 python 爬虫 的URL转码
		url_query=url_query_first_part+url_query_second_part

		yield scrapy.Request(url=url_query, callback=self.parse)


	def parse(self, response):
		self.logger.info('A response from %s just arrived!', response.url)  # 在终端输出相关日志打印

		for href in response.xpath('//a[@data-index]/@href').extract():
			yield scrapy.Request(response.urljoin(href), callback=self.parse_detail)

		next_url =  response.xpath('//a[@class="next"]/@href').extract_first()
		yield scrapy.Request(url=response.urljoin(next_url) ,  callback=self.parse)


	def parse_detail(self, response):
		self.logger.info('A response from %s just arrived!', response.url)  # 在终端输出相关日志打印

		item=Bosszhiping_query_item()

		item['job_name']=response.xpath('//span[@class="badge"]/parent::div/text()').extract_first()

		item['company_name']=response.xpath('//a[@ka="job-detail-company"]/text()').extract_first()
		item['company_statues']=response.xpath('//div[@class="info-comapny"]/p/text()').extract()
		item['company_address']=response.xpath('//div[@class="location-address"]/text()').extract_first()

		item['pub_date']= response.xpath('//span[@class="time"]/text()').extract_first()
		item['job_describe']=response.xpath('//div[@class="job-sec"]/div[@class="text"]/text()').extract()
		item['salary']=response.xpath('//span[@class="badge"]/text()').extract_first()

		yield item






from scrapy.shell import inspect_response
from scrapy_example.items import Lagou_query_item
import json, requests, time
class Lagou_query(scrapy.Spider):
	name='lagou_query'  # 拉勾网 查询 python爬虫
	#allowed_domains = ["lagou.com"]

	def start_requests(self):

		html_number=[]
		def analyse_lagou_json():
			content = json.loads(r_post.text)
			for i in content["content"]["positionResult"]["result"]:
				html_number.append(i["positionId"])


		headers = {}

		headers['Cookie']='user_trace_token=20170327110809-575392c6db754b5ab8774b95a617f299; LGUID=20170327110810-9bd13b4e-129a-11e7-a353-525400f775ce; index_location_city=%E4%B8%8A%E6%B5%B7; JSESSIONID=1133841E953E28B223C558829D457178; _gat=1; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=index_search; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1490584087; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1490594779; _ga=GA1.2.1250345329.1490584091; LGSID=20170327140600-73425dc2-12b3-11e7-9570-5254005c3644; LGRID=20170327140619-7efe0c56-12b3-11e7-9570-5254005c3644; SEARCH_ID=86fbf909d0cc4b428b8ccd513365785a'
		# 拉勾网 的Cookie其实是永久有效的，即使使用一个过期的Cookie访问拉勾网，它也会在访问后，被拉勾网更新Cookie，之后访问都是携带拉勾网更新后的Cookie。这样的写法可以避开一系列麻烦的Javascript分析工作

		headers['Referer']='https://www.lagou.com/jobs/list_python%E7%88%AC%E8%99%AB?labelWords=sug&fromSearch=true&suginput=python'
		headers['Content-Type']='application/x-www-form-urlencoded; charset=UTF-8'
		headers['Origin']='https://www.lagou.com'
		headers['X-Anit-Forge-Code']='0'
		headers['X-Anit-Forge-Token']='None'
		headers['X-Requested-With']='XMLHttpRequest'


		url='https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false'

		key_word = getattr(self, 'key_word', 'python 爬虫')  # 默认搜索python 爬虫
		data1={ 'first': 'true', 'pn':1, 'kd': '%s' % key_word}
		r_post=requests.post(url=url, headers=headers,  data=data1)
		# 对于 模拟Javascript请求数据的行为 用requests库来做 比起scrapy会简洁又方便

		analyse_lagou_json()
		time.sleep(2)


		start_number=2
		while start_number<=30:
			data_after={'first': 'false', 'pn':'%s'%start_number, 'kd': '%s' %key_word}
			r_post=requests.post(url=url, headers=headers,  data=data_after)

			analyse_lagou_json()
			time.sleep(2)
			start_number+=1


		for i in html_number:
			url_job_detail='https://www.lagou.com/jobs/%s.html' % i
			yield scrapy.Request(url=url_job_detail, callback=self.parse)


	def parse(self, response):
		self.logger.info('A response from %s just arrived!', response.url)  # 在终端输出相关日志打印
		if 'forbidden.lagou.com' in response.url:
			#inspect_response(response, self)  # 进入shell界面，查看详细的报错情况 并 调试
			raise ValueError('we got 403 page')

		item = Lagou_query_item()

		item['job_name'] = response.xpath('//div[@class="job-name"]//span[@class="name"]/text()').extract_first()
		item['job_salary'] = response.xpath('//span[@class="ceil-salary"]/text()').extract_first()
		item['advantage'] = response.xpath('//dd[@class="job-advantage"]/p/text()').extract_first()
		item['description'] = response.xpath('//dd[@class="job_bt"]//p//text()').extract()
		item['address'] = response.xpath('//div[@class="work_addr"]//a[@href!="javascript:;"]/text()').extract()
		item['publish_stage'] = ''.join(response.xpath('//ul[@class="c_feature"]//li/text()').extract()).replace(' ','').replace('\n',' ').strip()
		item['publish_time'] =  response.xpath('//p[@class="publish_time"]/text()').extract_first()[:-8]
		item['publish_name'] = response.xpath('//div[@class="job-name"]//div[@class="company"]/text()').extract_first()

		yield item













