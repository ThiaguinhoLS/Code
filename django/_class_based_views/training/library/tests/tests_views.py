# -*- coding: utf-8 -*-
from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve
from .. import models
from .. import views
from ..views import CreateModelsView, CreateAuthorView, CreateBookView, IndexView
from model_mommy import mommy

class TestIndexView(TestCase):

	'Teste da view index'

	def test_success_status_code_view(self):
		path = reverse('library:index')
		response = self.client.get(path)
		self.assertEqual(response.status_code, 200)

	def test_resolve_url_to_view(self):
		view = resolve('/')
		self.assertEqual(view.view_name, 'library:index')
		self.assertEqual(view.func.view_class, IndexView)

	def test_template_used_in_view(self):
		path = reverse('library:index')
		response = self.client.get(path)
		self.assertTemplateUsed(response, 'library/base.html')
		self.assertTemplateUsed(response, 'library/index.html')


class TestCreateModelsViewWithBookModel(TestCase):

	'Testes referente a criação de livros'

	def test_success_status_code_view(self):
		path = reverse('library:create_book')
		response = self.client.get(path)
		self.assertEqual(response.status_code, 200)

	def test_resolve_url_to_view(self):
		view = resolve('/create/book/')
		self.assertEqual(view.view_name, 'library:create_book')
		self.assertEqual(view.func.view_class, CreateModelsView)

	def test_template_used_in_view(self):
		path = reverse('library:create_book')
		response = self.client.get(path)
		self.assertTemplateUsed(response, 'library/base.html')
		self.assertTemplateUsed(response, 'library/create_book.html')


class TestCreateModelsViewWithAuthorModel(TestCase):

	'Testes referente a criação de autores'

	def test_success_status_code_view(self):
		path = reverse('library:create_author')
		response = self.client.get(path)
		self.assertEqual(response.status_code, 200)

	def test_resolve_url_to_view(self):
		view = resolve('/create/author/')
		self.assertEqual(view.view_name, 'library:create_author')
		self.assertEqual(view.func.view_class, CreateModelsView)

	def test_template_used_in_view(self):
		path = reverse('library:create_author')
		response = self.client.get(path)
		self.assertTemplateUsed(response, 'library/base.html')
		self.assertTemplateUsed(response, 'library/create_author.html')


class TestAuthorDetailView(TestCase):

	@classmethod
	def setUpClass(cls):
		cls.author = mommy.make(models.Author, name = 'John')

	def test_success_status_code_view(self):
		path = reverse('library:detail_author', kwargs = {'pk': self.author.pk})
		response = self.client.get(path)
		self.assertEqual(response.status_code, 200)

	def test_resolve_url_to_view(self):
		view = resolve('/author/detail/{}/'.format(self.author.pk))
		self.assertEqual(view.view_name, 'library:detail_author')
		self.assertEqual(view.func.view_class, AuthorDetailView)

	def test_template_used_in_view(self):
		path = reverse('library:detail_author', args = (self.author.pk,))
		response = self.client.get(path)
		self.assertTemplateUsed(response, 'library/base.html')
		self.assertTemplateUsed(response, 'library/detail_author.html')

	@classmethod
	def tearDownClass(cls):
		cls.author.delete()


class TestBookDetailView(TestCase):

	@classmethod
	def setUpClass(cls):
		cls.book = mommy.make(models.Book)

	def test_success_status_code_view(self):
		path = reverse('library:detail_book', kwargs = {'pk': self.book.pk})
		response = self.client.get(path)
		self.assertEqual(response.status_code, 200)

	def test_resolve_url_in_view(self):
		view = resolve('/book/detail/{}/'.format(self.book.pk,))
		self.assertEqual(view.view_name, 'library:detail_book')
		self.assertEqual(view.func.view_class, BookDetailView)

	def test_template_used_in_view(self):
		path = reverse('library:detail_book', args = (self.book.pk,))
		response = self.client.get(path)
		self.assertTemplateUsed(response, 'library/base.html')
		self.assertTemplateUsed(response, 'library/detail_book.html')

	@classmethod
	def tearDownClass(cls):
		cls.book.delete()
