from rest_framework import routers
from .views import ParticipantViewSet, ParticipantHistoryViewSet, SubjectViewSet

router = routers.DefaultRouter()

router.register(r'participant', ParticipantList)
router.register(r'participant_detail', ParticipantDetail)
router.register(r'participant_history', ParticipantHistoryViewSet)
router.register(r'subject', SubjectViewSet)