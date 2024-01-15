from django.urls import path
from .views import dashboard, home, edit_account, edit_profile, UserListView
from django.urls import reverse_lazy


from django.contrib.auth import views as auth_view

app_name = 'users'

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),

    # edit account
    path('edit-account/', edit_account, name='edit_account'),
    # edit profile
    path('edit-profile/', edit_profile, name='edit_profile'),

    #path('user-mgmt/', user_mgmt, name='user_mgmt'),
    path("user-mgmt/", UserListView.as_view())
]