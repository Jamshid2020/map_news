from django.contrib import admin
from .models import  Region

class RegionAdmin(admin.ModelAdmin):
    list_display = ['name_region', 'koordinate_region']

admin.site.register(Region, RegionAdmin)
