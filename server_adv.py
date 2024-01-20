from aiohttp import web

from models import init_orm, engine, Session
from urls import add_application_routes


async def init_db(app: web.Application) -> None:
    """Инициализация и завершение работы с базой данных"""
    print("START")
    await init_orm()
    yield
    print("FINISH")
    await engine.dispose()


@web.middleware
async def session_middleware(request: web.Request, handler):
    """Создание сессии"""
    async with Session() as session:
        request.session = session
        response = await handler(request)
        return response

if __name__ == '__main__':
    """Создание web-сервера на основе асинхронного микрофреймворка aiohttp"""
    advertisements = web.Application()  # Создание приложения

    advertisements.cleanup_ctx.append(init_db)  # Добавление контекста
    advertisements.middlewares.append(session_middleware)  # Добавление обработчика

    add_application_routes(advertisements)  # Добавление маршрутов приложения

    web.run_app(advertisements, port=8080)  # Запуск приложения на указанном порту
