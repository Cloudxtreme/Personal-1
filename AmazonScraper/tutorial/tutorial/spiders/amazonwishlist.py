import scrapy

class amazonSpider(scrapy.Spider):
    name = "amazonwishlist"
    allowed_domains = ["amazon.com"]
    start_urls = [
        "https://www.amazon.com/gp/registry/wishlist/L7ANS47RVV91?ie=UTF8&disableNav=1&layout=standard-print",
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
