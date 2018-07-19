# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError

def validate_age(value):

	if value < 18:
		raise ValidationError(
			'%(value)s não é uma idade válida.\n',
			params = {'value': value},
		)