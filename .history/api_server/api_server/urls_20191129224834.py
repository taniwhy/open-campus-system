from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from open_campus.views import ParticipantListViewSetltRouter()

router = DefaultRouter()
router.register(r'goods', GoodsListViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url('api/', include(router.urls)),
]