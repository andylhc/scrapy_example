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
* 爬取这250本书的：书名，作者名，简介，评分 并记入Mongo数据库
* 具有自动翻页的功能  

>PS：该网页没有任何防爬虫机制，信息量也适合，HTML页面较规范，很适合作为爬虫入门的素材练习
   
<br>
**boss直聘**  
爬取 boss直聘 所有有关 <MARK>python爬虫</MARK> 的职位信息

>* 初始URL为：<https://www.zhipin.com/> 以获取必要的登陆Cookie
>* 爬取URL为：<https://www.zhipin.com/job_detail/?query=python+%E7%88%AC%E8%99%AB&scity=101020100&source=2> 以及该页面下工作详情的子页面
>* 具有自动翻页功能，能记录来自第一次访问主页的Cookie，并将Cookie用在访问其他子页面上

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















