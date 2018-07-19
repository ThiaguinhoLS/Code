# -*- coding: utf-8 -*-
from django.urls import path, re_path
from django.views.generic import UpdateView
from django.conf import settings
from . import views
from .forms import AuthorModelForm, BookModelForm

app_name = 'library'

if settings.CLASSES_BASED:
	urlpatterns = [
		path('', views.IndexView.as_view(), name = 'index'),
		path('author/create/',
			views.CreateModelsView.as_view(
				form_class = AuthorModelForm,
				template_name = 'library/create_author.html'
			),
			name = 'create_author'
		),
		path('book/create/',
			views.CreateModelsView.as_view(
				form_class = BookModelForm,
				template_name = 'library/create_book.html'
			),
			name = 'create_book'
		),
		re_path(r'^author/detail/(?P<pk>\d+)/$', views.AuthorDetailView.as_view(), name = 'detail_author'),
		re_path(r'^book/detail/(?P<pk>\d+)/$', views.BookDetailView.as_view(), name = 'detail_book'),
		re_path(r'^author/update/(?P<pk>\d+)/$', views.AuthorUpdateView.as_view(), name = 'update_author'),
		re_path(r'^book/update/(?P<pk>\d+)/$', views.BookUpdateView.as_view(), name = 'update_book'),
	]
else:
	urlpatterns = [
		path('', views.index, name = 'index'),
		path('author/create/', views.create_author, name = 'create_author'),
		path('book/create/', views.create_book, name = 'create_book'),
		re_path(r'^author/detail/(?P<pk>\d+)/$', views.detail_author, name = 'detail_author'),
		re_path(r'^book/detail/(?P<pk>\d+)/$', views.detail_book, name = 'detail_book'),
		re_path(r'^author/update/(?P<pk>\d+)/$', views.update_author, name = 'update_author'),
		re_path(r'^book/update/(?P<pk>\d+)/$', views.update_book, name = 'update_book'),
	]


