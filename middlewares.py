# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

class ScrapyExampleSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)



import random, requests, json
class Xici_ip_middleware(object):

    r=requests.get('http://www.xdaili.cn/ipagent/greatRecharge/getGreatIp?spiderId=b7178b0530eb4a1da1984b75ec8e5e4b&orderno=YZ20173294180nHnBqJ&returnType=2&count=20')
    print(r.text)   # 提取20个代理公网IP备用

    proxy_ip_list=[]
    ip_information=json.loads(r.text)["RESULT"]
    for every_ip in ip_information:
        ip = every_ip["ip"]
        port = every_ip["port"]
        proxy_ip = ip + ":" + port
        proxy_ip_list.append(proxy_ip)


    def process_request(self, request, spider):
        # Set the location of the proxy
        proxy_ip =   "https://"  +  random.choice(self.proxy_ip_list).strip()   # 如果不是HTTPS的协议的话，要用HTTP开头哦
        request.meta['proxy'] = proxy_ip
        print('+'*8, 'the Current ip address is', proxy_ip, '+'*8)









