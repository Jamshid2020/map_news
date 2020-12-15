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

def test(request):
    sql_txt ="""SELECT "maps_news".title, link, maps_region.id,
    maps_region.name_region, koordinate_region
    FROM "maps_news"
    inner join maps_news_regions on maps_news.id = maps_news_regions.news_id
    inner join maps_region on maps_news_regions.region_id  = maps_region.id
    ORDER BY "maps_news"."created" DESC"""
    with connection.cursor() as cursor:
        cursor.execute(sql_txt)
        rows = cursor.fetchall()
    return rows
def search_by_group(request):
    q = request.GET.get('q', '')
    if q == '':
        return []
    search_vector = f"document_vector @@ to_tsquery('{q}:*')"

    sql_srch = f"""SELECT "maps_news".id, "maps_news".title,array_to_json(array_agg(row_to_json(maps_region) ) ) as regions
    FROM "maps_news"
    inner join maps_news_regions on maps_news.id = maps_news_regions.news_id
    inner join maps_region on maps_news_regions.region_id  = maps_region.id
    WHERE {search_vector}
    group by "maps_news".id,"maps_news".title
    LIMIT 10"""

    with connection.cursor() as cursor:
        cursor.execute(sql_srch)
        rows = cursor.fetchall()
    return rows
