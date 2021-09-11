from django.contrib import admin
from .models import *
from headteacher.models import HeadTeacher
admin.site.register(School)
admin.site.register(HeadTeacher)