# -*- coding: utf-8 -*-
import asyncio

async def coro(time):
    print('Iniciando corotina')
    await asyncio.sleep(time)
    print('Finalizando corotina')
    return 'Done'

def callback(f):
    print('Resultado:', f.result())

loop = asyncio.get_event_loop()
task = loop.create_task(coro(1))
task.add_done_callback(callback)
loop.run_until_complete(task)
loop.close()
