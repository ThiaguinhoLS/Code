# -*- coding: utf-8 -*-
import asyncio

async def coro(time):
    print('Iniciando corotina')
    await asyncio.sleep(time) # Na declaração de await é retornado o controle ao loop de eventos
    print('Finalizando corotina')

loop = asyncio.get_event_loop() # Recebendo um loop de eventos
task = loop.create_task(coro(1)) # Cria uma task(tarefa)
loop.run_until_complete(task) # Faz com que o loop não pare até completar a task
loop.close() # Fechando o loop de eventos
