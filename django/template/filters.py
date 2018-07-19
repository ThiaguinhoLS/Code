# -*- coding: utf-8 -*-
from django.template import Library
from django.template.defaultfilters import stringfilter

@register.filter(name = 'cut') # Se não especificado o nome do filtro o nome da função será usado
@stringfilter                  # Transforma o value passado numa string antes e chamar o filtro em si
def cut(value, arg):
    return value.replace(arg, '')

@register.filter(name = 'lower')
@stringfilter
def lower(value):
    return value.lower()

@register.filter(name = 'capfirst')
@stringfilter
def capfirst(value):
    return value.capitalize()


# Filtros

# {{ name|lower }} transformará todas as letras da variável name em minúsculas exemplo: 'Thiago' >>> 'thiago'
# {{ bio|truncatewords:2 }} exibirá as primeiras 2 palavras da variável bio exemplo: 'Thiago luiz silva' >>> Thiago luiz'
# {{ value|default:'nothing' }} caso a variável seja False ou '' mostrará 'nothing' exemplo: '' >>> 'nothing'
# {{ value|length }} retorna o comprimento do valor caso o mesmo seja um iterável exemplo: [1, 2] >>> 2
# {{ value|filesizeformat }} formata o valor como um tamanho de arquivo legível exemplo: '13 KB' '4.1 MB'
