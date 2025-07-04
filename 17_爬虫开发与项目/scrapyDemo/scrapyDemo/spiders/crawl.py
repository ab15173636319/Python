import scrapy


class crawl(scrapy.Spider):
    name = "crawl"

    def start_requests(self):
        # 设置需要爬取的地址
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
        ]

        # 获取所有地址
        for url in urls:
            # 发送网络请求
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # 获取页数
        page = response.url.split("/")[-2]
        # 根据页数设置文件名称
        filename = f"quotes-{page}.html"
        # 保存文件
        with open(filename, "w", encoding="utf-8") as f:
            f.write(response.text, indent=2)

        print(f"文件{filename}已保存")


