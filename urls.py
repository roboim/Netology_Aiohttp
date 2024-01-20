from aiohttp import web
from views import AdvView


def add_application_routes(application: web.Application) -> None:
    """Добавление маршрутов приложения"""
    application.add_routes(
        [
            web.delete("/adv/{adv_id:\d+}", AdvView),
            web.get("/adv/{adv_id:\d+}", AdvView),
            web.post("/adv", AdvView),
        ]
    )
