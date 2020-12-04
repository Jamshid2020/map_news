from django.core.management.base import BaseCommand
import scrapy
from scrapy.crawler import CrawlerProcess
from maps.models import News
from maps.models import Region
import re

regions_list = Region.objects.all()[:15]
class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        # pattern = '[^abc]'
        # test_string = 'Toshkent shahrida uy-joy sharoitlarini yaxshilashga muhtoj fuqarolarni hisobga olish tartibi o‘zgarishi mumkin '
        #
        # result = re.findall('Toshkent', test_string)
        # if result:
        #     print("OK ", result)
        # else:
        #     print("NO ", result)


        process = CrawlerProcess(settings={
            "FEEDS": {
                "items.json": {"format": "json"},
            },
        })

        process.crawl(KunSpider)
        process.start()


class KunSpider(scrapy.Spider):
    name = 'kunsiper'
    start_urls = ['https://kun.uz/uz/news/list']

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

        for region in regions_list:
            region_name = re.sub("'", '‘', region.name_region)
            check = re.findall(region_name, content)
            if check:
                model.regions.add(region)
                model.save()
