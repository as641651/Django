"""hello_world URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from basic_app import views

urlpatterns = [
    path("",views.CBView.as_view()),
    path("templateview/",views.IndexView.as_view()),
    path("listview/",views.SchoolListView.as_view(),name='list'),
    #for detail view, each enter gets its own url based on its primary key
    #pk stands for primary key
    path('listview/<int:pk>/',views.SchoolDetailView.as_view(),name='details'),
    path('createview/',views.SchoolCreateView.as_view()),
    path('update/<int:pk>/',views.SchoolUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.SchoolDeleteView.as_view(),name='delete'),
    path('admin/', admin.site.urls),
]
