from rest_framework import filters
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import mixins

from .models import Participant, ParticipantHistory, Subject
from .serializer import ParticipantSerializer, ParticipantHistorySerializer, SubjectSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class ParticipantFilter(filters.FilterSet):

    created_after = filters.CharFilter(method='filter_created_after')

    class Meta:
        model = Participant

    def filter_created_after(self, qs, name, value):
        return qs.filter(created_at__gte=valie)


class ParticipantViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Participant.objects.none()
    serializer_class = ParticipantSerializer
    filter_backends = (filters.rest_framework.DjangoFilterBackend,)
    filter_class = ArticleFilter
    def get_queryset(self):
        qs = Participant.objects.all()
        if 'created_after' in self.request.query_params:
            return qs

        offset = isodate.parse_duration('P1W')
        date = datetime.now() - offset
        return qs.filter(created_at__gte=date)

class ParticipantHistoryViewSet(viewsets.ModelViewSet):
    queryset = ParticipantHistory.objects.all()
    serializer_class = ParticipantHistorySerializer
