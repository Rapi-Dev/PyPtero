import typing
from ..constants import *
from .API import Route
from .API.Client import Client
import requests

class Pterodactyl(object):
    def __init__(self, *,
                 url: str, api_key: str,
                 use_ssl: bool = True,
                 raise_for_response: bool = True
                 ) -> typing.NoReturn:
        self.url = url.strip('/')
        self.api_key = api_key
        self.ssl = USE_SSL[use_ssl]
        self.raise_for_response = raise_for_response
        self.session = requests.Session()

        if not url.endswith('api'):
            self.url += '/api'

        self.client = Client(self)

        assert self.ssl == url.split(':')[0]
        # Checks if https/http is actually being used
