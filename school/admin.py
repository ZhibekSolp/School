from django.contrib import admin
from .models import School
from .models import Director
from .models import HeadTeacher
from .models import Teachers
from .models import Classes

admin.site.register(School)
admin.site.register(Director)
admin.site.register(HeadTeacher)
admin.site.register(Teachers)
admin.site.register(Classes)