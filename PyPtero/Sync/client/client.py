import typing

import requests

from ..Models.user import PterodactylUser

class Client(object):
    def __init__(self, pterodactyl) -> None:
        self.__domain: str = pterodactyl.domain.strip('/')
        self.__api_key: str = pterodactyl.api_key
        self.session: requests.Session = pterodactyl.session

        self.BASE_HEADER: dict = {
            "Authorization": "Bearer {api_token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "cookie": ""
        }

        self.cache = {}

        if not self.__domain.endswith('api'):
            self.__domain += '/api'

    @property
    def api_key(self):
        return self.__api_key

    @property
    def domain(self):
        return self.__domain

    def fetch_account(self, session_id: str) -> PterodactylUser:
        BASE_HEADER = self.BASE_HEADER.copy()
        BASE_HEADER['Authorization'].format(api_token=self.__api_key)

        if BASE_HEADER['cookie'].startswith('pterodactyl_session='):
            BASE_HEADER['cookie'] = session_id
        else:
            BASE_HEADER['cookie'] = 'pterodactyl_session=' + session_id

        url = self.__domain + '/client/account'

        request = requests.Request(method='GET', url=url, headers=BASE_HEADER)
        prepared_response = request.prepare()

        resp = self.session.send(prepared_response)

        if resp.status_code == 200:
            self.cache.update({session_id: resp.json()})

        return PterodactylUser(response=resp.json(), status_code=resp.status_code)

    def get_account(self, *, session_id: str) -> typing.Union[object, None]:
        return self.cache.get(session_id)
