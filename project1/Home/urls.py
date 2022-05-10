from unicodedata import name
from django.contrib import admin
from django.urls import path
from Home import views


urlpatterns = [
    path("", views.index, name='Home' ),
    path("about", views.about, name='about' ),
    path("services", views.services, name='services'),
    path("web", views.web, name='web' ),
    path("pbx", views.pbx, name='pbx' ),
    path("output", views.output, name='output' ),
    path("contact", views.contact, name='contact' ),
  
]
