from ...Models.user import PterodactylUser, __attrs__, __reqattr__
from ..base import PteroSyncBase, Route
import typing
from ....exceptions import *

@typing.final
class Users(PteroSyncBase):
    def __init__(self, pterodactyl):
        self.key: str = pterodactyl.admin_key
        self.session = pterodactyl.session
        self.url: str = pterodactyl.url

        super().__init__(
            api_token=self.key,
            session=self.session,
            url=self.url
        )

        self._cache: dict = {}

        self._update()

    def _update(self):
        route = Route('GET', '/application/users')
        response = super().request(route)
        response.raise_for_status()

        json = response.json()

        for user in json['data']:
            user_ = PterodactylUser(user, self)

            self._cache.update(
                {
                    user_.object.id: user_
                }
            )

    def get_user(self, id: int):
        return self._cache.get(id)

    def fetch_user(self, id: int, *, external: bool = False):
        if not external:
            route = f'/application/users/{id}?servers'
        else:
            route = f'/application/users/external/{id}?servers'
        route = Route('GET', route)

        response = super().request(route)
        response.raise_for_status()

        json = response.json()
        user = PterodactylUser(json['attributes'])

        self._cache.update({user.object.id: user})

        return user

    def get_by_attribute(self, value: str, attribute: str, *, index: int = 0):
        def _(_):
            return getattr(_[1], attribute, None) == value
        results = list(filter(_, self._cache.items()))

        if not results:
            return None

        try:
            return results[index]
        except IndexError:
            return results[0]

    def create(self, **attrs):
        unwanted_keys = [i for i in attrs.keys() if i not in __attrs__]
        if unwanted_keys:
            raise TypeError('Got unexpected argument(s), %r - Please choose from %r' % (
                unwanted_keys, __attrs__
            ))
        cleansed = {k: v for k, v in attrs.items() if k not in __attrs__}
        if any(i for i in cleansed.keys() if i not in __reqattr__):
            raise MissingRequiredArgument('Make sure your user has the following attributes, %r' % __reqattr__)

        route = Route('POST', '/application/users', payload=attrs)
        
        response = super().request(route)

        response.raise_for_status()

        json = response.json()
        user = PterodactylUser(json['attributes'], self)
        self._cache.update({user.object.id: user})

        return user

    def __iter__(self):
        return iter(self._cache.items())

    def __getitem__(self, item: int):
        key = int(item)

        return self._cache.get(key)