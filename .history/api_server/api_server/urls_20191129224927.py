from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from open_campus.views import ParticipantListViewSet

router = DefaultRouter()
router.register(r'goods', ParticipantListViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url('api/', include(router.urls)),
]