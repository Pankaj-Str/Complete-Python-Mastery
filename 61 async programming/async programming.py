{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ab618d31",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting aiohttp\n",
      "  Downloading aiohttp-3.12.11-cp313-cp313-win_amd64.whl.metadata (7.9 kB)\n",
      "Collecting beautifulsoup4\n",
      "  Downloading beautifulsoup4-4.13.4-py3-none-any.whl.metadata (3.8 kB)\n",
      "Collecting aiohappyeyeballs>=2.5.0 (from aiohttp)\n",
      "  Downloading aiohappyeyeballs-2.6.1-py3-none-any.whl.metadata (5.9 kB)\n",
      "Collecting aiosignal>=1.1.2 (from aiohttp)\n",
      "  Downloading aiosignal-1.3.2-py2.py3-none-any.whl.metadata (3.8 kB)\n",
      "Collecting attrs>=17.3.0 (from aiohttp)\n",
      "  Downloading attrs-25.3.0-py3-none-any.whl.metadata (10 kB)\n",
      "Collecting frozenlist>=1.1.1 (from aiohttp)\n",
      "  Downloading frozenlist-1.6.2-cp313-cp313-win_amd64.whl.metadata (17 kB)\n",
      "Collecting multidict<7.0,>=4.5 (from aiohttp)\n",
      "  Downloading multidict-6.4.4-cp313-cp313-win_amd64.whl.metadata (5.5 kB)\n",
      "Collecting propcache>=0.2.0 (from aiohttp)\n",
      "  Downloading propcache-0.3.1-cp313-cp313-win_amd64.whl.metadata (11 kB)\n",
      "Collecting yarl<2.0,>=1.17.0 (from aiohttp)\n",
      "  Downloading yarl-1.20.0-cp313-cp313-win_amd64.whl.metadata (74 kB)\n",
      "Collecting soupsieve>1.2 (from beautifulsoup4)\n",
      "  Downloading soupsieve-2.7-py3-none-any.whl.metadata (4.6 kB)\n",
      "Collecting typing-extensions>=4.0.0 (from beautifulsoup4)\n",
      "  Downloading typing_extensions-4.14.0-py3-none-any.whl.metadata (3.0 kB)\n",
      "Requirement already satisfied: idna>=2.0 in c:\\users\\programming\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from yarl<2.0,>=1.17.0->aiohttp) (3.10)\n",
      "Downloading aiohttp-3.12.11-cp313-cp313-win_amd64.whl (445 kB)\n",
      "Downloading beautifulsoup4-4.13.4-py3-none-any.whl (187 kB)\n",
      "Downloading aiohappyeyeballs-2.6.1-py3-none-any.whl (15 kB)\n",
      "Downloading aiosignal-1.3.2-py2.py3-none-any.whl (7.6 kB)\n",
      "Downloading attrs-25.3.0-py3-none-any.whl (63 kB)\n",
      "Downloading frozenlist-1.6.2-cp313-cp313-win_amd64.whl (46 kB)\n",
      "Downloading multidict-6.4.4-cp313-cp313-win_amd64.whl (38 kB)\n",
      "Downloading propcache-0.3.1-cp313-cp313-win_amd64.whl (44 kB)\n",
      "Downloading soupsieve-2.7-py3-none-any.whl (36 kB)\n",
      "Downloading typing_extensions-4.14.0-py3-none-any.whl (43 kB)\n",
      "Downloading yarl-1.20.0-cp313-cp313-win_amd64.whl (92 kB)\n",
      "Installing collected packages: typing-extensions, soupsieve, propcache, multidict, frozenlist, attrs, aiohappyeyeballs, yarl, beautifulsoup4, aiosignal, aiohttp\n",
      "Successfully installed aiohappyeyeballs-2.6.1 aiohttp-3.12.11 aiosignal-1.3.2 attrs-25.3.0 beautifulsoup4-4.13.4 frozenlist-1.6.2 multidict-6.4.4 propcache-0.3.1 soupsieve-2.7 typing-extensions-4.14.0 yarl-1.20.0\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 25.0.1 -> 25.1.1\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "%pip install aiohttp beautifulsoup4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b4438ae9",
   "metadata": {},
   "outputs": [
    {
     "ename": "RuntimeError",
     "evalue": "asyncio.run() cannot be called from a running event loop",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mRuntimeError\u001b[39m                              Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 26\u001b[39m\n\u001b[32m     23\u001b[39m     \u001b[38;5;28;01mawait\u001b[39;00m asyncio.gather(*tasks)\n\u001b[32m     25\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[34m__name__\u001b[39m == \u001b[33m\"\u001b[39m\u001b[33m__main__\u001b[39m\u001b[33m\"\u001b[39m:\n\u001b[32m---> \u001b[39m\u001b[32m26\u001b[39m     \u001b[43masyncio\u001b[49m\u001b[43m.\u001b[49m\u001b[43mrun\u001b[49m\u001b[43m(\u001b[49m\u001b[43mmain\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32mc:\\Users\\Programming\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\asyncio\\runners.py:191\u001b[39m, in \u001b[36mrun\u001b[39m\u001b[34m(main, debug, loop_factory)\u001b[39m\n\u001b[32m    161\u001b[39m \u001b[38;5;250m\u001b[39m\u001b[33;03m\"\"\"Execute the coroutine and return the result.\u001b[39;00m\n\u001b[32m    162\u001b[39m \n\u001b[32m    163\u001b[39m \u001b[33;03mThis function runs the passed coroutine, taking care of\u001b[39;00m\n\u001b[32m   (...)\u001b[39m\u001b[32m    187\u001b[39m \u001b[33;03m    asyncio.run(main())\u001b[39;00m\n\u001b[32m    188\u001b[39m \u001b[33;03m\"\"\"\u001b[39;00m\n\u001b[32m    189\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m events._get_running_loop() \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[32m    190\u001b[39m     \u001b[38;5;66;03m# fail fast with short traceback\u001b[39;00m\n\u001b[32m--> \u001b[39m\u001b[32m191\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mRuntimeError\u001b[39;00m(\n\u001b[32m    192\u001b[39m         \u001b[33m\"\u001b[39m\u001b[33masyncio.run() cannot be called from a running event loop\u001b[39m\u001b[33m\"\u001b[39m)\n\u001b[32m    194\u001b[39m \u001b[38;5;28;01mwith\u001b[39;00m Runner(debug=debug, loop_factory=loop_factory) \u001b[38;5;28;01mas\u001b[39;00m runner:\n\u001b[32m    195\u001b[39m     \u001b[38;5;28;01mreturn\u001b[39;00m runner.run(main)\n",
      "\u001b[31mRuntimeError\u001b[39m: asyncio.run() cannot be called from a running event loop"
     ]
    }
   ],
   "source": [
    "import asyncio\n",
    "import aiohttp\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "async def fetch_title(url):\n",
    "    async with aiohttp.ClientSession() as session:\n",
    "        async with session.get(url) as response:\n",
    "            html = await response.text()\n",
    "            # Use BeautifulSoup to parse the HTML and extract the <title>\n",
    "            soup = BeautifulSoup(html, 'html.parser')\n",
    "            title = soup.title.string.strip() if soup.title else 'No title found'\n",
    "            print(f\"{url}: {title}\")\n",
    "            return title\n",
    "\n",
    "async def main():\n",
    "    urls = [\n",
    "        \"https://www.python.org\",\n",
    "        \"https://www.github.com\",\n",
    "        \"https://www.wikipedia.org\",\n",
    "        \"https://www.stackoverflow.com\"\n",
    "    ]\n",
    "    tasks = [fetch_title(url) for url in urls]\n",
    "    await asyncio.gather(*tasks)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    asyncio.run(main())"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
