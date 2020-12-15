from django.contrib import admin
from .models import  Region, News

class RegionAdmin(admin.ModelAdmin):
    list_display = ['name_region', 'koordinate_region']

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'web_site', 'created']

admin.site.register(Region, RegionAdmin)
admin.site.register(News, NewsAdmin)
