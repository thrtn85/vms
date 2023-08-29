from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date
import re

def validate_date_of_birth(value):
     today = date.today()
     if value >= today:
          raise ValidationError("Date of birth cannot be today's date or in the future.")
