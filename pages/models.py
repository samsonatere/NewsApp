from django.conf import settings
from django.db import models
from cloudinary.models import CloudinaryField

class Profile(models.Model):
    avatar = CloudinaryField('image')
