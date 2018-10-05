# Stores all URL patterns for your project

"""first_project URL Configuration

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

##Default
from django.contrib import admin
from django.urls import path, include
##New import
from first_app import views

urlpatterns = [
    path('', views.index, name="index"), ##Maps applications view to the url,  # url : "127.0.0.1:8000/
    path('first_app/', include('first_app.urls')), # url : "127.0.0.1:8000/first_app"
    # 'first_app' can be any arbitary string
    # path('new_ext/', include('first_app.urls'))
    path('admin/', admin.site.urls), ##Appears default
]
