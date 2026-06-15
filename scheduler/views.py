from django.shortcuts import render
from resource_scheduling.serializers import CourseSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course

# Create your views here.
@api_view(['GET'])
def index(request):
    return Response({'Sucess': 'Successful setup!'})

@api_view(['GET'])
def courses(request):
    course = Course.objects.all()
    x = CourseSerializer(course, many=True)
    return Response(x.data)