import aiohttp
import aiohttp.web_response
from aiohttp_jinja2 import template


@template('index.html')
async def index(request):
    return {}
