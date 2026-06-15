from django.contrib import admin
from .models import (Lecturer, Room, Level, Course, Schedule)

# Register your models here.
admin.site.register(Lecturer)
admin.site.register(Room)
admin.site.register(Level)
admin.site.register(Course)
admin.site.register(Schedule)
