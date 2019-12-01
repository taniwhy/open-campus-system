from rest_framework import viewsets, routers
from open_campus.models import Participant
from open_campus.serializers import ParticipantSerializer

class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

router = routers.DefaultRouter()
router.register(r'participant', ParticipantViewSet)