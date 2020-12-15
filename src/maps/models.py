from django.db import models
from django.contrib.postgres.search import SearchVectorField

class Region(models.Model):

    name_region = models.CharField(max_length=300, null=False)
    koordinate_region = models.CharField(max_length=300, null=False)


class News(models.Model):
    title = models.CharField(max_length=300, null=False)
    link = models.CharField(max_length=500, null=False)
    web_site = models.CharField(max_length=30, null=False)
    news_date = models.CharField(max_length=30, null=False)
    content = models.TextField(null=False,)
    document_vector = SearchVectorField(null=True,)
    created = models.DateTimeField(auto_now=True,)
    regions = models.ManyToManyField(Region)
