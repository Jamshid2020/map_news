from rest_framework import viewsets
from maps.models import News

from .serializer import NewsSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
