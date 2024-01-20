from aiohttp import web
from models import Session


class AdvView(web.View):
    @property
    def session(self) -> Session:
        return self.request.session

    @property
    def adv_id(self):
        return int(self.request.match_info["adv_id"])

    async def get(self):
        return web.json_response({'hello': 'world!'})

    async def post(self):
        json_data = await self.request.json()
        # user = User(**json_data)
        # await add_user(self.session, user)
        return web.json_response({"id": user.id})
