import os
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.utils.deconstruct import deconstructible
#deconstructd class for image location 

# from house.models import House

@deconstructible
class GenerateProfileImagePath(object):

    def __init__(self):
        pass
        
    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        path=f'media/accounts/{instance.user.id}/images/'
        name = f'profile_image.(ext)'
        return os.path.join(path,name)
    

user_profile_image_path=GenerateProfileImagePath()   # vreate object off generateprofile

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) # cascade refers when delete user then complte profi;e is delted
    image = models.FileField(upload_to=user_profile_image_path,blank=True,null=True)
    house = models.ForeignKey('house.House', on_delete=models.SET_NULL,null=True,blank=True,related_name='members')

    def __str__(self):
        return f'{self.user.username}\'s Profile'