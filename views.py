from aiohttp import web
from models import Session, Advertisement
from schema import validate, CreateAdvertisement
from services import get_advertisement_by_id, add_advertisement


class AdvView(web.View):
    """Класс для работы с объявлениями"""
    @property
    def session(self) -> Session:
        return self.request.session

    @property
    def adv_id(self):
        """Получить id из параметров запроса"""
        return int(self.request.match_info["adv_id"])

    async def get_advertisement(self):
        return await get_advertisement_by_id(self.session, self.adv_id)

    async def get(self):
        advertisement = await self.get_advertisement()
        return web.json_response(advertisement.dict)

    async def post(self):
        json_data = await self.request.json()
        json_data = validate(CreateAdvertisement, json_data)
        advertisement = Advertisement(**json_data)
        await add_advertisement(self.session, advertisement)
        return web.json_response({'id': advertisement.id})

    async def delete(self):
        advertisement = await self.get_advertisement()
        await self.session.delete(advertisement)
        await self.session.commit()
        return web.json_response({'status': 'deleted', 'id': advertisement.id})
