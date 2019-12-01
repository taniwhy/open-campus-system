from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from open_campus.urls import router

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # blog.urlsをincludeする
    url(r'^api/', include(blog_router.urls)),
]