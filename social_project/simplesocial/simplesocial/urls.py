"""simplesocial URL Configuration

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
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.HomePage.as_view(),name='index'),
    path('accounts/',include('accounts.urls',namespace="accounts")),
    path('admin/', admin.site.urls),
    #No idea why he added this
    #path('accounts/',include('django.contrib.auth.urls')),
    path('groups/',include('groups.urls',namespace="groups")),
    path('loginsuccess/',views.Loginsuccess.as_view(),name="loginsuccess"),
    path('thanks/',views.Thanks.as_view(),name="thanks"),
]
