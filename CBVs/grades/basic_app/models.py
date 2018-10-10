from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.urls import reverse

# Create your models here.
class SiteUser(User):
    def get_absolute_url(self):
        return "/"

class Student(models.Model):
    candidate = models.OneToOneField(SiteUser,on_delete=models.CASCADE)
    grade = models.CharField(max_length=1,blank=True)
    remark = models.CharField(max_length=256,blank=True)

    def __str__(self):
        return self.candidate.first_name + " " + self.candidate.last_name

    def get_absolute_url(self):
        return reverse("app:details",kwargs={'pk':self.pk})

class StudentMarks(models.Model):
    candidate = models.OneToOneField(Student,on_delete=models.CASCADE)
    maths = models.PositiveIntegerField()
    science = models.PositiveIntegerField()
    english = models.PositiveIntegerField()
    tamil = models.PositiveIntegerField()
    evs = models.PositiveIntegerField()

    def __str__(self):
        return self.candidate.first_name + " " + self.candidate.last_name
