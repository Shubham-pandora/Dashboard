from unicodedata import name
from django.contrib import admin
from django.urls import path
from Home import views


urlpatterns = [
    path("", views.index, name='index' ),
    path("about", views.about, name='about' ),
    path("services", views.services, name='services'),
    path("web", views.web, name='web' ),
    path("pbx", views.pbx, name='pbx' ),
    path("output", views.output, name='output' ),
    path("contact", views.contact, name='contact' ),
    path("add/", views.add, name='add' ),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),  
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
]
