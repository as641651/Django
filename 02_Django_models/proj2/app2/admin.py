from django.contrib import admin
#import all tables
from app2.models import AccessRecord, Topic, Webpage

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
