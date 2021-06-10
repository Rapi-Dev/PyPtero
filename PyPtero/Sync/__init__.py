import typing
from ..constants import *
from .API import Route
from .API.Application import Application
import requests
from .API.base import PteroSyncBase, Route

class Pterodactyl(PteroSyncBase):
    def __init__(self, *,
                 url: str, api_key: typing.Union[str, list] = None,
                 admin_key: str = None, client_key: str = None,
                 use_ssl: bool = True,
                 ) -> typing.NoReturn:

        self.url = url.strip('/')
        self.ssl = USE_SSL[use_ssl]
        self.session = requests.Session()

        if not url.endswith('api'):
            self.url += '/api'

        if type(api_key) == list:
            self.client_key, self.admin_key = api_key
        else:
            self.admin_key = api_key

        if admin_key:
            self.admin_key = admin_key
        else:
            self.client_key = client_key

        if not getattr(self, 'client_key', None):
            self.client_key = None
        if not getattr(self, 'admin_key', None):
            self.admin_key = None

        assert self.ssl == url.split(':')[0]
        # Checks if https/http is actually being used

        # Define client now
        self.app = Application(self)

    @property
    def users(self):
        return self.app.users

