import django_filters
from rest_framework import viewsets, filters

from .models import Participant, ParticipantHistory, Subject
from .serializer import ParticipantSerializer, ParticipantHistorySerializer, SubjectSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    """学科一覧を取得
    Returns:
        学科一覧データ
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class ParticipantViewSet(viewsets.ModelViewSet):
    """参加者テーブルからデータ取得
    """
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

    def get_queryset(self):
        if self.request.query_params.get('id') == None:
            queryset = Participant.objects.all()
            return queryset
        else:
            id = self.request.query_params.get('id')
            address = self.request.query_params.get('address')
            queryset = Participant.objects.filter(id=id, address=address)
            return queryset


class ParticipantHistoryViewSet(viewsets.ModelViewSet):
    queryset = ParticipantHistory.objects.all()
    serializer_class = ParticipantHistorySerializer
