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

    # # user password
    # path('password_change/', auth_view.PasswordChangeView.as_view(
    #     template_name='users/password_change_form.html', success_url=reverse_lazy('users:password_change_done')),
    #     name='password_change'),
    # path('password_change_done', auth_view.PasswordChangeDoneView.as_view(
    #     template_name='users/password_change_done.html'),
    #     name='password_change_done'),
    # path('password_reset/', auth_view.PasswordResetView.as_view(
    #     template_name='users/password_reset_form.html',
    #     email_template_name='users/password_reset_email.html',
    #     success_url=reverse_lazy('users:password_reset_done')), 
    #     name='password_reset'),
    # path('password_reset/done/', auth_view.PasswordResetDoneView.as_view(
    #     template_name='users/password_reset_done.html'), 
    #     name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(
    #     template_name='users/password_reset_confirm.html',
    #     success_url=reverse_lazy('users:login')), 
    #     name='password_reset_confirm'),
    # path('reset/done/', auth_view.PasswordResetCompleteView.as_view(
    #     template_name='users/password_reset_complete.html'), 
    #     name='password_reset_complete'),

    path('dashboard/', dashboard, name='dashboard'),

    # edit profile
    path('edit_profile/', edit, name='edit'),


]