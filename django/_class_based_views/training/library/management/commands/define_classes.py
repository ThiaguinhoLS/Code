# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.core.management import call_command

class Command(BaseCommand):

	help = 'Alterna entre function-based views e class-based views'

	def add_arguments(self, parser):
		parser.add_argument('typing', action="store_true")

	def handle(self, *args, **options):
		typing = options['typing']
		if typing:
			settings.CLASSES_BASED = True
		call_command('runserver')
