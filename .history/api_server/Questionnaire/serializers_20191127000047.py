from rest_framework import serializers
from .models import Participant


class participantSerializer(serializers.ModelSerializer):
    class Meta:
        model = participant
        fields = (
            'participant_id',
            'first_name',
            'last_name',
            'first_name_reading',
            'last_name_reading',
            'birthday',
            'gender',
            'phone_number',
            'postal_code',
            'address',
            'job',
            'highschool_id',
            )