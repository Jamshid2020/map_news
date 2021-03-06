"""map_news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.v1.maps.views import UserViewSet
from api.v1.news.views import NewsViewSet


router = routers.DefaultRouter()
router.register(r'v1/users', UserViewSet)
router.register(r'v1/news', NewsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('maps.urls')),
    path('api/', include(router.urls)),


    path('__debug__/', include(debug_toolbar.urls)),
]
