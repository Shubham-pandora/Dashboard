from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    # ...your other urls...
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]