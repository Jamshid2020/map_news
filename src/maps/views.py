from django.shortcuts import render
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from .models import News
from .services import searchNews

def index(request):


    # q = request.GET.get('q', '')
    # search_query = SearchQuery(f"{q}:*", search_type='raw')

    # .annotate(rank=SearchRank(vector, query)).
    # model = News.objects.filter(document_vector=search_query).order_by('-created')[:10]

    # for data in model:
    #     print(data.title)


    result = searchNews(request, 10)
    for title, link, region_id, region_name, coordinates in result:
        print(region_name,' --- ', coordinates)
        print('***************************')


    return render(request,'map/index.html',{"list":1})
