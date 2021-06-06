r""" Handy utility methods to make using the API simpler """
import typing
import requests
from ...constants import *

class Route(object):
    def __init__(self, method: str, route: str, *, payload=None, headers=None, **others):
        if headers is None:
            headers = dict()
        if payload is None:
            payload = dict()

        self.method = method.upper()
        self.route = route
        self.headers = headers
        self.others = others
        self.payload = payload

        self.PREPARED = False
        self.request = None

    def __extend_uri(self, base: str) -> typing.NoReturn:
        base = base.strip('/')  # Removes trailing `/`
        base += '/{}'.format(self.route.strip('/'))

        self.route = base
        self.PREPARED = True

    def prepare(self, base: str):
        if not self.PREPARED:
            self.__extend_uri(base)

        headers = self.headers.copy()
        headers['User-Agent'] = USER_AGENT

        unprepared_request = requests.Request(self.method,  self.route,
                                              data=self.payload,
                                              headers=headers, **self.others)
        self.request = unprepared_request.prepare()


class PteroSyncBase(object):
    def __init__(self, api_token: str, url: str, session: requests.Session) -> typing.NoReturn:
        self.api_token = api_token
        self.url = url
        self.session: requests.Session = session

    def request(self, route: Route) -> requests.Response:
        if not route.PREPARED:
            route.prepare(self.url)
        required_header = self.get_headers()

        if not route.headers:
            route.headers = self.get_headers()
        else:
            route.headers = dict(**route.headers, **required_header)

        response: requests.Response = self.session.send(request=route.request)
        return response

    def get_headers(self):
        headers = {
            'Authorization': 'Bearer {0}'.format(self.api_token),
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        return headers

    def raw_request(self, **kwargs) -> requests.Response:
        request = requests.Request(**kwargs)
        return self.session.send(request.prepare())
