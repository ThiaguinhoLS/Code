# -*- coding: utf-8 -*-
from django.db import models

class Author(models.Model):

	'Classe que modela um autor de livros'

	name = models.CharField(verbose_name = 'nome', max_length = 50, unique = True)
	age = models.PositiveSmallIntegerField(verbose_name = 'idade')
	created_at = models.DateTimeField(verbose_name = 'criado em ?', auto_now_add = True)
	updated_at = models.DateTimeField(verbose_name = 'editado em ?', auto_now = True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Autor'
		verbose_name_plural ='Autores'
		ordering = ('name',)


class Book(models.Model):

	'Classe que modela um livro'

	name = models.CharField(verbose_name = 'nome', max_length = 40, unique = True)
	number_pages = models.PositiveSmallIntegerField(verbose_name = 'número de páginas')
	created_at = models.DateTimeField(verbose_name = 'criado em ?', auto_now_add = True)
	updated_at = models.DateTimeField(verbose_name = 'editado em ?', auto_now = True)
	author = models.ForeignKey(verbose_name = 'autor', to = Author, on_delete = models.CASCADE, related_name = 'books')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Livro'
		verbose_name_plural = 'Livros'
		ordering = ('-name',)
