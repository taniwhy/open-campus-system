import django_filters.rest_framework
from rest_framework import viewsets, filters
from rest_framework import generics

from .models import Participant, ParticipantHistory, Subject
from .serializer import ParticipantSerializer, ParticipantHistorySerializer, SubjectSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class ParticipantListView(generics.ListAPIView):
    serializer_class = ParticipantSerializer

    def get_queryset(self):
        queryset = Participant.objects.all()
        family_name = self.request.query_params.get('family_name', None)
        if family_name is not None:
            queryset = queryset.filter(purchaser__family_name=family_name)
        return queryset


class ParticipantHistoryViewSet(viewsets.ModelViewSet):
    queryset = ParticipantHistory.objects.all()
    serializer_class = ParticipantHistorySerializer
