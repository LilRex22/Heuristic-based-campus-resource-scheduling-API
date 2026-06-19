from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from scheduler.models import (Lecturer, Room, Course, Schedule, Timeslot)

class ScheduleSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Schedule
        
class LecturerSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Lecturer
        
class RoomSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Room
        
class CourseSerializer(ModelSerializer):
    Lecturer = serializers.StringRelatedField() # this turns the foreign key into a string representation of the related object
    Level = serializers.CharField(source='Level.Name', read_only=True)
    Room =serializers.StringRelatedField()
    class Meta:
        fields = '__all__'
        model = Course
        

class TimeslotSerializer(ModelSerializer):
    class Meta: 
        fields = '__all__'
        model = Timeslot