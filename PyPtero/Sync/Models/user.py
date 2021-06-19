from pydantic import BaseModel
from ..API.base import Route
import datetime

__attrs__ = {
    'email', 'username', 'first_name', 'last_name', 'language', 'password',
    'external_id', 'root_admin',
}

__reqattr__ = {
    'email', 'username', 'first_name', 'last_name'
}


class PterodactylUserModel(BaseModel):
    id: int
    uuid: str
    username: str
    email: str
    first_name: str
    last_name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

    external_id: str = None
    language: str = 'en'
    root_admin: bool = False
    _2fa: bool = False
    servers: list = []
    meta = {}


class PterodactylUser(object):
    def __init__(self, json: dict, base):
        if json.get('meta'):
            meta = json['meta']
        else:
            meta = ''
        meta = meta or {}

        json['attributes']['created_at'] = datetime.datetime.fromisoformat(json['attributes']['created_at'])
        json['attributes']['updated_at'] = datetime.datetime.fromisoformat(json['attributes']['updated_at'])

        self.object = PterodactylUserModel(**json['attributes'], meta=meta)
        self.base = base
        self.json = json

    def update(self, **attr):
        unwanted_keys = [i for i in attr.keys() if i not in __attrs__]
        if unwanted_keys:
            raise TypeError('Got unexpected argument(s), %r - Please choose from %r' % (
                unwanted_keys, __attrs__
            ))

        request = Route('PATCH', '/application/users/{}'.format(self.object.id), payload=attr)

        response = self.base.request(request)
        response.raise_for_status()

        return super().__new__(response.json(), self.base)

    def delete(self):
        request = Route('DELETE', '/application/users/{}'.format(self.object.id))

        response = self.base.request(request)
        response.raise_for_status()

        return True

    def copy(self):
        return super().__new__(self.json, self.base)

    def __getattr__(self, item):
        if item == '2fa':
            item = '_2fa'

        return getattr(self.object, item, None)
