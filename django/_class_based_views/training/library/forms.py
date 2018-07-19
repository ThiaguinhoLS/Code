# -*- coding: utf-8 -*-
from django import forms
from .models import Author, Book
from .validators import validate_age

class AuthorModelForm(forms.ModelForm):

	class Meta:
		model = Author
		fields = '__all__'


class BookModelForm(forms.ModelForm):

	class Meta:
		model = Book
		fields = '__all__'


class AuthorForm(forms.Form):

	name = forms.CharField(label = 'Nome', min_length = 3, max_length = 50, help_text = 'Nome do author')
	age = forms.IntegerField(label = 'Idade', validators = [validate_age], help_text = 'Idade do author')

	def save(self, instance = None, *, commit = True):
		name = self.cleaned_data['name']
		age = self.cleaned_data['age']
		if instance:
			instance.name = name
			instance.age = age
			if commit:
				instance.save()
			return instance
		else:
			author = Author(name = name, age = age)
			if commit:
				author.save()
			return author


class BookForm(forms.Form):

	name = forms.CharField(label = 'Nome', min_length = 3, max_length = 50)
	number_pages = forms.IntegerField(label = 'Número de páginas')
	author = forms.ModelChoiceField(label = 'Autor', queryset = Author.objects.all())

	def save(self, instance = None, *, commit = True):
		name = self.cleaned_data['name']
		number_pages = self.cleaned_data['number_pages']
		author = self.cleaned_data['author']
		print('salvo')
		if instance:
			print('instance')
			instance.name = name
			instance.number_pages = number_pages
			instance.author = author
			if commit:
				instance.save()
			return instance
		else:
			book = Book(name = name, number_pages = number_pages, author = author)
			if commit:
				book.save()
			return book
