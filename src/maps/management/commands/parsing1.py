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
    name = 'kunspider'
    start_urls = ['https://kun.uz/news/list']

    def parse(self, response):
        for data in response.css('.daily-block'):
            href = 'http://kun.uz'+data.css('a::attr("href")').get()
            # title = data.css('.right-block>.news-title ::text').get()
            url = response.urljoin(href)
            # dt = data.css('.news-date ::text').get()
            # print(dt + '-', title)

            # yield {'title': title.css('a ::text').get()}
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        for data in response.css('.tags-ui__items'):
            tag_name = data.css('.tags-ui__items a::text').get()
            print(tag_name)



        # for news-date in response.css('a.news-date'):
        #      yield response.follow(news-date, self.parse)
