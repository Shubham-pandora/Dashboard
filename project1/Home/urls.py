from unicodedata import name
from django.contrib import admin
from django.urls import path
from Home import views


urlpatterns = [
    path("", views.index, name='index' ),
    path("IPTables", views.IPTables, name='IPTables' ),
    path("services", views.services, name='services'),
    path("web", views.web, name='web' ),
    path("pbx", views.pbx, name='pbx' ),
    path("output", views.output, name='output' ),
    path("img", views.images, name='img' ),
    path("checkupdate", views.checkupdate, name='checkupdate' ),
    path("checkupdate/add/", views.addinNewUpdateInfo, name='addnewupdateinfo' ),    
    path("checkupdate/add/addrecord/", views.addrecordinNewUpdateInfo, name='addrecordnewupdateinfo' ),    
    path('delete/<int:id>', views.deleteinNewUpdateInfo, name='deleteinNewUpdateInfo'),
    path('checkupdate/update/<int:id>', views.updateinNewUpdateInfo, name='updateinNewUpdateInfo'),   
    path('checkupdate/update/updaterecord/<int:id>', views.updaterecordNewUpdateInfo, name='updaterecordinNewUpdateInfo'),
    path("loading", views.loading, name='loading'),  # Add this line
    path('cert-expiry/', views.cert_expiry, name='cert_expiry'),
    path('login/', views.custom_login, name='custom_login'),
    path('logout/', views.custom_logout, name='custom_logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # ---------------sample 
  
]
