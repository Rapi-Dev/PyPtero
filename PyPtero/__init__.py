import typing

from .Sync.client.client import Client
from .Sync.client.server import Server
from .Sync.client.users import Users

class __Pterodactyl(object):
    r"""
    Base Class for passing vars through files

    Holds the API_KEY and DOMAIN

    Example Usage:
    ```
    from PyPtero import Pterodactyl, Client

    ptero = Pterodactyl(..., ...)

    Client.do_stuff()
    ```

    Note: It is not recommended to change the base
    """
    def __init__(self, api_key: str, domain: str) -> typing.NoReturn:
        self.api_key: str = api_key
        self.domain: str = domain
        self.Client = Client
        self.Server = Server
        self.Users = Users

    def update(self, target: str = '*', **kwargs):
        for i in list(kwargs.keys()):
            if i not in ['api_key', 'domain']:
                raise AttributeError('Update got an unexpected argument {!r}'.format(i))

        api_key = kwargs.get('api_key')
        domain = kwargs.get('domain')

        current_domain = self.domain
        current_apikey = self.api_key

        if api_key:
            if target == '*':
                return Pterodactyl(api_key=api_key, domain=current_domain)
            else:
                new_instance = super().__new__(self.__class__, api_key, current_domain)
                new_instance.api_key = api_key; new_instance.domain = current_domain

                _ = super().__getattribute__(target)
                _.__init__(_, pterodactyl=new_instance)

                return new_instance

        if domain:
            if target == '*':
                return Pterodactyl(current_apikey, domain)
            else:
                new_instance = super().__new__(self.__class__, current_apikey, domain)
                new_instance.api_key = current_apikey; new_instance.domain = domain

                _ = super().__getattribute__(target)
                _.__init__(_, pterodactyl=new_instance)

                return new_instance

def Pterodactyl(api_key: str, domain: str) -> __Pterodactyl:
    pterodactyl = __Pterodactyl(api_key=str(api_key), domain=str(domain))

    Client.__init__(Client, pterodactyl=pterodactyl)
    Server.__init__(Server, pterodactyl=pterodactyl)
    Users.__init__(Users, pterodactyl=pterodactyl)

    return pterodactyl
