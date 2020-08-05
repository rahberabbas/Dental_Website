from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='Home'),
    path('contact/',views.contact,name='Contact'),
    path('pricing/',views.pricing,name='Pricing'),
    path('service/',views.service,name='Service'),
    path('appointment/',views.appointment,name='Appointment'),
]
