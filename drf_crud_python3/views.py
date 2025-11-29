from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializar
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
import io
from django.views.decorators.csrf import csrf_exempt, csrf_protect


# Create your views here.

def welcome(request):
    json_data = JSONRenderer().render({'message': 'Welcome to DRF with Python3'})
    return HttpResponse(json_data, content_type='application/json')


def get_student_detail(request):
    student = Student.objects.get(id=1)
    serializer = StudentSerializar(student)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')


@csrf_protect
def create_student(request):
    if request.method == 'POST':
        json_data = request.body
        stream_data = io.BytesIO(json_data)
        python_object = JSONParser().parse(stream_data)
        serializer = StudentSerializar(data=python_object)
        if serializer.is_valid():
            serializer.save()
            res = {'status': 200, 'message': 'Successfully Created'}
            json_data_res = JSONRenderer().render(res)
            return HttpResponse(json_data_res, content_type='application/json')
        json_data_error = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data_error, content_type='application/json')
