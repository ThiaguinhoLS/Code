# -*- coding: utf-8 -*-

def say_hello(request):
    return {'name': 'Thiago'}

def request(request):
    return {'request': request}

from django.conf import settings

def static(request):
    return {'STATIC_URL': settings.STATIC_URL}

