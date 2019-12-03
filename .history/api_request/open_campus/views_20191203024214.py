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


class PaticipantListView(generics.ListAPIView):
    serializer_class = ParticipantSerializer
    queryset = Participant.objects.filter()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('phone_number', 'postal_code')


class ParticipantHistoryViewSet(viewsets.ModelViewSet):
    queryset = ParticipantHistory.objects.all()
    serializer_class = ParticipantHistorySerializer
