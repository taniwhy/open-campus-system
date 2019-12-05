from django.contrib import admin
from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token # 追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', obtain_jwt_token), # 追加
]