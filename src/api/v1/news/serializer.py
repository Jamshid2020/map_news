from rest_framework import serializers
from maps.models import News


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'link']
