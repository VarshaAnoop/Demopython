from django.contrib import admin
from .import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    # path('demo1/',views.demo1,name='demo1')

]