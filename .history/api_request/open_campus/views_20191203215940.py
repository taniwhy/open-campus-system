from rest_framework import filters
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import mixins

from .models import Participant, ParticipantHistory, Subject
from .serializer import ParticipantSerializer, ParticipantHistorySerializer, SubjectSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class ParticipantViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ParticipantHistoryViewSet(viewsets.ModelViewSet):
    queryset = ParticipantHistory.objects.all()
    serializer_class = ParticipantHistorySerializer
