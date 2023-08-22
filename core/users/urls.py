from django.urls import path
from .views import edit, dashboard, home
from django.urls import reverse_lazy


from django.contrib.auth import views as auth_view

app_name = 'users'

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),

    # edit profile
    path('edit_profile/', edit, name='edit'),

]