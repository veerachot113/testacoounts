from django.contrib import admin
from .models import CustomUser, Student, Organizer




admin.site.register(CustomUser)
admin.site.register(Student)
admin.site.register(Organizer)

