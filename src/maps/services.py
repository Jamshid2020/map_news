from django.db import connection


def searchNews(request, limit):
    sql_txt ="""SELECT "maps_news".title, link, maps_region.*
FROM "maps_news"
inner join maps_news_regions on maps_news.id = maps_news_regions.news_id
inner join maps_region on maps_news_regions.region_id  = maps_region.id
WHERE "maps_news"."document_vector" @@ to_tsquery('farg:*')
ORDER BY "maps_news"."created" DESC
LIMIT 10"""

    with connection.cursor() as cursor:
        cursor.execute(sql_txt)
        rows = cursor.fetchall()
    return rows
