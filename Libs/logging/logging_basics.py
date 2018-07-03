# -*- coding: utf-8 -*-
import logging

logging.basicConfig(format = '%(levelname)s: %(asctime)s: %(funcName)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def add(x, y):
    logger.info('Função funcionando perfeitamente')
    return x + y

def sub(x, y):
    logger.info('Função funcionando perfeitamente')
    return x - y

def mul(x, y):
    logger.info('Função funcionando perfeitamente')
    return x * y

def div(x, y):
    logger.info('Função funcionando perfeitamente')
    try:
        return x / y
    except ZeroDivisionError as exc:
        logger.exception('Erro em divisão por zero')
    return 0


if __name__ == '__main__':
    add(1, 2)
    sub(1, 2)
    mul(1, 2)
    div(1, 2)
    div(1, 0)
