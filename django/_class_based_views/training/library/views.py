# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, DetailView, UpdateView
from .forms import AuthorModelForm, BookModelForm, AuthorForm, BookForm
from .models import Author, Book
from django.contrib import messages

# Class-based views

class IndexView(View):

	'Página inicial com class function'

	template_name = 'library/index.html'

	def get(self, request):
		context = {
			'authors': Author.objects.all(),
			'books': Book.objects.all()
		}
		return render(request, self.template_name, context)


class CreateAuthorView(CreateView):

	'Página para criação deum autor'

	template_name = 'library/create_author.html'
	form_class = AuthorModelForm
	success_url = reverse_lazy('library:index')


class CreateBookView(CreateView):

	'Página para criação de um livro'

	template_name = 'library/create_book.html'
	form_class = BookModelForm
	success_url = reverse_lazy('library:index')


class CreateModelsView(CreateView):

	'Página para criação dos modelos'

	success_url = reverse_lazy('library:index')


class AuthorDetailView(DetailView):

	'Página de detalhe de um autor'

	template_name = 'library/detail_author.html'
	model = Author


class BookDetailView(DetailView):

	'Página de detalhe de um livro'

	template_name = 'library/detail_book.html'
	model = Book


class AuthorUpdateView(UpdateView):
    
    template_name = 'library/update_author.html'
    model = Author
    form_class = AuthorModelForm
    success_url = reverse_lazy('library:index')

    def form_valid(self, form):
    	messages.success(self.request, 'Editado com sucesso')
    	return super(AuthorUpdateView, self).form_valid(form)


class BookUpdateView(UpdateView):

	template_name = 'library/update_book.html'
	model = Book
	form_class = BookModelForm
	success_url = reverse_lazy('library:index')

	def form_valid(self, form):
		messages.success(self.request, 'Editado com sucesso')
		return super(BookUpdateView, self).form_valid(form)


# function-based views

def index(request):

	'Página inicial com view function'

	context = {
		'authors': Author.objects.all(),
		'books': Book.objects.all()
	}
	return render(request, 'library/index.html', context)

def create_author(request):

	'Página de criação de autor com view function'

	template_name = 'library/create_author.html'
	if request.method == 'POST':
		form = AuthorForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Criado com sucesso')
			return redirect('library:index')
	else:
		form = AuthorForm()
	return render(request, template_name, {'form': form})

def create_book(request):

	'Página de criação de livro com view function'

	template_name = 'library/create_book.html'
	if request.method == 'POST':
		form = BookForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Adicionado com sucesso')
			return redirect('library:index')
	else:
		form = BookForm()
	return render(request, template_name, {'form': form})

def detail_author(request, pk):

	'Página de detalhe de um autor'

	template_name = 'library/detail_author.html'
	author = get_object_or_404(Author, pk = pk)
	return render(request, template_name, {'author': author})

def detail_book(request, pk):

	'Página de detalhe de um livro'

	template_name = 'library/detail_book.html'
	book = get_object_or_404(Book, pk = pk)
	return render(request, template_name, {'book': book})

def update_author(request, pk):

	'Página de alteração de um autor'

	template_name = 'library/update_author.html'
	author = get_object_or_404(Author, pk = pk)
	if request.method == 'POST':
		form = AuthorForm(request.POST)
		if form.is_valid():
			form.save(author)
			messages.success(request, 'Editado com sucesso')
			return redirect('library:index')
	else:
		initial = {
			'name': author.name,
			'age': author.age
		}
		form = AuthorForm(initial = initial)
	return render(request, template_name, {'form': form, 'author': author})

def update_book(request, pk):

	'Página de alteração de um livro'

	template_name = 'library/update_book.html'
	book = get_object_or_404(Book, pk = pk)
	if request.method == 'POST':
		form = BookForm(request.POST)
		if form.is_valid():
			form.save(book)
			messages.success(request, 'Editado com sucesso')
			return redirect('library:index')
	else:
		initial = {
			'name': book.name,
			'number_pages': book.number_pages,
			'author': book.author
		}
		form = BookForm(initial = initial)
	return render(request, template_name, {'form': form, 'book': book})








