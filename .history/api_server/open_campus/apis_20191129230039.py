from rest_framework import viewsets, routers
from .models import Participant
from .serializers import ParticipantSerializer
from rest_framework.filters import DjangoFilterBackend

class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Ar.objects.all()
    serializer_class = ParticipantSerializer

router = routers.DefaultRouter()
router.register(r'Participant', ParticipantViewSet)