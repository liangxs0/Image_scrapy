import scrapy
import time
import sys
from ..items import ImageItem
from ..pipelines import ImagePipline
class ImageSpider(scrapy.Spider):
    name = 'images'
    allow_domains = ['https://2sbest.com']
    start_urls = ['https://2sbest.com']
    #https://2sbest.com/collections/cover-ups/products/solid-color-lacy-swimwear-cover-ups
    def parse(self, response):
        urls = response.xpath('//figure/figcaption/div/a[@class="title"]/text()')
        # 构造item对象
        Images_data = ImageItem()
        # sel = response.xpath('//a/div[@class="product_card__image-wrapper"]/img/@sizes')
        images = response.xpath('//ul[@id="ProductThumbs-product-template"]/li/a/@href')
        prices = response.xpath(
            '//div[@class="selection-wrapper price product-single__price-product-template"]/span[@class="money"]/text()')
        describe = response.xpath('//*[@id="tabs-1"]/table[1]/tbody//td[1]/text()')
        describe_data = response.xpath('//*[@id="tabs-1"]/table[1]/tbody//h6/span/text()')
        describe_dict = dict(zip(describe.extract(), describe_data.extract()))
        describe_Size_Inches_S = response.xpath('//*[@id="tabs-1"]/table[2]/tbody/tr[3]//h6/text()')
        describe_Size_Inches_M = response.xpath('//*[@id="tabs-1"]/table[2]/tbody/tr[4]//h6/text()')
        describe_Size_Inches_L = response.xpath('//*[@id="tabs-1"]/table[2]/tbody/tr[5]//h6/text()')
        describe_Size_Cen_S = response.xpath('//*[@id="tabs-1"]/table[3]/tbody/tr[3]//h6/text()')
        describe_Size_Cen_M = response.xpath('//*[@id="tabs-1"]/table[3]/tbody/tr[4]//h6/text()')
        describe_Size_Cen_L = response.xpath('//*[@id="tabs-1"]/table[3]/tbody/tr[5]//h6/text()')
        # 数据处理
        img_data = ['Image1', 'Image2', 'Image3', 'Image4', 'Image5', 'Image6', 'Image7']
        img = dict(zip(img_data, images.extract()))
        Images_data['img'] = img
        Images_data['prices'] = dict(zip(['Prices'], prices.extract()))
        Images_data['describe_dict'] = describe_dict
        Images_data['describe_Size_Inches_S'] = describe_Size_Inches_S.extract()
        Images_data['describe_Size_Inches_M'] = describe_Size_Inches_M.extract()
        Images_data['describe_Size_Inches_L'] = describe_Size_Inches_L.extract()
        Images_data['describe_Size_Cen_S'] = describe_Size_Cen_S.extract()
        Images_data['describe_Size_Cen_M'] = describe_Size_Cen_M.extract()
        Images_data['describe_Size_Cen_L'] = describe_Size_Cen_L.extract()
        yield Images_data

        for url in urls.extract():
            time.sleep(2)
            url = url.replace(' ','-')
            urls = 'https://2sbest.com/collections/cover-ups/products/' + url
            print(urls)
            yield scrapy.Request(urls,callback=self.parse)





