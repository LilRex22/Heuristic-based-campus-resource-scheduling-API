from django.shortcuts import render
from resource_scheduling.serializers import (CourseSerializer, LecturerSerializer, RoomSerializer, TimeslotSerializer)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import (Course, Lecturer, Room, Timeslot)

# Create your views here.
@api_view(['GET'])
def index(request):
    return Response({'Sucess': 'Successful setup!'})

@api_view(['GET'])
def courses(request):
    course = Course.objects.all()
    no_of_course = len(course)
    x = CourseSerializer(course, many=True)
    
    return Response({
        'courses': x.data,
        'count': no_of_course
    })

@api_view(['GET'])
def lecturers(request):
    lecturers = Lecturer.objects.all()
    x = LecturerSerializer(lecturers, many=True)
    return Response(x.data)

@api_view(['GET'])
def classrooms(request):
    rooms = Room.objects.all()
    x = RoomSerializer(rooms, many=True)
    return Response(x.data)

@api_view(['GET'])
def timeslots(request):
    timeslots = Timeslot.objects.all()
    x = TimeslotSerializer(timeslots, many=True)
    return Response(x.data)