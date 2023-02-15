import aiohttp
import asyncio
from demo import create_app

app = create_app()

if __name__ == '__main__':
    aiohttp.web.run_app(app, )
