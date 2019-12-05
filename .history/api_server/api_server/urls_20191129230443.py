from django.conf.urls import url, include
from django.contrib import admin
from open_campus import apis

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(apis.router.urls)),
]