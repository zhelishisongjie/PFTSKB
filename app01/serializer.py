from rest_framework import serializers
from app01.models import *


class PftdDecisionIndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PftdDecisionIndicator
        fields = '__all__'