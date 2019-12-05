from rest_framework import routers
from .views import ParticipantViewSet,articipantHistoryViewSet, SubjectViewSet

router = routers.DefaultRouter()

router.register(r'participant', ParticipantViewSet)
router.register(r'participan_history', ParticipantHistoryViewSet)
router.register(r'subject', SubjectViewSet)