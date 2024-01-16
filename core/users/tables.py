import django_tables2 as tables
from django.contrib.auth import get_user_model


User = get_user_model()


class UserTable(tables.Table):
     last_login = tables.Column()
     
     class Meta:
          model = User
          sequence = ("username","first_name", "last_name", "email","is_active", "last_login", "is_staff")
          exclude = ("id","password", "is_superuser", "date_joined" )