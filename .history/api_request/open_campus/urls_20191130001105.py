from rest_framework import routers
from .views import ParticipantViewSet

router = routers.DefaultRouter()
router.register(r'users', ParticipantViewSet)