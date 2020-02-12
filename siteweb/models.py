'''
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.user.first_name#username

	def create_profile(sender, **kwargs):
		if kwargs['created']:
			user_profile = UserProfile.objects.create(user=kwargs['instance'])

		post_save.connect(create_profile, sender=User)
'''