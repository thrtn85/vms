from django.db import models


class Volunteer(models.Model):
     # Personal Information
     name = models.CharField(max_length=64 )
     date_of_birth = models.DateField(verbose_name="Date of Birth", blank=True, null=True)

     # Photo
     photo = models.FileField(upload_to='profile_images/')

     # Skills and Interests
     skills = models.ManyToManyField('Skills', blank=True)
     interests = models.ManyToManyField('Interests', blank=True)

     # Availability
     # Experience
     # Bio or Introduction
     bio = models.TextField(blank=True, null=True)

     # Preferred Volunteer Opportunities
     # --- this should come from opportunities model

     # References
     # Emergency Contact Information

     def __str__(self):
          return self.name

     class Meta:
          verbose_name_plural = "Volunteers"


class Skills(models.Model):
     name = models.CharField(max_length=64, verbose_name="Skill Name")

     def __str__(self):
          return self.name
     
     class Meta:
          verbose_name_plural = "Skills"


class Interests(models.Model):
     name =  models.CharField(max_length=64, verbose_name="Interest Name")

     def __str__(self):
          return self.name
     
     class Meta:
          verbose_name_plural = "Interests"