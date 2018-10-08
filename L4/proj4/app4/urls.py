from django.urls import path
from app4 import views

#Template tagging
app_name = 'Application4'

urlpatterns =[
    path('relative/',views.relative,name='relative_p'),
    path('other/',views.other,name='other_p'),
]
