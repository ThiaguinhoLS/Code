# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):

	'Formulário de login'

	username = forms.CharField(label = 'Username', max_length = 50)
	password = forms.CharField(label = 'Senha', max_length = 30, widget = forms.PasswordInput)
	
class UserForm(forms.Form):

	'Formulário de criação do usuário'

	username = forms.CharField(label = 'Username', max_length = 50)
	password1 = forms.CharField(label = 'Senha', max_length = 30, widget = forms.PasswordInput)
	password2 = forms.CharField(label = 'Confirme a senha', max_length = 30, widget = forms.PasswordInput)
	email = forms.EmailField(label = 'E-mail')

	def clean_password2(self):

		'Validação das senhas'

		password1 = self.cleaned_data['password1']
		password2 = self.cleaned_data['password2']
		if password1 and password2:
			if password1 != password2:
				raise forms.ValidationError('Senhas diferentes')
			else:
				if len(password1) < 8:
					raise forms.ValidationError('Senha muito curta')
		return password2

	def clean_email(self):

		'Validação do campo email'

		email = self.cleaned_data['email']
		if User.objects.filter(email = email).exists():
			raise forms.ValidationError('Email já está em uso')
		return email

	def save(self, commit = True):

		'Salva o usuário caso o formulário seja válido'

		username = self.cleaned_data['username']
		password = self.cleaned_data['password1']
		email = self.cleaned_data['email']
		user = User(username = username, password = password, email = email)
		if commit:
			user.save()
		return user


