# -*- coding: utf-8 -*-
from django.apps import AppConfig

class AccountsConfig(AppConfig):
	
    name = 'accounts'
    verbose_name = 'Contas'

    def ready(self):
    	from .signals import create_profile, delete_profile
