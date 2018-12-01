from scrapy.spiders import CrawlSpider,Rule
import scrapy
from newspaper import Article

class BaiDu(scrapy.Spider):
    name='bds'
    allowed_domains=[]
    start_urls=['https://www.baidu.com/']

    def parse(self, response):
        search=input('输入关键字：')
        url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&ch=1&tn=87048150_dg&wd=%E7%BE%8E%E9%A3%9F&rsv_pq=e29dd6dd00023d61&rsv_t=1218oxbCV3a8pGcl1NEa3Z809Z2%2BLxzAzMNNvajXcecAJR3d3iFJHX6PXWF0ZFr0Tac&rqlang=cn&rsv_enter=1&rsv_sug3=3&rsv_sug1=3&rsv_sug7=001'

        yield scrapy.Request(url,callback=self.parse1)

    def parse1(self,response):

        urls=response.xpath("//h3[@class='c-title']/a/@href")
        for url in urls:
            news=Article(url,language='zh')
            news.download()
            news.parse()
            print(news.title,news.keywords)
            'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&ch=1&tn=87048150_dg&wd=%E7%BE%8E%E9%A3%9F&rsv_pq=e29dd6dd00023d61&rsv_t=1218oxbCV3a8pGcl1NEa3Z809Z2%2BLxzAzMNNvajXcecAJR3d3iFJHX6PXWF0ZFr0Tac&rqlang=cn&rsv_enter=1&rsv_sug3=3&rsv_sug1=3&rsv_sug7=001'
