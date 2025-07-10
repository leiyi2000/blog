from typing import Callable

import os
import asyncio

import django
from aerich import Command
from tortoise import Tortoise
from django.core.asgi import get_asgi_application
from asgiref.compatibility import guarantee_single_callable

from .settings import TORTOISE_ORM, APP_NAME


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
django.setup(set_prefix=False)
django_asgi_app = get_asgi_application()


class LifespanApp:
    def __init__(self, app: Callable):
        self.app = guarantee_single_callable(app)

    async def __call__(self, scope, receive, send):
        if scope["type"] == "lifespan":
            await self.lifespan(scope, receive, send)
        else:
            await self.app(scope, receive, send)

    async def lifespan(self, scope, receive, send):
        while True:
            message = await receive()
            if message["type"] == "lifespan.startup":
                await self.on_startup()
                await send({"type": "lifespan.startup.complete"})
            elif message["type"] == "lifespan.shutdown":
                await self.on_shutdown()
                await send({"type": "lifespan.shutdown.complete"})

    async def on_startup(self):
        async with Command(
            tortoise_config=TORTOISE_ORM,
            app=APP_NAME,
            location="./migrations",
        ) as command:
            await command.init()
            await command.upgrade(run_in_transaction=True)
        await Tortoise.init(TORTOISE_ORM)
        await Tortoise.generate_schemas()

    async def on_shutdown(self):
        await Tortoise.close_connections()


application = LifespanApp(django_asgi_app)
