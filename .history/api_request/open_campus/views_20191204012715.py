import django_filters
from rest_framework import viewsets, filters

from .models import Participant, ParticipantHistory, Subject
from .serializer import ParticipantSerializer, ParticipantHistorySerializer, SubjectSerializer


class SubjectList(viewsets.ModelViewSet):
    """学科一覧を取得
    Returns:
        学科一覧
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class ParticipantList(viewsets.ModelViewSet):
    """参加者テーブルから全権取得
    Returns:
        参加者一覧
    """
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


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
        if self.request.query_params == None:
            return queryset
        else:
            id = self.request.query_params.get('id')
            address = self.request.query_params.get('address')
            queryset = Participant.objects.filter(id=id, address=address)

            return self.request.query_params

class ParticipantHistoryViewSet(viewsets.ModelViewSet):
    queryset = ParticipantHistory.objects.all()
    serializer_class = ParticipantHistorySerializer
