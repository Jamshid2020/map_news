from django.shortcuts import render
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from .models import News
def index(request):
    q = request.GET.get('q', '')
    print(q)
    vector = SearchVector('document_vector')
    query = SearchQuery(q)
    model = News.objects.annotate(rank=SearchRank(vector, query)).order_by('-rank')

    for data in model:
        print(data.title)
    return render(request,'map/index.html',{"list":1})
