from django.db import connection


def searchNews(request, limit):

    q = request.GET.get('q', '')
    if q == '':
        return []
    search_vector = f"document_vector @@ to_tsquery('{q}:*')"

    sql_txt =f"""SELECT "maps_news".title, link, maps_region.id,
    maps_region.name_region, koordinate_region
FROM "maps_news"
inner join maps_news_regions on maps_news.id = maps_news_regions.news_id
inner join maps_region on maps_news_regions.region_id  = maps_region.id
WHERE {search_vector}
ORDER BY "maps_news"."created" DESC
LIMIT %s"""

    with connection.cursor() as cursor:
        cursor.execute(sql_txt, [limit])
        rows = cursor.fetchall()
    return rows
