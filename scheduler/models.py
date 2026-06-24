from django.db import models
from datetime import datetime

# Create your models here.
class Lecturer(models.Model):
    Name = models.CharField(max_length=200, unique=True)
    Department = models.CharField(max_length=200)
    Available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.Name
    
    
class Room(models.Model):
    Name = models.CharField(max_length=200, unique=True)
    Type = models.CharField(max_length=200, default='Lecture Hall')
    Capacity = models.IntegerField()
    Location = models.CharField(max_length=200)
    Available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.Name
    
class Level(models.Model):
    Name = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.Name


class Course(models.Model):
    Course_code = models.CharField(max_length=50, unique=True)
    Course_title = models.CharField(max_length=50)
    Level = models.ForeignKey(Level, on_delete=models.CASCADE)
    Credit = models.IntegerField()
    Student = models.CharField(max_length=200)
    Lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    Room = models.ForeignKey(Room, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Course_code


class Timeslot(models.Model):
    Day = models.CharField(max_length=200)
    Start_time = models.TimeField()
    End_time = models.TimeField()
    Duration = models.DurationField(editable=False)
    
    def save(self, *args, **kwargs):
        start = datetime.combine(datetime.today(), self.Start_time)
        end = datetime.combine(datetime.today(), self.End_time)
        self.Duration = end - start
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.Day


class Schedule(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Room = models.ForeignKey(Room, on_delete=models.CASCADE)
    Timeslot = models.ForeignKey(Timeslot, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Course} - {self.Room} - {self.Timeslot}"