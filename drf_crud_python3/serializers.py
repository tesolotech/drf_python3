from rest_framework import serializers
from .models import Student


class StudentSerializar(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    mobile = serializers.CharField(max_length=13)


def create(self, validate_data):
    return Student.objects.create(**validate_data)
