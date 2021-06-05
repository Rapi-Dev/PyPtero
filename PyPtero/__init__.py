import typing
import requests
from .Sync.client import Client

class Pterodactyl(object):
    def __init__(self, api_key: str, domain: str) -> typing.NoReturn:
        self.api_key = api_key
        self.domain = domain.strip('/')
        self.session = requests.Session()

        self.client = Client(pterodactyl=self)
