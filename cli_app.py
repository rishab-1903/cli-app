import aiohttp
import asyncio
import argparse

async def fetch_url(session, url):
    try:
        async with session.get(url) as response:
            content = await response.text()
            print(f"URL: {url} | Status: {response.status} | Content Length: {len(content)}")
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")

async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Async http request with CLI")
    parser.add_argument("urls", metavar="URL", nargs="+", help="One or more URLs to fetch")
    args=parser.parse_args()


    asyncio.run(main(args.urls))
"""added a comment"""