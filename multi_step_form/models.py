from django.db import models

# Create your models here.


class UserPictures(models.Model):
    '''
    Model to manage multiple pictures of the user
    '''
    user_uuid = models.UUIDField()
    image = models.ImageField(upload_to='user_images/')