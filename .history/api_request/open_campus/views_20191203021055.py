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
    created_after = filters.CharFilter(method='filter_created_after')

    def filter_created_after(self, qs, name, value):
        try:
            offset = isodate.parse_duration(value)
        except:
            offset = isodate.parse_duration('P1W')

        date = datetime.now() - offset
        return qs.filter(created_at__gte=date)


class ParticipantHistoryViewSet(viewsets.ModelViewSet):
    queryset = ParticipantHistory.objects.all()
    serializer_class = ParticipantHistorySerializer
