from rest_framework import viewsets, routers
from .models import Participant
from .serializers import ParticipantSerializer

class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

router = routers.DefaultRouter()
router.register(r'participant', ParticipantViewSet)