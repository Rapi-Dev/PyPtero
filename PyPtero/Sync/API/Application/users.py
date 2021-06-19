from ...Models.user import PterodactylUser, __attrs__, __reqattr__
from ..base import PteroSyncBase, Route
import typing
from ....exceptions import *

params = {
    'servers': True
}


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

        self.cached_users: dict = {}

        self._update()

    def _update(self):
        route = Route('GET', '/application/users', params=params)
        response = super().request(route)
        response.raise_for_status()

        json = response.json()

        meta = json.get('meta')

        if meta and meta.get('pagination'):
            pages = meta['pagination']['total_pages']
            current_page = meta['pagination']['current_page']
        else:
            pages = None

        for user in json['data']:
            user_ = PterodactylUser(user, self)

            self.cached_users.update(
                {
                    user_.object.id: user_
                }
            )
        if pages:
            for page_number in range(current_page, (pages + 1)):
                route = Route('GET', '/application/users/?page=%s' % page_number, params=params)
                response = super().request(route)
                response.raise_for_status()

                json = response.json()

                for user in json['data']:
                    user_ = PterodactylUser(user, self)

                    self.cached_users.update(
                        {
                            user_.object.id: user_
                        }
                    )

    def get_user(self, id: int):
        return self.cached_users.get(id)

    def fetch_user(self, id: int, *, external: bool = False):
        if not external:
            route = f'/application/users/{id}'
        else:
            route = f'/application/users/external/{id}'
        route = Route('GET', route, params=params)

        response = super().request(route)
        response.raise_for_status()

        json = response.json()
        user = PterodactylUser(json, self)

        self.cached_users.update({user.object.id: user})

        return user

    def get_user_by_attribute(self, attribute: str, value: str, *, index: int = 0):
        def _(_):
            return getattr(_[1], attribute, None) == value
        filtered = list(filter(_, self.cached_users.items()))

        if not filtered or len(filtered) < index:
            return None

        return filtered[index]

    def fetch_user_by_attribute(self, attribute: str, value: str, *, index: int = 0):
        def _(_):
            return getattr(_[1], attribute, None) == value

        route = f'/application/users?filter[%s]=%s' % (attribute, value)

        route = Route('GET', route, params=params)
        response = super().request(route)
        response.raise_for_status()

        json = response.json()
        users = []
        for user in json['data']:
            user = PterodactylUser(user, self)
            users.append(user)
            self.cached_users.update({user.id: user})

        filtered = list(filter(_, users))

        if not filtered or len(filtered) < index:
            return None

        return filtered[index]

    def create_user(self, **attrs):
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
        self.cached_users.update({user.object.id: user})

        return user

    def __iter__(self):
        return iter(self.cached_users.items())

    def __getitem__(self, item: int):
        key = int(item)

        return self.cached_users.get(key)