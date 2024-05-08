"""
Scrapy kood magaziin.ee lehe jalanõude scrapimiseks.

Käima panemiseks sisestage see konsooli:
scrapy runspider -o scrapy_output_magaziin.json scrapy_scraper.py
"""
import scrapy
import time


class MagaziinSpider(scrapy.Spider):
    # Andmed veebilehele + header
    name = "magaziin_spider"
    url = "https://pood.magaziin.ee/product-category/jalatsid/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'
    }

    # Saadab requesti lehele
    def start_requests(self):
        yield scrapy.http.Request(self.url, headers=self.headers)

    # Alustab scrapimist
    def parse(self, response):
        # Produkti class
        product_selector = '.product'
        for jalatsid in response.css(product_selector):
            # Nime, hinna ja pildi source'i classid
            name_selector = '.woocommerce-loop-product__title ::text'
            price_selector = '.price .woocommerce-Price-amount bdi::text'
            image_selector = 'img ::attr(src)'
            yield {
                'Title': jalatsid.css(name_selector).extract_first(),
                'Price': jalatsid.css(price_selector).get().strip(),
                'Picture href': jalatsid.css(image_selector).extract_first()
            }
        # Järgmise lehe jaoks class
        next_page_selector = '.next.page-numbers::attr(href)'
        next_page = response.css(next_page_selector).extract_first()

        if next_page:
            # Et server ei tapaks meie sessiooni ära, on lisatud 5 sekundit paus.
            time.sleep(5)
            url = response.urljoin(next_page)
            yield scrapy.Request(url, self.parse, headers=self.headers)
