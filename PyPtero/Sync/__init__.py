import typing
from ..constants import *
from ..exceptions import *
from .API import Route
import requests
from .API.base import PteroSyncBase, Route
from .API.Application.users import Users

__all__ = (
    'Client',
    'Pterodactyl'
)


class Client(object):
    def __init__(self, *, url: str, client_key: str, session: requests.Session = requests.Session()):
        self.url = url.strip('/')
        self.key = client_key
        self.session = session

        if not url.endswith('api'):
            self.url += '/api'

        if not self.key:
            raise MissingAPIKey('Missing Client API token, You can find this from `%s/account/api`' % self.url)

        super().__init__(api_token=self.key, url=self.url, session=self.session)


class Pterodactyl(Users, PteroSyncBase):
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

        try:
            self.client = Client(url=self.url, client_key=self.client_key, session=self.session)
        except MissingAPIKey:
            self.client = None

        super(Users, self).__init__(api_token=self.admin_key, url=self.url, session=self.session)
        super().__init__(pterodactyl=self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        del self
