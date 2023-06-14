from rest_framework import serializers
from .models import Led

class LedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Led
        fields = "__all__"