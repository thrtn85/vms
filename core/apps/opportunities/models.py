from django.db import models
from django.contrib.auth.models import Permission

class Opportunity(models.Model):
     name = models.TextField(blank = False)

     def __str__(self):
          return self.name