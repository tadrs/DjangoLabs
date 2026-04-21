from rest_framework import serializers
from ..models import Trainee

class TraineeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
