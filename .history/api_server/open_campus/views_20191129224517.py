from rest_framework import mixins
from rest_framework import viewsets

from .models import Participant
from .serializer import ParticipantSerializer

class ParticipantListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
     queryset = Participant.objects.all()
     serializer_class = ParticipantSerializer