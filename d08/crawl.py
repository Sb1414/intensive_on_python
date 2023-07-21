import aiohttp
import asyncio
import json

async def fetch_url(session, url):
    async with session.get(url) as response:
        return url, response.status

async def crawl(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        return await asyncio.gather(*tasks)

if __name__ == "__main__":
    urls = [
        "https://example.com",
        "https://www.google.com",
        "https://www.python.org",
    ]

    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(crawl(urls))

    for url, status_code in results:
        print(f"{url}\t{status_code}")