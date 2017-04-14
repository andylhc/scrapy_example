# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
import subprocess, os
import pymongo

host = settings['MONGODB_HOST']
port = settings['MONGODB_PORT']
dbName = settings['MONGODB_DBNAME']
client = pymongo.MongoClient(host=host,port=port)   # 开启mongo的客户端
my_db = client[dbName]                              # 选择数据库


class Douban_book_pipeline(object):
	def __init__(self):
		self.collection = my_db['douban_book']                    # 选定集合
		self.collection.drop()

	def open_spider(self, spider):
		pass

	def process_item(self, item, spider):
		self.collection.insert(dict(item))
		return item

	# def close_spider(self, spider):
	#     self.post.close()


class Bosszhiping_query_pipeline(object):
	def __init__(self):
		self.collection = my_db['bosszhiping_query']              # 选定集合
		self.collection.drop()

	def open_spider(self, spider):
		pass

	def process_item(self, item, spider):
		self.collection.insert(dict(item))
		return item


class Lagou_query_pipeline(object):
	def __init__(self):
		self.collection=my_db['lagou_query']
		self.collection.drop()

	def open_spider(self, spider):
		pass

	def process_item(self, item, spider):
		self.collection.insert( dict(item) )
		return item

class Xici_ip_pipeline(object):
	def __init__(self):
		self.collection=my_db['xici_ip_all']
		self.collection.drop()

	def open_spider(self, spider):
		pass

	def process_item(self, item, spider):
		self.collection.insert(dict(item))
		return item

	def close_spider(self, spider):
		pass


class Qqvideo_movie_pipeline(object):
	def __init__(self):
		self.collection=my_db['qqvideo_movie']
		self.collection.drop()

	def open_spider(self, spider):
		pass

	def process_item(self, item, spider):
		self.collection.insert(dict(item))
		return item

	def close_spider(self, spider):
		pass



class Jiedaibao_file_pipeline(object):      #
	def __init__(self):
		self.collection=my_db['jiedaibao_full']
		self.collection.drop()
	def open_spider(self, spider):
		pass

	def process_item(self, item, spider):

		result_item=dict(item)
		file_url = result_item['file_urls'][0]
		home = os.getenv('HOME')

		temp_list =[]
		for i in self.collection.find( {"file_urls" : "%s" % file_url} ):
			temp_list.append(i)

		if not temp_list:
			self.collection.insert(  result_item  )

			if not os.path.exists( '%s/Social_Engineering/jiedaibao' %home  +  result_item['title'] ):
					os.makedirs( '%s/Social_Engineering/jiedaibao' %home +  result_item['title'] )

			os.chdir('%s/Social_Engineering/jiedaibao' %home +result_item['title'])

			file_name = str(item['file_results'])

			if os.path.exists(file_name):
				return  item

			count =0
			while count <= 5:

				try:
					out_put = subprocess.check_output("curl -vL -c - -o '%s' '%s' " %( file_name , result_item['file_urls'][0] ) , stderr=subprocess.STDOUT  , shell=True).decode('utf-8')
					if '200 OK' in out_put:
						print("this one is done")
						break

				except subprocess.CalledProcessError :
					pass

				finally:
					count += 1

		return item


	def close_spider(self, spider):
		pass















