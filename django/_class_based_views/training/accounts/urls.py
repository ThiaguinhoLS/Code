# -*- coding: utf-8 -*-
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views, get_user_model
from django.shortcuts import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.generic import DetailView

from . import views

app_name = 'accounts'

User = get_user_model()

if settings.CLASSES_BASED:
	urlpatterns = [
		path('login/',
			auth_views.LoginView.as_view(
				template_name = 'accounts/login.html',
				redirect_authenticated_user = True,
			),
			name = 'login'
		),
		path('logout/',
			auth_views.LogoutView.as_view(next_page = reverse_lazy('library:index')),
			name = 'logout'
		),
		path('create/account/', views.CreateUserView.as_view(), name = 'create_account'),
		#path('profile/', login_required(views.ProfileView.as_view()), name = 'profile'),
		path('profile/', views.ProfileView.as_view(), name = 'profile'),
	]
else:
	urlpatterns = [
		path('login/', views.as_login, name = 'login'),
		path('logout/', views.as_logout, name = 'logout'),
		path('create/account/', views.create_account, name = 'create_account'),
		path('profile/', views.profile, name = 'profile'),
	]