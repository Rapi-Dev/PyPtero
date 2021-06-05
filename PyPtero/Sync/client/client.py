class Client(object):
    def __init__(self, pterodactyl: object) -> None:
        self.__domain = pterodactyl.domain
        self.__api_key = pterodactyl.api_key

    @property
    def api_key(self):
        return self.__api_key

    @property
    def domain(self):
        return self.__domain