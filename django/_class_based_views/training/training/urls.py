# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
	path('', include('library.urls', namespace = 'library')),
	path('accounts/', include('accounts.urls', namespace = 'accounts')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
	import debug_toolbar
	urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

