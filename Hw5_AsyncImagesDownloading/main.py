import os
import time
import aiohttp
import asyncio
import os
import asyncio
import aiohttp  # pip install aiohttp
import aiofiles  # pip install aiofiles
from pip._internal.utils import urls

FILES_PATH = "artifacts/easy"
SITE = 'https://thiscatdoesnotexist.com/'
IMG_NUMBER = 20

if __name__ == '__main__':
    if not os.path.exists(FILES_PATH):
        path = FILES_PATH.split('/')
        for dir in path:
            if not os.path.exists(dir):
                os.mkdir(dir)
            os.chdir(dir)

    sema = asyncio.BoundedSemaphore(5)


    async def fetch_file():
        arr = SITE.split("/")
        file_name = SITE.split("/")[-2]
        async with sema, aiohttp.ClientSession() as session:
            for i in range(IMG_NUMBER):
                start = time.time()  ####
                async with session.get(SITE) as resp:
                    async with aiofiles.open(f"{FILES_PATH}/{file_name}_{i + 1}.png", "bw") as file:
                        await file.write((await resp.content.read()))
                        print(f"Time for img {i + 1}: " + str(time.time() - start))
                time.sleep(1)


    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_file())
    loop.close()
