from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from blog.urls import router as blog_router

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', obtain_jwt_token), # 追加
]