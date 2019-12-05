import django_filters as filters
from rest_framework import viewsets, filters, generics


from .models import Participant, ParticipantHistory, Subject
from .serializer import ParticipantSerializer, ParticipantHistorySerializer, SubjectSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


class ParticipantFilter(generics.ListAPIView):
    serializer_class = ParticipantSerializer

    def get_queryset(self):
        queryset = Participant.objects.all()
        phone_number = self.request.query_params.get('phone_number', None)
        postal_code = self.request.query_params.get('postal_code', None)
        if phone_number is not None:
            queryset = queryset.filter(phone_number=phone_number, postal_code=postal_code)
        return queryset


class ParticipantHistoryViewSet(viewsets.ModelViewSet):
    queryset = ParticipantHistory.objects.all()
    serializer_class = ParticipantHistorySerializer
