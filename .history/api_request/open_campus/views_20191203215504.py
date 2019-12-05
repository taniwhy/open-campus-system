from rest_framework import filters
from rest_framework import generics
from rest_framework import viewsets

from .models import Participant, ParticipantHistory, Subject
from .serializer import ParticipantSerializer, ParticipantHistorySerializer, SubjectSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class ParticipantViewSet(generics.ListCreateAPIView):
    def get_queryset(self):
        return Participant.objects.filter(id=self.kwargs["id"])

class ParticipantHistoryViewSet(viewsets.ModelViewSet):
    queryset = ParticipantHistory.objects.all()
    serializer_class = ParticipantHistorySerializer
