# -*- coding": utf-8 -*-
import base64
import json
import requests

import scrapy
from scrapy import Request
from scrapy.http import FormRequest
from scrapy.shell import inspect_response


class Douban_login(scrapy.Spider):
	name = "douban_login"
	allowed_domains = ["douban.com"]

	def start_requests(self):
		yield Request("https://accounts.douban.com/login", callback=self.parse )


	def parse(self, response):
		captcha = response.xpath("//img[@id='captcha_image']/@src").extract()
		if len(captcha) > 0:
			print("此时有验证码")
			print(captcha)
			canshu = str(captcha).split('id=')[1].split('&')[0]
			print(canshu)

			r=requests.get(captcha[0], stream=True)
			picture = base64.b64encode( r.raw.read() ).decode('utf-8')  #读取文件内容，转换为base64编码


			url = 'http://ali-checkcode.showapi.com/checkcode'
			appcode = '16ccb8d34e124f9e9b74d972e42c17ad'

			headers={}
			headers['Authorization'] = 'APPCODE ' + appcode
			headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'

			bodys = {}
			bodys['img_base64'] = picture
			bodys['typeId'] = '3000'

			r=requests.post(url, headers=headers, data=bodys)
			answer = json.loads( r.text )['showapi_res_body']['Result']
			print ('验证码是 %s' % answer)



			data = {
				"source":"None",
				"form_email": "13661482706",
				"form_password": "douban123",
				"captcha-solution":str(answer),
				"captcha-id" : canshu,
				"redir": "https://www.douban.com",   # 登录后要返回的页面
				"login":"登录",
			}

		else:
			print("此时没有验证码")
			data = {
				"source":"None",
				"form_email":"13661482706",
				"form_password":"douban123",
				"redir":"https://www.douban.com",   # 登录后要返回的页面
				"login":"登录",
			}
		print("登录中。。。。。。")

		yield  FormRequest.from_response(response,  formdata=data, callback=self.next )


	def next(self,response):
		print("此时已经登录完成并爬取了个人中心的数据")
		title = response.xpath("/html/head/title/text()").extract()
		print(title[0])
		inspect_response(response, self)
