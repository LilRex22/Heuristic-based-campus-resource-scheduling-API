from django.db import models

# Create your models here.
class Lecturer(models.Model):
    Name = models.CharField(max_length=200)
    Department = models.CharField(max_length=200)
    Available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.Name
    
    
class Room(models.Model):
    Name = models.CharField(max_length=200)
    Capacity = models.IntegerField()
    Location = models.CharField(max_length=200)
    
    def __str__(self):
        return self.Name
    
class Level(models.Model):
    Name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.Name


class Course(models.Model):
    Course_code = models.CharField(max_length=50)
    Course_title = models.CharField(max_length=50)
    Level = models.ForeignKey(Level, on_delete=models.CASCADE)
    Credit = models.IntegerField()
    Student = models.CharField(max_length=200)
    Lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    Room = models.ForeignKey(Room, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Course_code


class Schedule(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Room = models.ForeignKey(Room, on_delete=models.CASCADE)
    Timeslot = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Course