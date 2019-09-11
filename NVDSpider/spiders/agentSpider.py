import scrapy
import json

class agentSpider(scrapy.Spider):
    name = 'agentSpider'
    allowed_domains = ['httpbin.org']
    start_urls = ['https://httpbin.org/get?show_env=1']
    num = 0

    def parse(self, response):
        if self.num < 20:
            self.num = self.num + 1
            print(response.text)
            yield scrapy.Request(self.start_urls[0])
        else:
            print(response.text)
            return scrapy.Request(self.start_urls[0])