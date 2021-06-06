import typing
from ..base import PteroSyncBase, Route

@typing.final
class Client(PteroSyncBase):
    def __init__(self, pterodactyl) -> typing.NoReturn:
        self.url = pterodactyl.url
        self.api_token = pterodactyl.api_key
        self.session = pterodactyl.session
        self.raise_ = pterodactyl.raise_for_response

        self._details = dict()

        super().__init__(
            api_token=self.api_token,
            url=self.url,
            session=self.session,
        )

    @property
    def details(self):
        return self._details

    def fetch_details(self):
        route = Route(
            method='GET',
            route='/client/account',
        )
        response = super().request(route=route)

        if self.raise_:
            response.raise_for_status()

        print(response)