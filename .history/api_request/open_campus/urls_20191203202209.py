from rest_framework import routers
from .views import ParticipantViewSet, ParticipantHistoryViewSet, SubjectViewSet, ParticipantDetail
from open_campus import views

router = routers.DefaultRouter()

router.register(r'participant', views.ParticipantDetail.as_view())
router.register(r'participant_history', ParticipantHistoryViewSet)
router.register(r'subject', SubjectViewSet)