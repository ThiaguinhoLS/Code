# -*- coding: utf-8 -*-

def simple_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        return response
    return middleware


class SimpleMiddleware(object):

    def __init__(self, get_response = None):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response


# Desmarcar um middleware

from django.core.exceptions import MiddlewareNotUsed

class SimpleMiddleware(object):

    def __init__(self, get_response = None):
        raise MiddlewareNotUsed
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response


# Métodos especiais

class Middleware(object):

    def __init__(self, get_response = None):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, view_func, view_args, view_kwargs):
        '''
            Retorna None ou um objeto HttpResponse Se retornar None o django continuará processando esta requisição executando
            outras process_view, se retornar um objeto HttpResponse o django 
        '''
        return None 
