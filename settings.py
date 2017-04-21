# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_example project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_example'

SPIDER_MODULES = ['scrapy_example.spiders']
NEWSPIDER_MODULE = 'scrapy_example.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_example (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'scrapy_test'     # 数据库名


# Obey robots.txt rules
ROBOTSTXT_OBEY = False  # 无视 robots.txt 文件，爬取所有页面
FEED_EXPORT_ENCODING = 'utf-8'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

DOWNLOAD_DELAY = 3

# The download delay setting will honor only one of:

#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2,ja;q=0.2',
   'Connection' : 'keep-alive',
}


# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scrapy_example.middlewares.ScrapyExampleSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html


DOWNLOADER_MIDDLEWARES = {
   # 'scrapy_example.middlewares.Xici_ip_middleware': 543,          # 讯代理的代理IP使用，如果要挂代理IP的话，开启该中间件
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html


ITEM_PIPELINES = {  # 数值小的先运行， 数值大的后运行
    # 'scrapy_example.pipelines.Douban_book_pipeline': 300,         # 如果要爬取 豆瓣图书 的信息，使用这个pipeline
    # 'scrapy_example.pipelines.Bosszhiping_query_pipeline': 300,   # 如果要爬取 boss直聘 的信息，使用这个pipeline
    # 'scrapy_example.pipelines.Xici_ip_pipeline' : 300,
    # 'scrapy_example.pipelines.Lagou_query_pipeline' : 300,        # 如果要爬取 拉勾网 的信息，使用这个pipeline

    # 'scrapy_example.pipelines.Jiedaibao_file_pipeline' : 300,
    # 'scrapy_example.pipelines.Qqvideo_movie_pipeline' : 300,


  # 'scrapy.contrib.pipeline.images.ImagesPipeline': 1,   # 下载待爬取页面的图片
  # 'scrapy.pipelines.files.FilesPipeline': 1,            # 下载待爬取页面除图片外的小文件，文件大小推荐小于32MB，下载时间小于180秒

}

# IMAGES_STORE = 'pic/'             # 下载图片要使用的3个参数
# IMAGES_URLS_FIELD = 'image_urls'
# IMAGES_RESULT_FIELD = 'image_results'


# FILES_STORE = 'file/'             # 下载文件要使用的3个参数
# FILES_URLS_FIELD  = 'file_urls'
# FILES_RESULT_FIELD = 'file_results'



# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
