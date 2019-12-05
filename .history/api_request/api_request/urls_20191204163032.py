from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from open_campus.urls import router

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', obtain_jwt_token),
    url(r'^api/', include(router.urls)),
    url(r'^api/auth/obtain_token/', obtain_jwt_token),
    url(r'^api/auth/refresh_token/', refresh_jwt_token),
]
