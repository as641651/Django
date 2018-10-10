from django.contrib import admin
from basic_app.models import Student,StudentMarks,SiteUser
# Register your models here.

admin.site.register(Student)
admin.site.register(StudentMarks)
admin.site.register(SiteUser)
