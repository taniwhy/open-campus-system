from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    url('api/', include(router.urls)),
]