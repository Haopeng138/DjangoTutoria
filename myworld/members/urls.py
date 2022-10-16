from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('',views.index,name='index'),
    path('add/',views.add,name='add'),
    path('add/addrecord/',views.addrecord,name='addrecord'),
]