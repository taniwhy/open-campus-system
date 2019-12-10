import django_filters
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly

from .models import Participant, ParticipantHistory, Subject
from .serializer import ParticipantSerializer, ParticipantHistorySerializer, SubjectSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    """学科一覧を取得
    Returns:
        Object: 学科一覧データ
    """
    permission_classes = [AllowAny]
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class ParticipantViewSet(viewsets.ModelViewSet):
    """参加者テーブルからデータ取得
    """
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

    def get_queryset(self):
        """GETメソッド処理
        Returns:
            Object: 参加者情報
        """
        if self.request.query_params.get('phone_number') == None:
            queryset = Participant.objects.all()
            return queryset
        else:
            family_name = self.request.query_params.get('family_name')
            first_name = self.request.query_params.get('first_name')
            birthday = self.request.query_params.get('birthday')
            phone_number = self.request.query_params.get('phone_number')
            postal_code = self.request.query_params.get('postal_code')

            queryset = Participant.objects.filter(
                family_name=family_name,
                first_name=first_name,
                birthday=birthday,
                phone_number=phone_number,
                postal_code=postal_code)
            return queryset

    def get_permissions(self):
        if 'phone_number' in self.request.query_params:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class ParticipantHistoryViewSet(viewsets.ModelViewSet):
    queryset = ParticipantHistory.objects.all()
    serializer_class = ParticipantHistorySerializer

    def get_queryset(self):
        """GETメソッド処理
        Returns:
            Object: 参加者情報
        """
        if self.request.query_params.get('join_day') == None:
            queryset = ParticipantHistory.objects.all()
            return queryset
        else:
            join_day = self.request.query_params.get('join_day')
            queryset = ParticipantHistory.objects.filter(
                join_day=join_day)
            return queryset

    def get_permissions(self):
        if self.request.method == 'POST':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
