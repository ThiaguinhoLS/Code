# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):

	date_birth = models.DateField(verbose_name = 'data de nascimento', blank = True, null = True)
	age = models.PositiveSmallIntegerField(verbose_name = 'Idade', blank = True, null = True)
	user = models.ForeignKey(User, verbose_name = 'Usuário', on_delete = models.CASCADE)

	def __str__(self):
		return self.user.username

	class Meta:
		verbose_name = 'Perfil'
		verbose_name_plural = 'Perfis'
