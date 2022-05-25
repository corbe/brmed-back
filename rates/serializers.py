from rest_framework import serializers
from .models import Rate, RateValue


class RateValueSerializer(serializers.ModelSerializer):
  class Meta:
    model = RateValue
    depth = 1
    fields = (
      'id',
      'currency',
      'value'
    )


class RateSerializer(serializers.Serializer):
    date = serializers.DateField()
    rate = RateValueSerializer(many=True)
