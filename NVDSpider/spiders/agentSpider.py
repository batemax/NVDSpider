import scrapy
import json

class agentSpider(scrapy.Spider):
    name = 'agentSpider'
    allowed_domains = ['httpbin.org']
    start_urls = ['https://httpbin.org/get?show_env=1']

    def parse(self, response):
        print(response.text)