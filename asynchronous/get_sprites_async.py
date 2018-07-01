# -*- coding: utf-8 -*-
import asyncio
import aiohttp
import aiofiles
from contextlib import contextmanager
from time import time
import os
import shutil

BASE_DIR = os.path.dirname(__file__)
PASTE = 'downloads'

if os.path.exists(PASTE):
    shutil.rmtree(PASTE)
os.makedirs(PASTE)

@contextmanager
def timeit():
    'Cria um gereciador de contexto apartir de uma função implementando os métodos dunders __enter__ e __exit__'
    start = time()
    yield
    print('Tempo de execução: {:.3f}'.format(time() - start))

async def get_urls(session, url):
    'Pega todas as urls'
    async with session.get(url) as response:
        r = await response.json()
        return r['results']

async def get_sprites_url(session, url):
    async with session.get(url['url']) as response:
        r = await response.json()
        return url['name'], r['sprites']['front_default']

async def download(session, name, url):
    'Download das imagens'
    async with session.get(url) as response:
        filename = name + os.path.splitext(url)[1]
        filepath = os.path.join(BASE_DIR, PASTE, filename)
        async with aiofiles.open(filepath, 'wb') as f:
            while True:
                chunk = await response.content.read(1024)
                if not chunk:
                    break
                await f.write(chunk)

async def main():
    'Corotina principal'
    async with aiohttp.ClientSession() as session:
        response = await get_urls(session, 'http://pokeapi.co/api/v2/pokemon/?limit=50')
        tasks = [get_sprites_url(session, url) for url in response]
        for f in asyncio.as_completed(tasks):
            r = await f
            await download(session, r[0], r[1])
            print(r)

if __name__ == '__main__':
    with timeit():
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        loop.close()

