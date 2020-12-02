from django.core.management.base import BaseCommand
import scrapy
from scrapy.crawler import CrawlerProcess

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        process = CrawlerProcess(settings={
            "FEEDS": {
                "items.json": {"format": "json"},
            },
        })

        process.crawl(KunSpider)
        process.start()


class KunSpider(scrapy.Spider):
    name = 'kunsiper'
    start_urls = ['https://kun.uz/news/list']

    def parse(self, response):
        for data in response.css('.daily-block'):
            # title = data.css('.right-block>.news-title ::text').get()
            href = 'https://kun.uz'+data.css('a::attr("href")').get()
            #print(href)
            url = response.urljoin(href)
            yield scrapy.Request(url, callback = self.parse_dir_contents)
            #yield {'title': title.css('a ::text').get()}

    def parse_dir_contents(self, response):
        for data in response.css('.tags-ui__items'):
            tag_name = data.css('.tags-ui__item a::text').get()
            print(tag_name)
