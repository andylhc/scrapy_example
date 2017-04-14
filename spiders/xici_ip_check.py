#! /usr/bin/env python
# -*- coding: utf-8 -*-

import threading, pymongo, requests
client = pymongo.MongoClient("127.0.0.1",27017)
db = client.scrapy_test
collection_full = db.xici_ip_all
collection_available = db.xici_ip_available


class myThread (threading.Thread):
	def __init__(self, thread_id, thread_name, proxy_ip ):
		threading.Thread.__init__(self)
		self.threadID = thread_id
		self.thread_name = thread_name
		self.proxy_ip=proxy_ip
	def run(self):
		check_ip_available(self.thread_name, self.proxy_ip)


def check_ip_available(threadName, proxy_ip):
	url = 'http://%s/qiniu_do_not_delete.gif' % proxy_ip
	headers={'Host' : 'wst.cdn.clouddn.com'}

	try :
		r = requests.get(url, headers=headers, timeout=20)
	except Exception:
		pass
	else:
		if r.status_code == '200' or r.status_code==200:
			available_ip=collection_full.find( {'proxy_ip' : '%s' % proxy_ip} )
			print("\"",proxy_ip,"\",")
			collection_available.insert(available_ip[0])


def multiple_main_run():
	collection_available.drop()

	proxy_ip_list=[]
	for i in collection_full.find():
		proxy_ip_list.append(i['proxy_ip'])

	thread_list=[]
	id_count=0
	for i in proxy_ip_list:
		thread_list.append(myThread(id_count, "Thread-%s" % id_count, i))
		id_count+=1

	for i in thread_list:
		i.start()

	for i in thread_list:
		i.join()

	print("退出主线程")


if __name__ == '__main__':
	multiple_main_run()

































