# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import View, CreateView
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import LoginForm, UserForm

User = get_user_model()

class CreateUserView(CreateView):

	'Página de criação do usuário'

	template_name = 'accounts/create_account.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('library:index')


class CreateUserView(View):

	'Página de criação do usuário'

	template_name = 'accounts/create_account.html'
	form_class = UserForm
	initial = {
		'username': 'thiago',
	}

	def get(self, request):
		form = self.form_class()
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect(settings.LOGIN_REDIRECT_URL)
		return render(request, self.template_name, {'form': form})


@method_decorator(login_required, name = 'dispatch')
class ProfileView(View):

	'Página de perfil do usuário'

	template_name = 'accounts/profile.html'

	def get(self, request):
		return render(request, self.template_name)


def as_login(request):
	
	'Página de login'

	template_name = 'accounts/login.html'
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username = username, password = password)
			if user:
				login(request, user)
				messages.success(request, 'Logado com sucesso')
				return redirect(settings.LOGIN_REDIRECT_URL)
			return redirect(settings.CREATE_ACCOUNT)
	else:
		form = LoginForm()
	return render(request, template_name, {'form': form})


def as_logout(request):

	'Página de logout do site'

	logout(request)
	messages.success(request, 'Deslogado com sucesso')
	return redirect(settings.LOGOUT_REDIRECT_URL)


def create_account(request):

	'Página de criação de conta'

	template_name = 'accounts/create_account.html'
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('library:index')
	else:
		form = UserCreationForm()
	return render(request, template_name, {'form': form})


@login_required
def profile(request):

	'Página de perfil do usuário'

	template_name = 'accounts/profile.html'
	return render(request, template_name)
