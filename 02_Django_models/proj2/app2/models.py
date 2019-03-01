from django.db import models

# Create your models here.

#A table
class Topic(models.Model):
    #define columns
    top_name = models.CharField(max_length=264, #constraint max length
                                unique=True) #Elements in this column should be unique

    def __str__(self):
         return self.top_name

#another table
class Webpage(models.Model):
    #Foreign key uses the same column from other table
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage,models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
