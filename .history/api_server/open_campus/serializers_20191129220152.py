from rest_framework import serializers
from open_campus.models import Participant


class ParticipantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = ("id", "title", 'stock_count')