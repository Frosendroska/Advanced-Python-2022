import time
import os
import asyncio
import aiohttp  # pip install aiohttp
import aiofiles  # pip install aiofiles

FILES_PATH = "artifacts/easy"
SITE = 'https://picsum.photos/600/600?random'
FILENAME = SITE.split("/")[-2]
IMG_NUMBER = 20


async def downloading_task(i):
    async with aiohttp.ClientSession() as session:
        async with session.get(SITE) as resp:
            async with aiofiles.open(f"{FILENAME}_{i + 1}.png", "bw") as file:
                start = time.time()  ####
                await file.write((await resp.read()))
                print(f"Time for img {i + 1}: " + str(time.time() - start))  ###


async def fetch_files():
    tasks = []
    for i in range(IMG_NUMBER):
        tasks.append(asyncio.create_task(downloading_task(i)))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    path = FILES_PATH.split('/')
    if not os.path.exists(FILES_PATH):
        for curdir in path:
            if not os.path.exists(curdir):
                os.mkdir(curdir)
            os.chdir(curdir)
    else:
        for curdir in path:
            os.chdir(curdir)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_files())
    loop.close()
