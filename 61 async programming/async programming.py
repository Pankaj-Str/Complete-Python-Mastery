import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def fetch_title(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            # Use BeautifulSoup to parse the HTML and extract the <title>
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.title.string.strip() if soup.title else 'No title found'
            print(f"{url}: {title}")
            return title

async def main():
    urls = [
        "https://www.python.org",
        "https://www.github.com",
        "https://www.wikipedia.org",
        "https://www.stackoverflow.com",
        "https://www.codeswithpankaj.com"
    ]
    tasks = [fetch_title(url) for url in urls]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())