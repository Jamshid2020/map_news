from django.core.management.base import BaseCommand
import scrapy
from scrapy.crawler import CrawlerProcess
from maps.models import News

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
        data=response.css('.single-layout__center')
        title = data.css('.single-header__title ::text').get()
        news_date = data.css('.date ::text').get()
        news_date = data.css('.date ::text').get()

        content=""
        for news in data.css('.single-content>p'):
            t = news.css("p ::text").get()
            if t:
                content =f'{content}{t}'
            # print(news.css('p ::text').get())
        print(title, news_date)
        # print(content)
        link=response.url
        print(link)
        model=News(title=title,
            link=link, web_site='kun.uz',
            news_date=news_date,
            content=content)
        model.save()
