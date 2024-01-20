import pydantic
from aiohttp import web

from services import get_http_error


class CreateAdvertisement(pydantic.BaseModel):
    title: str
    description: str
    user: str


def validate(schema_class, json_data):
    try:
        return schema_class(**json_data).dict(exclude_unset=True)
    except pydantic.ValidationError as er:
        error = er.errors()[0]
        error.pop('ctx', None)
        raise get_http_error(web.HTTPBadRequest, f'Please, check data')
