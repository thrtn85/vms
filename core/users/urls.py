from django.urls import path
from .views import edit, dashboard, home, PasswordChangeView
from django.urls import reverse_lazy


from django.contrib.auth import views as auth_view

app_name = 'users'

urlpatterns = [
    path('', home, name='home'),

    # user registration
    #path('register/', register, name='register'),

    # user login/logout
    #path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logged_out.html'), name='logout'),

    path('dashboard/', dashboard, name='dashboard'),

    # edit profile
    path('edit_profile/', edit, name='edit'),


]