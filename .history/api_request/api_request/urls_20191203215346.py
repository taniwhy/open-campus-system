from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from open_campus import views

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', views.ParticipantViewSet.as_view()),
]