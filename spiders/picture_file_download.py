# -*- coding: utf-8 -*-

import scrapy
from scrapy.shell import inspect_response
from scrapy_example.items import Qqvideo_movie_item

class Qqvideo_movie(scrapy.Spider):
	name='qqvideo_movie'
	start_urls = ['http://v.qq.com/x/list/movie']
	num = 0
	#while(num<=4980):
	while(num<60):
		num = num + 30
		url = 'http://v.qq.com/x/list/movie?&offset=' + str(num)
		start_urls.append(url)

	def parse(self, response):
		for every_video in response.xpath('//li[@class="list_item"]'):
			video_title=every_video.xpath('./div[@class="figure_title_score"]/strong/a/text()').extract_first()
			video_image= 'http:' + every_video.xpath('./descendant::img[@r-lazyload]/@r-lazyload').extract_first()
			video_url=every_video.xpath('./div[@class="figure_title_score"]/strong/a/@href').extract_first()
			video_stars= every_video.xpath('//em[@class="score_l"]/text()').extract_first() + every_video.xpath('//em[@class="score_s"]/text()').extract_first()
			video_actors=every_video.xpath('//a[@_stat="videos-vert:actor"]/text()').extract()
			video_plays=every_video.xpath('//span[@class="num"]/text()').extract_first()

			item=Qqvideo_movie_item()
			item['title'] = video_title
			#item['actors']=video_actors
			item['plays']=video_plays
			item['stars']=video_stars

			item['url'] = video_url
			#item['comment']=
			temp =[]
			temp.append(video_url)

			item['image_urls'] = temp


			yield item



























































































from scrapy_example.items import Jiedaibao_file_item

class Jiedaibao_file(scrapy.Spider):
	name='jiedaibao_file'

	start_urls=[ 'https://www.jiedaibao10g.com/mm/', ]

	def parse(self, response):  # 分析首页元素
		first_path=response.xpath('//a[@style="font-size:16px;"]/@href').extract()
		for i in first_path:
			self.logger.info('A response from %s just arrived!', i)

			if '%E8%B4%B7' in i:
				yield scrapy.Request(response.urljoin(i), callback=self.parse_second)

	def parse_second(self, response):   # 进入个人-列表
		second_path=response.xpath('//a[@style="font-size:16px;"]/@href').extract()
		for i in second_path:
			yield scrapy.Request(response.urljoin(i), callback=self.parse_third)


	def parse_third(self, response): # 进入该人的 所有图片和视频
		all_href=response.xpath('//a')
		for i in all_href:
			if '.' in i.xpath('./text()').extract_first():
				yield scrapy.Request(response.urljoin( i.xpath('./@href').extract_first()  ), callback=self.parse_4th)


	def parse_4th(self, response):  # 进入 具体的某一个视频 或者 图片
		item=Jiedaibao_file_item()
		try:
			all_href=response.xpath('//a')

		except Exception:
			pass

		else:
			if response.xpath('//title/text()').extract_first():
				item['title']=response.xpath('//title/text()').extract_first().split(" -- ")[0].replace("/","-")

			for i in all_href:
				#self.logger.info('A response from %s just arrived!', response.url)

				try:
					if '下载地址(右键 目标另存为...)' in i.xpath('./text()').extract_first():
						pass
				except Exception:
					continue

				else:

					if '下载地址(右键 目标另存为...)' in i.xpath('./text()').extract_first():
						#self.logger.info('A response from %s just arrived!', response.url)
						file_urls = response.urljoin(   i.xpath('./@href').extract_first() )
						item['file_results'] = file_urls.split("/")[-1]
						temp=[]
						temp.append(file_urls)

						item['file_urls']= temp
						yield item

					elif '.' in i.xpath('./text()').extract_first() and '.db' not in i.xpath('./text()').extract_first():
						#self.logger.info('A response from %s just arrived!', response.url)
						file_urls = response.urljoin(   i.xpath('./@href').extract_first() )
						item['file_results'] = file_urls.split("/")[-1]
						temp=[]
						temp.append(file_urls)

						item['file_urls']=  temp
						yield item














































