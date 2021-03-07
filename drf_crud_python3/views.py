from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializar
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


# Create your views here.

def welcome(request):
    json_data = JSONRenderer().render({'message': 'Welcome to DRF with Python3'})
    return HttpResponse(json_data,content_type='application/json')

def get_student_detail(request):
    student =  Student.objects.get(id=1)
    serializar = StudentSerializar(student)
    json_data = JSONRenderer().render(serializar.data)
    return HttpResponse(json_data, content_type='application/json')

