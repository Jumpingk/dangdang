import scrapy
from scrapy import Request
from dangdang.items import DangdangItem
from tqdm import tqdm

class DdSpider(scrapy.Spider):
    name = 'dd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cid4003844.html']

    def parse(self, response):
        item = DangdangItem()
        item['title'] = response.xpath('//ul[@class="bigimg cloth_shoplist"]/li/p[@class="name"]/a/text()').extract()
        item['goods_link'] = response.xpath('//ul[@class="bigimg cloth_shoplist"]/li/a/@href').extract()
        item['shop_link'] = response.xpath('//ul[@class="bigimg cloth_shoplist"]/li/p[@class="link"]/a/@href').extract()
        item['comment_count'] = response.xpath('//ul[@class="bigimg cloth_shoplist"]/li/p[@class="star"]/a/text()').extract()
        item['price'] = response.xpath('//ul[@class="bigimg cloth_shoplist"]/li/p[@class="price"]/span/text()').extract()
        item['shop_name'] = response.xpath('//ul[@class="bigimg cloth_shoplist"]/li/p[@class="link"]/a/text()').extract()
        yield item
        for i in tqdm(range(2, 101), desc='Processing'):
            url = f'http://category.dangdang.com/pg{str(i)}-cid4003844.html'
            yield Request(url=url, callback=self.parse)




