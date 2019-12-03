from rest_framework import routers
from .views import ParticipantViewSet, ParticipantFilter, ParticipantHistoryViewSet, SubjectViewSet

router = routers.DefaultRouter()

router.register(r'participant', ParticipantViewSet)
router.register(r'participant_filter', ParticipantFilter)
router.register(r'participant_history', ParticipantHistoryViewSet)
router.register(r'subject', SubjectViewSet)
