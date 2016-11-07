import scrapy

class amazonSpider(scrapy.Spider):
    name = "amazonwishlist"
    allowed_domains = ["amazon.com"]
    start_urls = [
        "https://www.amazon.com/gp/registry/wishlist/L7ANS47RVV91?ie=UTF8&disableNav=1&layout=standard-print",
    ]

    def parse(self, response):
        for sel in response:
            #name = sel.xpath('td/h5').extract()
            #author = response.xpath('td/span').re('<span> by.*')
            price = response.xpath('//table/tr/td/span/text()').re('.\d\d.\d\d')
            print price
