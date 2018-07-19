# -*- coding: utf-8 -*-

from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.contrib.auth import get_user_model
from .models import Profile
from django.core.mail import send_mail

User = get_user_model()

@receiver(post_save, sender = User)
def create_profile(sender, **kwargs):
	user = kwargs.get('instance')
	print('save', user)
	if kwargs['created']:
		Profile.objects.create(user = user)

@receiver(post_delete, sender = User)
def delete_profile(sender, **kwargs):
	user = kwargs.get('instance')
	print('delete', user)
