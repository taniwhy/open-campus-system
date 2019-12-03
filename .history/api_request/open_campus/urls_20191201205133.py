from rest_framework import routers
from .views import ParticipantViewSet,SubjectViewSet

router = routers.DefaultRouter()

router.register(r'participant', ParticipantViewSet)
router.register(r'participan_history', ParticipantViewSet)
router.register(r'subject', SubjectViewSet)