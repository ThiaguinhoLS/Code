# -*- coding: utf-8 -*-
import types

class Strategy(object):

    def __init__(self, func = None):
        if func:
            self.execute = types.MethodType(func, self)

    def execute(self):
        print('Execute Strategy default')


def execute_strategy_custom(self):      # Definição de uma Strategy
    print('Execute Strategy custom')

    
def main(): # Contexto decide qual strategy será usada
    strategy = Strategy()
    strategy.execute() # 'Execute Strategy default'
    strategy = Strategy(execute_strategy_custom)
    strategy.execute()


if __name__ == '__main__':
    main()
