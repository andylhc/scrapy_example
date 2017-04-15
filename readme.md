# Scrapy爬虫框架的 简单实例 和 相关代码
***

## 简介
本人现在正在找工作，该代码是写给HR以及需要找爬虫程序猿的部门经理看的，



<br>

## 代码介绍

主代码是在：[spiders/real_example.py](https://github.com/zhangyunchuan/scrapy_example/blob/master/spiders/real_example.py "real_example.py 里面有 豆瓣网，boss直聘，拉勾网 爬虫代码") 里面  
real_example.py 里面包含了三个爬虫，分别是用来爬取 **豆瓣网**，**boss直聘**，**拉勾网**  
<br>
<br>
**豆瓣网**  
爬取 豆瓣网 的Top250的图书信息  

>* 初始URL为：<https://book.douban.com/top250>
>* 爬取这250本书的：书名，作者名，简介，评分 并记入Mongo数据库
>* 具有自动翻页的功能  
>
>PS：该网页没有任何防爬虫机制，信息量也适合，HTML页面较规范，很适合作为爬虫入门的素材练习
   
<br>

**boss直聘**  
爬取 boss直聘 所有有关 <MARK>python爬虫</MARK> 的职位信息

>* 初始URL为：<https://www.zhipin.com/> 以获取必要的登陆Cookie
>* 爬取URL为：<https://www.zhipin.com/job_detail/?query=python+%E7%88%AC%E8%99%AB&scity=101020100&source=2> 以及该页面下工作详情的子页面
>* 具有自动翻页功能，能记录来自第一次访问主页的Cookie，并将Cookie用在访问其他子页面上
>
>PS：  
>困难：该网页使用了 *禁用IP的防爬虫策略*   
>解决：所以我在中间件中写的`Xici_ip_middleware`类就是用来使用多个代理IP以突破这种防爬虫策略，代理IP是从 <http://www.xdaili.cn/> 买的

<br>

**拉勾网**  
爬取 拉勾网 所有有关 <MARK>python爬虫</MARK> 的职位信息

>* 初始URL为：<https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false> 请求方法必须是<MARK>POST请求</MARK>，并带有相关Cookies 和 该网站需要的其他请求头 
>* 爬取URL为：<https://www.lagou.com/jobs/.html> 要带Cookies访问
>* 具有自动翻页功能
>
>PS：   
> 
>* 困难：该网页使用了 *Javascript动态加载网页内容的防爬虫策略*，所以[查询页面](https://www.lagou.com/jobs/list_python%20%E7%88%AC%E8%99%AB?labelWords=&fromSearch=true&suginput=)虽然能看到职位内容，但是html源码中没有相关的职位内容。  
>* 解决：分析xhr文件得知是用Javascript请求了数据库，获得的JSON文件来动态填充来原始HTML页面。于是用python模拟向数据库发起请求，并根据获得的JSON文件，直接抓取包含职位详情的页面
	
	
	
<br>

## 需求
1. 该代码为python3格式
2. 需要安装python3, scrapy框架，requests库，
3. 推荐安装 Mongo数据库


<br> 

## 操作方法  
爬取 **豆瓣网**

1. 开启 settings.py 文件中 豆瓣网 的pipeline，如下图：  
   将红框中那一行的注释去掉即可
   ![豆瓣网配置](http://www.samael.tk/douban_settings.png)
2. 在 scrapy_example 的目录下输入：`scrapy crawl douban_book`

PS: 爬取的信息默认存储在 本地 mongo数据库 的 scrapy_test 数据库中  
爬取信息如下：  
![豆瓣_mongo](http://www.samael.tk/douban_book_output.png)

<br>

爬取 **boss直聘**

1. 开启 settings.py 文件中 boss直聘网 的pipeline，如下图：   
   将红框中那一行的注释去掉即可
   ![boss直聘配置](http://www.samael.tk/boss_zhiping_settings.png)
2. 在 scrapy_example 的目录下输入：`scrapy crawl bosszhiping_query`  
	默认是搜索`python 爬虫`相关的职位信息，如果需要搜索其他职位信息，可以输入 `scrapy crawl bosszhiping_query -a key_word=<关键词> `  
	例如要搜索`前端`相关的职位信息，则输入`scrapy crawl bosszhiping_query -a key_word=前端 `

PS:  pipeline的配置是把boss直聘网中爬取的信息存入mongo数据库，middlewares的配置是开启代理IP以防止本地IP被反爬虫机制ban  
爬取信息如下：  
![boss_mongo](http://www.samael.tk/boss_zhiping_output.png)

<br> 



爬取 **拉勾网**

1. 开启 settings.py 文件中 拉勾网 的pipeline，如下图：
   将红框中那一行的注释去掉即可
   ![拉勾1](http://www.samael.tk/lagou_settings1.png)
   ![拉勾2](http://www.samael.tk/lagou_settings2.png)
2. 在 scrapy_example 的目录下输入：`scrapy crawl lagou_query`
	默认是搜索`python 爬虫`相关的职位信息，如果需要搜索其他职位信息，可以输入 `scrapy crawl lagou_query -a key_word=<关键词> `  
	例如要搜索`前端`相关的职位信息，则输入`scrapy crawl lagou_query -a key_word=前端 `

PS: 爬虫爬取的时间会比较长，因为我开启了6秒的延迟。也可以关闭延迟时间，使用  boss直聘 中的代理IP中间件来爬取，以提高效率  
爬取信息如下：  
![lagou_output](http://www.samael.tk/lagou_output.png)






