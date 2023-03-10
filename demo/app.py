from aiohttp import web
from .routes import setup_routes
import jinja2
import aiohttp_jinja2


async def create_app():
    app = web.Application()
    aiohttp_jinja2.setup(app,
                         loader=jinja2.PackageLoader('demo', 'templates')
                         )
    setup_routes(app)
    return app
