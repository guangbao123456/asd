from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
import re
class RenMin(CrawlSpider):
    name='ren'
    allowed_domains=[]
    start_urls=['http://edu.people.com.cn/']
    rules = (
        Rule(LinkExtractor(allow='http://edu.people.com.cn/n1/2018/\d{4}/.*.html',restrict_css='ul a'),callback='parse_item'),
        Rule(LinkExtractor(allow='http://edu.people.com.cn/n1/2018/\d{4}/.*.html',),follow=True),
    )
    def parse_item(self, response):
        url=response.url
        s=Selector(response)
        title=s.xpath("//div/h1/text()").extract()
        keywords=s.xpath("//meta[@name='keywords']/@content").extract()
        daodu=s.xpath("//meta[@name='description']/@content").extract()
        print(title,keywords,daodu)
        shijian=s.xpath("//div[@class='box01']/div[@class='fl']/text()").extract()
        laiyuan=s.xpath("//div[@class='box01']/div[@class='fl']/a/text()").extract()
        author=s.xpath("//div[@class='edit clearfix']/text()").extract()
        tuurl=s.xpath("//div[@id='picG']/div[@class='box_pic']//a/img/@src").extract()
        content=s.xpath("//div[@id='rwb_zw']/p/text()").extract()

