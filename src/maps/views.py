import json
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from .models import News
from .services import searchNews, search_by_group

def index(request):


    # q = request.GET.get('q', '')
    # search_query = SearchQuery(f"{q}:*", search_type='raw')

    # .annotate(rank=SearchRank(vector, query)).
    # model = News.objects.filter(document_vector=search_query).order_by('-created')[:10]

    # for data in model:
    #     print(data.title)


    result = searchNews(request, 10)
    list = []
    for title, link, region_id, region_name, coordinates in result:
        print(region_name,' --- ', coordinates, '------', link)
        print('***************************')
        item = {}
        item['title']=title
        item['link']=link
        item['region_id']=region_id
        item['region_name']=region_name
        item['coordinates']=coordinates

        #print(title)

        list.append(item)




    return render(request,'map/index.html',{"list":list, 'q':request.GET.get('q', '')})


def search(request):
    content=[]
    result = search_by_group(request)
    for id, title, regions in result:

        item = {}
        item['id']=id
        item['title']=title
        item['regions']=regions


        #print(title)

        content.append(item)


  #   content = [
  #   {
  #     'title': 'Horse',
  #     'description': 'An Animal',
  #   },
  #   {
  #     'title': 'Cow',
  #     'description': 'Another Animal',
  #   }
  # ]

    response = JsonResponse({"items": content})
    return response
