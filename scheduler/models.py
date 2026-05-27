from django.db import models

# Create your models here.
class Lecturer(models.Model):
    Name = models.charfield(max_length=200)
    
    
class Room(models.Model):
    Name = models.charfield(max_length=200)
    Capacity = models.IntegerField()
    

class Course(models.Model):
    Name = models.charfield(max_length=50)
    Lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    Room = models.ForeignKey(Room, on_delete=models.CASCADE)


class Schedule(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Room = models.ForeignKey(Room, on_delete=models.CASCADE)
    Timeslot = models.CharField(max_length=100)