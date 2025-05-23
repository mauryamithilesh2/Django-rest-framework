from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver

from .models import Profile

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)


# generating automatic username using first and last name 
#in siggnals becouse signal disrect modeify the  admin a pannel by auto set

@receiver(pre_save,sender=User)
def set_usename(sender,instance,**kwargs):
    if not instance.username:
        username= f'{instance.first_name}_{instance.last_name}'.lower()
        counter =1
        while User.objects.filter(username=username):
            counter += 1
            username= f'{instance.first_name}_{instance.last_name}_{counter}'.lower()
        instance.username = username
