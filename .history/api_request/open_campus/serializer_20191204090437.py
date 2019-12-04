from rest_framework import serializers
from .models import Participant, ParticipantHistory, Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = "__all__"


class ParticipantSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = "__all__"

class ParticipantHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantHistory
        fields = "__all__"
