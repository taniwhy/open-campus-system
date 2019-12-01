from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework import routers
from open_campus import apis


urlpatterns = [
    path('admin/', admin.site.urls),
    url('api/', include(router.urls)),\
]