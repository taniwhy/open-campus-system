import django_filters
from rest_framework import viewsets, filters

from .models import Participant, ParticipantHistory, Subject
from .serializer import ParticipantSerializer, ParticipantHistorySerializer, SubjectSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class ParticipantList(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


class ParticipantDetail(viewsets.ModelViewSet):
    """参加者テーブルから一件取得
    Returns:
        参加者データ
    """
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    def get_queryset(self):
        id = self.request.query_params.get('id')
        address = self.request.query_params.get('address')
        queryset = Participant.objects.filter(id=id, address=address)

        return queryset

class ParticipantHistoryViewSet(viewsets.ModelViewSet):
    queryset = ParticipantHistory.objects.all()
    serializer_class = ParticipantHistorySerializer
