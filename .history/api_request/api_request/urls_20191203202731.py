from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from open_campus import views

urlpatterns = [
    path('api/', views.ParticipantDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)