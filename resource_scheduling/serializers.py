from rest_framework.serializers import ModelSerializer
from scheduler.models import (Lecturer, Room, Course, Schedule)

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
    class Meta:
        fields = '__all__'
        model = Course