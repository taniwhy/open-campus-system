from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from open_campus.urls import router


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
]