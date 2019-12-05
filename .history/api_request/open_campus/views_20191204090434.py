import django_filters
from rest_framework import viewsets, filters

from .models import Participant, ParticipantHistory, Subject
from .serializer import ParticipantSerializer, ParticipantHistorySerializer, SubjectSerializer, ParticipantSerializer2


class SubjectList(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class ParticipantDetail(viewsets.ModelViewSet):
    """参加者テーブルから一件取得
    Parameters:
        post_code:参加者の郵便番号
    Returns:
        一件の参加者データ
    """
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    def get_queryset(self):
        id = self.request.query_params.get('id')
        address = self.request.query_params.get('address')
        queryset = Participant.objects.filter(id=id, address=address)

        return queryset


class ParticipantList(viewsets.ModelViewSet):
    """参加者テーブルから全権取得
    """
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer2



class ParticipantHistoryViewSet(viewsets.ModelViewSet):
    queryset = ParticipantHistory.objects.all()
    serializer_class = ParticipantHistorySerializer
