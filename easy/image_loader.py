import asyncio
import aiofiles
import aiohttp
import random

photos_url = 'https://picsum.photos/200'


async def upload_image(session, url: str):
    async with session.get(url) as response:
        if response.status == 200:
            data = await response.read()
            return data
        else:
            return None


def get_image_hasher(m, x):
    def hasher(data: bytes):
        p = 1
        ans = 0
        for i in range(len(data)):
            ans = (ans + data[i] * p) % m
            p = (p * x) % m
        return ans

    return hasher


async def save_image(filename, data):
    file = await aiofiles.open(filename, 'w+b')
    await file.write(data)
    await file.close()


async def upload_images(n: int, directory: str):
    distinct_images = dict()
    m = 480208559894147258675444406469
    x = random.randint(10 ** 2, 10 ** 8)
    hasher = get_image_hasher(m, x)
    async with aiohttp.ClientSession() as session:
        while len(distinct_images) < n:
            await asyncio.sleep(2)
            left = n - len(distinct_images)
            tasks = [asyncio.create_task(upload_image(session, photos_url)) for _ in range(left)]
            for t in asyncio.as_completed(tasks):
                res = await t
                if res is None:
                    continue
                h = hasher(res)
                if h not in distinct_images:
                    distinct_images[h] = res

    save_tasks = [asyncio.create_task(save_image(directory + f'/photos/photo{str(h)}.jpg', data)) for h, data in
                  distinct_images.items()]
    await asyncio.gather(*save_tasks)


def main():
    img_count = int(input('Enter number of images to upload: '))
    img_directory = input('Enter directory where you want to store pictures: ')
    asyncio.run(upload_images(img_count, img_directory))


if __name__ == '__main__':
    main()
