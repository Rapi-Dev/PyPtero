from ...Models import PterodactylUser
from ..base import PteroSyncBase, Route
import typing

@typing.final
class Users(PteroSyncBase):
    def __init__(self, pterodactyl):
        self.key = pterodactyl.admin_key
        self.session = pterodactyl.session
        self.url = pterodactyl.url

        super().__init__(
            api_token=self.key,
            session=self.session,
            url=self.url
        )

        self._cache = {}

    def _update(self):
        route = Route('GET', '/application/users?servers=true')
        response = super().request(route)
        response.raise_for_status()

        json = response.json()

        for user in json['data']:
            user_ = PterodactylUser(user['attributes'], self)

            self._cache.update(
                {
                    user_.object.id: user_
                }
            )

    def get_user(self, id: int):
        return self._cache.get(id)

    def fetch_user(self, id: int):
        route = f'/application/users/{id}?servers=True'
        route = Route('GET', route)

        response = super().request(route)
        response.raise_for_status()

        json = response.json()
        user = PterodactylUser(json['attributes'])

        self._cache.update({user.object.id: user})

        return user