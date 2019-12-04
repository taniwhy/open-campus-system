from rest_framework import routers
from .views import ParticipantViewSet, ParticipantHistoryViewSet, SubjectViewSet, ParticipantDetail

router = routers.DefaultRouter()

router.register(r'participant', ParticipantDetail.as_view())
router.register(r'participant_history', ParticipantHistoryViewSet)
router.register(r'subject', SubjectViewSet)