from django.shortcuts import render
# Import models
from app2.models import Topic, Webpage,AccessRecord
# Create your views here.

def index(request):
    return render(request,'index.html',context=None)

def db_table(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request,'tables.html',context=date_dict)
