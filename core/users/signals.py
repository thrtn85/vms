from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import UserProfile

User = get_user_model()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
     if created:
          UserProfile.objects.create(user=User)
# def create_user_profile(request, **kwargs):
#      user = kwargs['user']
#      profile = UserProfile(user=user)
#      profile.save()

#      if settings.DEBUG:
#           print('New profile created for user' + user.email)
#      return

