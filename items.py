# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags

class Douban_book_item(scrapy.Item):
    # item 的元素全部都是列表
    author_name = scrapy.Field()
    book_name = scrapy.Field()
    comment = scrapy.Field()
    record_people_number = scrapy.Field()
    record_value = scrapy.Field()
    debug_thing=scrapy.Field()

class Bosszhiping_query_item(scrapy.Item):
    company_name=scrapy.Field()
    company_statues=scrapy.Field()
    company_address=scrapy.Field()

    pub_date=scrapy.Field()
    salary=scrapy.Field()
    job_name=scrapy.Field()
    job_describe=scrapy.Field()
    # job_describe= scrapy.Field(
    #     input_processor=MapCompose(remove_tags),
    #     output_processor=Join(' '),   # 将所有的字符都 拼接在一起  # Join('<br>') == '<br>'.join(<接收到的值>)
    # )


class Lagou_query_item(scrapy.Item):
    job_name=scrapy.Field()
    job_salary=scrapy.Field()
    advantage=scrapy.Field()
    description=scrapy.Field()
    # description = scrapy.Field(
    #     input_processor=MapCompose(remove_tags),
    #     output_processor=Join(' '),   # 将所有的字符都 拼接在一起  # Join('<br>') == '<br>'.join(<接收到的值>)
    # )

    address=scrapy.Field()
    publish_stage=scrapy.Field()
    publish_time=scrapy.Field()
    publish_name=scrapy.Field()


class Xici_ip_item(scrapy.Item):
    ip=scrapy.Field()
    port=scrapy.Field()
    location_address=scrapy.Field()
    HTTP_HTTPS=scrapy.Field()

    connect_speed=scrapy.Field()
    connect_time=scrapy.Field()
    live_time=scrapy.Field()
    last_check=scrapy.Field()

    proxy_ip=scrapy.Field()

class Qqvideo_movie_item(scrapy.Item):
    title = scrapy.Field()
    plays = scrapy.Field()
    stars = scrapy.Field()
    actors = scrapy.Field()
    url=scrapy.Field()

    image_urls=scrapy.Field()
    image_result=scrapy.Field()
    #comment = scrapy.Field()


class Jiedaibao_file_item(scrapy.Item):
    title = scrapy.Field()

    file_urls = scrapy.Field()
    file_results = scrapy.Field()






























