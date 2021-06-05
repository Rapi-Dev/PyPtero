import typing
from ..constants import *

class Pterodactyl(object):
    def __init__(self, *,
                 url: str, api_key: str,
                 use_ssl: bool = True,
                 ) -> typing.NoReturn:
        self.url = url
        self.api_key = api_key
        self.ssl = USE_SSL[use_ssl]

        assert self.ssl == url.split(':')[0]
        ## Checks if https/http is actually being used

