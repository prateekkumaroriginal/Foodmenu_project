from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('register/', user_views.register, name='register-user'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login-user'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout-user'),
    path('profile/', user_views.user_profile, name='user-profile')
]
