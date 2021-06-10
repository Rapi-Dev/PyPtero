from pydantic import BaseModel
from requests import Response
from ..API.base import Route

__attrs__ = {'email', 'username', 'first_name', 'last_name', 'language', 'password'}

class PterodactylUserModel(BaseModel):
    id: int
    external_id: str
    uuid: str
    username: str
    email: str
    first_name: str
    last_name: str
    language: str
    root_admin: bool = False
    _2fa: bool = False
    created_at: str
    updated_at: str
    servers: list = []

class PterodactylUser(object):
    def __init__(self, json: dict, base):
        self.object = PterodactylUserModel(**json['attributes'])
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
        return self.object.item