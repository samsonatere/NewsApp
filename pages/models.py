from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField

class Profile(models.Model):
	user = models.OneToOneField(get_user_model(), null=True, on_delete=models.CASCADE)
	role = models.CharField(max_length=20, null=True, blank=True)
	age = models.PositiveIntegerField(null=True, blank=False)
	email = models.CharField(max_length=200, null=True)
	image = CloudinaryField(default="profile1.png", null=True, blank=True)


	def __str__(self):
		return self.email
