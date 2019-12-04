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
        if self.request.query_params.get('phone_number') == None:
            queryset = Participant.objects.all()
            return queryset
        else:
            phone_number = self.request.query_params.get('phone_number')
            postal_code = self.request.query_params.get('postal_code')
            queryset = Participant.objects.filter(phone_number=phone_number, postal_code=postal_code)
            return queryset


class ParticipantHistoryViewSet(viewsets.ModelViewSet):
    queryset = ParticipantHistory.objects.all()
    serializer_class = ParticipantHistorySerializer
