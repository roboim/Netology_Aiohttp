import json
from aiohttp import web
from sqlalchemy.exc import IntegrityError

from models import Session, Advertisement


def get_http_error(error_class, message):
    return error_class(
        text=json.dumps({'error': message}),
        content_type='application/json'
    )


async def get_advertisement_by_id(session: Session, adv_id: int):
    """Получить объявление по номеру"""
    advertisement = await session.get(Advertisement, adv_id)
    if advertisement is None:
        raise get_http_error(web.HTTPNotFound, f'Advertisement with id {adv_id} not found')
    return advertisement


async def add_advertisement(session: Session, advertisement: Advertisement):
    """Создать объявление"""
    try:
        session.add(advertisement)
        await session.commit()
    except IntegrityError:
        raise get_http_error(web.HTTPConflict, f'Advertisement with name {advertisement.title} already exists')
    return advertisement

