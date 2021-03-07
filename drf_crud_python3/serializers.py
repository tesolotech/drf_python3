
from rest_framework import serializers

class StudentSerializar(serializers.Serializer):
    name = serializers.CharField(max_length = 100)
    age = serializers.IntegerField()
    mobile = serializers.CharField(max_length = 13)