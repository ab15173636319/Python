import scrapy
import json


class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["itcast.cn"]
    start_urls = ["https://www.itheima.com/teacher.html"]

    def parse(self, response):
        node= response.xpath('//*[@id="mCSB_1_container"]/ul/li/div')
        print(len(node))
        with open("teacher.html","w",encoding="utf-8") as f:
            f.write(response.text)