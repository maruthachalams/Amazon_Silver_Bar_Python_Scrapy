""" 
Developer Name: MARUTHACHALAM S
Project Title: Silver Bar 1 kg 999.9 Purity Search in Amazon Website using Python with Scrapy Framework
Date: 28.01.2025
Version 1

 """ 

import scrapy


class AmazonSilverScrapSpider(scrapy.Spider):
    name = "amazon_silver_scrap"
    allowed_domains = ["www.amazon.in"]
    start_urls = ["https://www.amazon.in/s?k=silver+bar+1kg+999.9+purity&crid=2SOL10HL7K7H&sprefix=silver+bar+1kg+999.9+purity%2Caps%2C450&ref=nb_sb_noss_1"]

    def parse(self, response):
        for silverbar in response.xpath('//div[@data-component-type="s-search-result"]'):
            item = {
                'company_name': (silverbar.xpath(".//h2//span[@class='a-size-base-plus a-color-base']/text()").get() or '').strip(),
                'product_title': (silverbar.xpath('.//h2[@aria-label]//span/text()').get() or '').strip(),
                'ratings': (silverbar.xpath('.//span[@class="a-icon-alt"]/text()').get() or '').strip(),
                'mrp': (silverbar.xpath('.//span[@class="a-price a-text-price"]/span[@class="a-offscreen"]/text()').get() or '').strip(),
                'final_price': (silverbar.xpath('.//span[@class="a-price-whole"]/text()').get() or '').strip(),
            }
            if "1 kg" in item['product_title']:
                if "Silver" in item['product_title']:
                    if "Bar" in item['product_title']:
                        self.log(f"Scraped item: {item}")
                        yield item
            elif "1 Kg" in item['product_title']:
                if "Silver" in item['product_title']:
                    if "Bar" in item['product_title']:
                        self.log(f"Scraped item: {item}")
                        yield item
               

        next_page = response.xpath('//li[@class="s-list-item-margin-right-adjustment"]//span[@class="a-list-item"]//a[@href]').get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            self.log(f"Following next page link: {next_page_url}")
            yield scrapy.Request(next_page_url, callback=self.parse)
