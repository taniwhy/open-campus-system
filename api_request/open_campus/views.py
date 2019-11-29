import django_filters
from rest_framework import viewsets, filters

from .models import Participant
from .serializer import ParticipantSerializer


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
