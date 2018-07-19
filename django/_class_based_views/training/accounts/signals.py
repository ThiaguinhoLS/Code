# -*- coding: utf-8 -*-
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.contrib.auth import get_user_model
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings

User = get_user_model()

@receiver(post_save, sender = User)
def create_profile(sender, **kwargs):
	user = kwargs.get('instance')
	if kwargs['created']:
		Profile.objects.create(user = user)
		send_mail(
			'Conta criada com sucesso',
			f'{user.username}, sua conta foi criada com sucesso',
			settings.DEFAULT_FROM_EMAIL,
			[user.email],
		)

@receiver(post_delete, sender = User)
def delete_profile(sender, **kwargs):
	user = kwargs.get('instance')
	send_mail(
		'Conta excluída com sucesso',
		'Agradeço por ter faito parte da equipe ...',
		settings.DEFAULT_FROM_EMAIL,
		[user.email],
	)
