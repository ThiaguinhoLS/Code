# -*- coding: utf-8 -*-
from django.conf import settings

def _settings(request):
    return {'settings': settings}

def media(request):
    return {'MEDIA_URL': settings.MEDIA_URL}
