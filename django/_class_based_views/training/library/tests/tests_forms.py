# -*- coding: utf-8 -*-
from django.test import TestCase
from django.shortcuts import reverse
from ..forms import AuthorForm, BookForm
from ..models import Author, Book

class TestAuthorForm(TestCase):

	@classmethod
	def setUpClass(cls):
		self.assertFalse(Author.objects.all())

	def test_success_create_author_with_form(self):
		path = reverse('library:create_author')
		data = {
			'name': 'john',
			'age': 31
		}
		self.client.post(path, data)