from rest_framework import serializers
from .models import Participant, ParticipantHitory, Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = "__all__"

class ParticipantHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = "__all__"
