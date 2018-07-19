# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.contrib.auth import login, logout, authenticate
from django.http import HttpRequest

from django.conf import settings
from importlib import import_module

from functools import partial

class Command(BaseCommand):

	help = 'Inicializa o servidor com o usuário logado'

	def add_arguments(self, parser):
		parser.add_argument('username', help = 'Nome de usuário')
		parser.add_argument('password', help = 'Senha do usuário')

	def _handle(self, *args, **options):
		username = options['username']
		password = options['password']
		user = authenticate(username = username, password = password)
		if user is None:
			raise CommandError('Usuário ou senha inválidos')
		request = HttpRequest()
		engine = import_module(settings.SESSION_ENGINE)
		request.session = engine.SessionStore(None)
		call_command('runserver')
		login(request, user)
		
	def handle(self, *args, **options):
		username = options['username']
		password = options['password']
		user = authenticate(username = username, password = password)
		if user is None:
			raise CommandError('Usuário ou senha inválidos')
		f = partial(lambda user: lambda request: login(request, user))
		call_command('runserver')
